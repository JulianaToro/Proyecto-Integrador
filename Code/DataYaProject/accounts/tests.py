from django.test import TestCase
from .models import CustomUser

# Prueba para el modelo CustomUser
class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configura un objeto que se usará en todas las pruebas de métodos
        CustomUser.objects.create(username='testuser', email='testuser@test.com', password='testpassword', name='Test', last_name='User', company_name='Test Company', role='AD')

    def test_name_content(self):
        user = CustomUser.objects.get(id=1)
        expected_object_name = f'{user.name}'
        self.assertEquals(expected_object_name, 'Test')
