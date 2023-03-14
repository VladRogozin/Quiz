from accounts.views import UserRegisterView
from accounts.views import user_activate
from accounts.views import user_profile_view
from accounts.views import UserLogoutView
from accounts.views import UserLoginView

from django.test import SimpleTestCase
from django.urls import resolve
from django.urls import reverse


class TestUrls(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)

    def test_profile_url_resolves(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func, user_profile_view)

    def test_activate_user_url_resolves(self):
        url = reverse('accounts:register_activate', kwargs={'sign': 'ewsad'})
        self.assertEqual(resolve(url).func, user_activate)

    def test_login_logaut_url_resolves(self):
        """Homework test"""
        self.assertEqual(resolve(reverse('accounts:login')).func.view_class, UserLoginView)
        self.assertEqual(resolve(reverse('accounts:logout')).func.view_class, UserLogoutView)