from django.urls import path
from . import views

app_name = 'business'
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.Dashboard.as_view(), name="dashboard"),
    path("change_info", views.Change_info.as_view(), name="change_info"),
    path("add_product", views.Add_product.as_view(), name="add_product"),
    path("order", views.Orders.as_view(), name="order"),
    path("change_password", views.Change_password.as_view(), name="change_password"),
    path("payment", views.Payments.as_view(), name="payment"),
]

'''
index: sends get request to display the index page. It gets a 200 status code response if user is not authenticated 
and a 302 redirect to dashboard if the user is already authenticated. This can be tested using the test cases in the test folder

All the http get request made on all other routes get a 302 redirect to login page if user is not authenticated, as all 
their views are inheriting from Django LoginRequiredMixin class

'''