from django.test import TestCase
import datetime
from producto.models import Producto
from lote.models import Lote
from .models import Item

class ItemModelTest(TestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            registro_invima='1234567890',
            nombre='Producto de prueba',
            marca='Marca de prueba',
            presentacion='Caja',
            precio=100.00
        )
        
        fecha_ingreso = datetime.date(2024, 12, 31)
        fecha_vencimiento = datetime.date(2026, 12, 31)
        
        self.lote = Lote.objects.create(
            codigo_barras='1234567890123',
            fecha_ingreso = fecha_ingreso,
            fecha_vencimiento=fecha_vencimiento,
        )

    def test_crear_item(self):
        item = Item.objects.create(
            codigo_barras='1234567890124',
            producto_id=self.producto,
            codigo_lote=self.lote,
            estado='disponible',
        )

        self.assertEqual(item.codigo_barras, '1234567890124')
        self.assertEqual(item.producto_id, self.producto)
        self.assertEqual(item.codigo_lote, self.lote)
        self.assertEqual(item.estado, 'disponible')