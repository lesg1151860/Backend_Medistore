from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from .models import Lote

class LoteModelTest(TestCase):

    def setUp(self):
        self.lote = Lote.objects.create(
            codigo_barras="1234567890123",
            fecha_ingreso=timezone.now().date(),
            fecha_vencimiento=timezone.now().date() + timezone.timedelta(days=365)
        )
        self.delete_url = reverse('eliminar-lote', kwargs={'codigo_barras': self.lote.codigo_barras})
    
    def test_lote_creation(self):
        lote = Lote.objects.get(codigo_barras="1234567890123")
        self.assertEqual(lote.codigo_barras, "1234567890123")
        self.assertEqual(lote.fecha_vencimiento, timezone.now().date() + timezone.timedelta(days=365))
        self.assertEqual(lote.fecha_ingreso, timezone.now().date())

    def test_fecha_vencimiento_no_anterior_a_fecha_ingreso(self):
        with self.assertRaises(ValidationError):
            lote = Lote(
                codigo_barras="9876543210987",
                fecha_ingreso=timezone.now().date(),
                fecha_vencimiento=timezone.now().date() - timezone.timedelta(days=1)
            )
            lote.full_clean()
            lote.save()

    def test_delete_lote_success(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lote.objects.filter(codigo_barras="1234567890123").exists())

    def test_delete_lote_not_found(self):
        url = reverse('eliminar-lote', kwargs={'codigo_barras': '9876543210987'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)