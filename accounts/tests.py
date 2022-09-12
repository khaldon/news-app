from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class SignupPageTest(TestCase):
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
    
    def test_signup_forms(self):
        responses = self.client.post(reverse('signup'), {
            "username":"username"
        })
        self.assertEqual(responses.status_code, 302)
        # self.assertEqual(get_user_model().objects.all().count(), 1)
        # self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        # self.assertEqual(get_user_model().objects.all()[0].email, "mohamed@uah.com")