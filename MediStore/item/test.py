from django.forms import ValidationError
from django.test import TestCase
import datetime
from producto.models import Producto
from lote.models import Lote
from .models import Item

class ItemModelTest(TestCase):

    def setUp(self):
        self.producto = Producto.objects.create(
            registro_invima='INVIMA12345',
            nombre='Producto de prueba',
            marca='Marca de prueba',
            presentacion='Caja',
            precio=100.00
        )
        
        fecha_ingreso = datetime.date(2024, 12, 31)
        fecha_vencimiento = datetime.date(2026, 12, 31)
        
        self.lote = Lote.objects.create(
            codigo_barras='L123',
            fecha_ingreso = fecha_ingreso,
            fecha_vencimiento=fecha_vencimiento,
        )

    def test_crear_item(self):
        item = Item.objects.create(
            codigo_barras='L123',
            producto_id=self.producto,
            codigo_lote=self.lote,
            estado='disponible',
        )
        self.assertEqual(item.codigo_barras, 'L123')
        self.assertEqual(item.producto_id, self.producto)
        self.assertEqual(item.codigo_lote, self.lote)
        self.assertEqual(item.estado, 'disponible')
    
    def test_create_item_with_valid_producto_id(self):
        item = Item.objects.create(
            codigo_barras="1234567890123",
            producto_id=self.producto,
            codigo_lote=self.lote,
            estado="disponible",
            
        )
        self.assertIsInstance(item, Item)
        self.assertEqual(item.producto_id, self.producto)

    def test_create_item_with_invalid_producto_id(self):
        with self.assertRaises(ValidationError):
            item = Item(
                codigo_barras="1234567890123",
                producto_id_id=999,
                codigo_lote=self.lote,
                estado="disponible",
            )
            item.full_clean()
            item.save()
            
    def test_create_item_with_existing_lote(self):
        item = Item.objects.create(
            codigo_barras="1234567890123",
            producto_id=self.producto,
            codigo_lote=self.lote,
            estado="disponible",
        )

        self.assertIsInstance(item, Item)
        self.assertEqual(item.codigo_lote, self.lote)
        self.assertEqual(item.codigo_lote.codigo_barras, "L123")
        self.assertEqual(Item.objects.get(codigo_barras="1234567890123").codigo_lote, self.lote)