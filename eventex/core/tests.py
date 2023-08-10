from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
    def test_get(self):
        """GET / deve retornar status code 200"""        
        self.assertEqual(200, self.response.status_code)
        
    
    def test_template(self):
        """deve usar o template index.html"""        
        self.assertTemplateUsed(self.response,'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')

