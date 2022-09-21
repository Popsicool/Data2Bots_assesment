from django.test import TestCase
from business.models import Payment, Order, Product
from django.contrib.auth.models import User, auth

class TestModels(TestCase):

    def setUp(self):
        self.product_name= 'TestProduct'
        self.product = Product.objects.create(
            name=self.product_name, description='this product is for testing purpose',
            price=2000,quantity=35
        )
        Product.objects.create(
            name='Test Product', description='this product is for testing purpose',
            price=2000,quantity=35
        )
        self.user = User.objects.create_user(
            username='Test1', email='testemail@gmail.com',
            first_name='sam',last_name='seg', password="testPassword"
        )
        
        self.user.save()
        self.client.login(username="Test1", password="testPassword")
        self.order= Order.objects.create(
            user=self.user, quantity=45, product=self.product, amount=5000
        )
        self.payment = Payment.objects.create(
           user =self.user, reference_number=8587585959,
            amount=2000
        )
        
        
    def test_quantity(self):   
        self.assertEquals(self.product.quantity, 35)
    def test_payment_status(self):   
        self.assertEquals(self.order.payment_status, False)
    def test_payment_amount(self):   
        self.assertEquals(self.payment.amount, 2000)