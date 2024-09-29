from django.test import TestCase
from django.contrib.auth import get_user_model
from factura.models import Factura

User = get_user_model()

class FacturaModelTest(TestCase):

    def setUp(self):
        self.regente = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_factura(self):
        factura = Factura.objects.create(
            regente=self.regente,
            total_pagar=150.50
        )
        self.assertEqual(factura.regente, self.regente)
        self.assertEqual(factura.total_pagar, 150.50)
        self.assertIsNotNone(factura.fecha)

    def test_change_total_pagar(self):
        factura = Factura.objects.create(
            regente=self.regente,
            total_pagar=150.50
        )
        factura.total_pagar = 200.00
        factura.save()

        updated_factura = Factura.objects.get(id=factura.id)
        self.assertEqual(updated_factura.total_pagar, 200.00)

    def test_delete_factura(self):
        factura = Factura.objects.create(
            regente=self.regente,
            total_pagar=150.50
        )
        factura_id = factura.id
        factura.delete()

        with self.assertRaises(Factura.DoesNotExist):
            Factura.objects.get(id=factura_id)
