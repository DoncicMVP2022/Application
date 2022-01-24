from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from .views import MyTableView, CooperatorView


class ViewsTestCase(TestCase):
    def test_get_dashboard(self):
        response = self.client.get(reverse("dashboard"))
        print(response.resolver_match)
        return self.assertEqual(response.status_code, 200)
    def test_get_dashboard(self):
        response = self.client.get(reverse('cooperator'))
        print(response.resolver_match)
        return self.assertEqual(response.status_code, 200)
