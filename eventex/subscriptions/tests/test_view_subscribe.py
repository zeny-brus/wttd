from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET/Inscricao/ deve retornar status code 200"""        
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """deve usar o template subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')
    
    def test_html(self):
        """deve conter tags de input html"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
        
    def test_csrf(self):
        """deve conter a tag de CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_has_form(self):
        """deve haver subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    '''def test_has_fields(self):
        """o forms deve ter 4 campos"""
        form = self.response.context['form']
        self.assertEqual(['name', 'cpf','email','phone'], list(form.fields))
'''
class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Zeny Brus', cpf='12345678901',
                    email='zeny-brus@email.com.br', phone='55-99988-7766')
        self.response = self.client.post('/inscricao/', data) 
                
   
    def test_post(self):
        """POST válido devera redirecionar para o caminho /inscricao/"""
        self.assertEqual(302, self.response.status_code)
    
    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))    

class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})
        
    def test_post(self):
        """POST invalido não deverá redirecionar"""        
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response,'subscriptions/subscription_form.html')
    
    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)
    
class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='zeny brus', cpf='12345678901',
                    email='zeny-brus@email.com', phone='51-98877-6655')
        response = self.client.post('/inscricao/',data,follow=True)
        self.assertContains(response, 'Inscricao realizada com sucesso!')

