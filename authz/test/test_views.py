from django.test import TestCase, Client
from django.contrib.auth.models import User, auth
import json 
from django.urls import reverse, resolve


class TestViews(TestCase):
    def setUp(self):
        self.client= Client()
        self.login_url= reverse('authz:login')
        self.signup_url= reverse('authz:signup')
        self.logout_url= reverse('authz:login')
       
    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'authz/login.html')

    def test_logout_get(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code,200)

    def test_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'authz/signup.html')

   
    def test_login_post(self):
        response = self.client.post(self.login_url, {
            'username':'Samson', 'password' : 'Akinola'
        })
        self.assertEquals(response.status_code,302)
    
    def test_signup_post(self):
        response = self.client.post(self.signup_url, {
            'username':'Samson', 'password' : 'AkinolaSam', 'confirm_password': 'AkinolaSam',
            'email':'testemail@gmail.com', 'first_name': 'Samson', 'last_name':'Akinola'
        })
        self.assertEquals(response.status_code,302)
 