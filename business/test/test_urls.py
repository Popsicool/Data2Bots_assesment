from django.test import SimpleTestCase
from django.urls import reverse, resolve
from business.views import index, Dashboard,Change_info,Change_password,Payments,Add_product,Orders

class TestUrls(SimpleTestCase):

    def test_index_is_resolved(self):
        url = reverse('business:index')
        self.assertEquals(resolve(url).func, index)

    def test_dashboard_is_resolved(self):
        url = reverse('business:dashboard')
        self.assertEquals(resolve(url).func.view_class, Dashboard)

    def test_change_info_is_resolved(self):
        url = reverse('business:change_info')
        self.assertEquals(resolve(url).func.view_class, Change_info)
    
    def test_add_product_is_resolved(self):
        url = reverse('business:add_product')
        self.assertEquals(resolve(url).func.view_class, Add_product)

    def test_order_is_resolved(self):
        url = reverse('business:order')
        self.assertEquals(resolve(url).func.view_class, Orders)
    def test_change_password_is_resolved(self):
        url = reverse('business:change_password')
        self.assertEquals(resolve(url).func.view_class, Change_password)
    def test_payment_resolved(self):
        url = reverse('business:payment')
        self.assertEquals(resolve(url).func.view_class, Payments)