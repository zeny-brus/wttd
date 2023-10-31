from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Zeny Brus', cpf='12345678901',
                    email='zeny-brus@email.com.br', phone='55-99988-7766')
        self.client.post('/inscricao/',data)
        self.email =  mail.outbox[0]        

    def test_subscription_email_subject(self):
        
        expect = 'confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)
    
    def test_subscription_email_from(self):
        
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        
        expect = ['contato@eventex.com.br','zeny-brus@email.com.br']

        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = [
            'Zeny Brus',
            '12345678901',
            'zeny-brus@email.com.br',
            '55-99988-7766',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        