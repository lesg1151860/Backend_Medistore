from django.forms import ValidationError
from django.test import TestCase
from django.utils import timezone
from .models import Lote

class LoteModelTest(TestCase):

    def setUp(self):
        self.lote = Lote.objects.create(
            codigo_barras="1234567890123",
            fecha_ingreso=timezone.now().date(),
            fecha_vencimiento=timezone.now().date() + timezone.timedelta(days=365)
        )

    def test_lote_creation(self):
        """
        Prueba que el lote se cree correctamente con los datos dados.
        """
        lote = Lote.objects.get(codigo_barras="1234567890123")
        self.assertEqual(lote.codigo_barras, "1234567890123")
        self.assertEqual(lote.fecha_vencimiento, timezone.now().date() + timezone.timedelta(days=365))
        self.assertEqual(lote.fecha_ingreso, timezone.now().date())

    def test_fecha_vencimiento_no_anterior_a_fecha_ingreso(self):
        """
        Prueba que la fecha de vencimiento no sea anterior a la fecha de ingreso.
        """
        with self.assertRaises(ValidationError):  # Cambiar a ValidationError
            lote = Lote(
                codigo_barras="9876543210987",
                fecha_ingreso=timezone.now().date(),
                fecha_vencimiento=timezone.now().date() - timezone.timedelta(days=1)  # Fecha anterior
            )
            lote.full_clean()  # Ejecutar validaciones antes de guardar el objeto
            lote.save()