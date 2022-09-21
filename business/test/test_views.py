from django.test import TestCase, Client
from django.urls import reverse, resolve
from business.models import Order, Payment, Product
from django.contrib.auth.models import User, auth
import json


class TestViews(TestCase):
    def test_index_get(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code,302)

    def setUp(self):
        self.client= Client()
        self.index_url= reverse('business:index')
        self.dashboard_url= reverse('business:dashboard')
        self.change_info_url= reverse('business:change_info')
        self.change_password_url= reverse('business:change_password')
        self.payment_url= reverse('business:payment')
        self.order_url= reverse('business:order')
        self.add_product_url= reverse('business:add_product')
        self.add_url= reverse('business:change_info')
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
        return self.user
        
    def test_Dashboard_get(self):
        response = self.client.get(self.dashboard_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'business/dashboard.html')

    def test_Change_info_get(self):
        response = self.client.get(self.change_info_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'business/change_info.html')

    def test_Change_info_post(self):
        response = self.client.post(self.change_info_url, {
            'first_name':'Samson', 'last_name' : 'Akinola'
        })
        self.assertEquals(response.status_code,302)

    def test_Change_password_get(self):
        response = self.client.get(self.change_password_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'business/change_password.html')
    def test_Change_password_post(self):
        response = self.client.post(self.change_password_url, {
            'password':'Samson', 'confirm_password' : 'Akinola'
        })
        self.assertEquals(response.status_code,200)
    def test_Change_password_post(self):
        response = self.client.post(self.change_password_url, {
            'password':'Samson', 'confirm_password' : 'Samson'
        })
        self.assertEquals(response.status_code,302)
    def test_Payments_get(self):
        response = self.client.get(self.payment_url)
        self.assertEquals(response.status_code,302)
    def test_Orders_get(self):
        response = self.client.get(self.order_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'business/order.html')
    def test_Add_product_get(self):
        response = self.client.get(self.add_product_url)
        self.assertEquals(response.status_code,302)