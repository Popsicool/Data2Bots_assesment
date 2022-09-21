from django.test import TestCase
from django.urls import reverse, resolve
from authz.views import login, logout, signup

class TestUrls(TestCase):

    def test_login_is_resolved(self):
        url = reverse('authz:login')
        self.assertEquals(resolve(url).func, login)
    def test_logout_is_resolved(self):
        url = reverse('authz:logout')
        self.assertEquals(resolve(url).func, logout)
    def test_signup_is_resolved(self):
        url = reverse('authz:signup')
        self.assertEquals(resolve(url).func, signup)
