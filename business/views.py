from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random
from .models import Payment, Order, Product

#generates a random number to serve as reference number for each payment
def generateReferenceNumber():
    return random.randrange(1111111111, 9999999999)


def index(request):
    if request.user.is_authenticated:
        return redirect('business:dashboard')
    context = {}
    return render(request, "business/index.html", context)

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        context= {'products':products}
        return render(request, "business/dashboard.html", context)

class Change_info(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "business/change_info.html")
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if (len(first_name) < 1 or len(last_name) < 1):
             messages.info(request, "field can not be empty")
             return render(request, "business/change_info.html")
        User.objects.filter(email=request.user.email).update(
            first_name=first_name, last_name=last_name)

        messages.info(request, "Details updated succesfully")
        return redirect('business:dashboard')

class Change_password(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "business/change_password.html")
    def post(self, request):
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if (password != confirm_password):
             messages.info(request, "Password didn't match!!!")
             return render(request, "business/change_password.html")
        u = User.objects.get(username=request.user.username)
        u.set_password(password)
        u.save()
        user = auth.authenticate(username=request.user.username, password=password)
        if user is not None:
            auth.login(request, user)
        messages.info(request, "Password Changed")
        return redirect('business:dashboard')



class Payments(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if (user.is_superuser == False):
            return redirect('business:order')
        
        payments= Payment.objects.all()
        orders= Order.objects.all()
        context={'payments':payments, 'orders':orders}
        return render(request, "business/payments.html", context)


    def post(self, request):
        pk = request.POST['id']
        ref = 0
        while (ref == 0):
            ref2 = generateReferenceNumber()
            object_with_similar_ref = Payment.objects.filter(reference_number=ref2)
            if not object_with_similar_ref:
                ref = ref2
        amount = Order.objects.get(id=pk).amount
        payment = Payment.objects.create(user=request.user,reference_number=ref, amount=amount)
        payment.save()
        messages.info(request, "Payment Successful")
        Order.objects.filter(id=pk).update(payment_status=True)
        return redirect('business:order')



class Orders(LoginRequiredMixin, View):
    def get(self, request):
        orders= Order.objects.filter(user=request.user)
        context={'orders':orders}
        return render(request, "business/order.html", context)

    def post(self, request):
        quantity = request.POST['quantity']
        try:
            quantity= int(quantity)
        except:
            messages.info(request, "Quantity must be number only")
            return redirect('business:dashboard')
        product_id = int(request.POST['id'])
        product = Product.objects.get(id=product_id)
        amount= int(product.price) * int(quantity)
        order = Order.objects.create(user=request.user,quantity=quantity, amount=amount,product=product)
        order.save()
        messages.info(request, "Order has been placed")
        return redirect('business:dashboard')

class Add_product(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        if (user.is_superuser == False):
            return redirect('business:order')
        return render(request, "business/add_product.html")

    def post(self, request):
        user = request.user
        if (user.is_superuser == False):
            return redirect('business:order')
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity= request.POST['quantity']
        product = Product.objects.create(name=name, description=description,price=price,quantity=quantity)
        product.save()
        messages.info(request, "Product added")
        return redirect('business:dashboard')
def error_404(request, exception):
    return render(request, "business/404.html")

def error_500(request):
    return render(request, "business/500.html")