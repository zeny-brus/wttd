from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
    def test_get(self):
        """GET/Inscricao/ deve retornar status code 200"""        
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """deve usar o template subscription/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')
    
    def test_html(self):
        """deve conter tags de input html"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response,'<input', 6)
        self.assertContains(self.response,'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response,'type="submit"')
    
    def test_csrf(self):
        """deve conter a tag de CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_has_form(self):
        """deve haver subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    def test_has_fields(self):
        """o forms deve ter 4 campos"""
        form = self.response.context['form']
        self.assertEqual(['name', 'cpf','email','phone'], list(form.fields))

