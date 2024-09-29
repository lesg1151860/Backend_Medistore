from django.db import IntegrityError
from django.test import TestCase
from factura.models import Factura
from item.models import Item
from lote.models import Lote
from producto.models import Producto
from venta.models import Venta
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class VentaModelTest(TestCase):

    def setUp(self):
        self.regente = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

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
            codigo_barras='0123',
            fecha_ingreso=fecha_ingreso,
            fecha_vencimiento=fecha_vencimiento,
        )

        self.item = Item.objects.create(
            codigo_barras='1234567890123',
            producto_id=self.producto,
            codigo_lote=self.lote,
            estado='disponible',
        )

        self.factura = Factura.objects.create(
            regente=self.regente,
            total_pagar=150.50
        )

    def test_create_venta(self):
        self.assertIsNotNone(self.item)

        venta = Venta.objects.create(
            factura_id=self.factura,
            item_cod_barras=self.item,
            precio_unitario=50.00
        )
        self.assertEqual(venta.factura_id, self.factura)
        self.assertEqual(venta.item_cod_barras, self.item)
        self.assertEqual(venta.precio_unitario, 50.00)

    def test_create_venta_with_invalid_factura(self):
        with self.assertRaises(IntegrityError):
            Venta.objects.create(
            factura_id=None,
            item_cod_barras=self.item,
            precio_unitario=50.00
        )

    def test_create_venta_with_invalid_item(self):
        with self.assertRaises(ValueError):
            Venta.objects.create(
                factura_id=self.factura,
                item_cod_barras=None,
                precio_unitario=50.00
            )
    
    def test_create_venta_with_invalid_item(self):
        with self.assertRaises(IntegrityError):
            Venta.objects.create(
                factura_id=self.factura,
                item_cod_barras=None,
                precio_unitario=50.00
            )
    
    def test_delete_venta(self):
        venta = Venta.objects.create(
            factura_id=self.factura,
            item_cod_barras=self.item,
            precio_unitario=50.00
        )
        venta_id = venta.id
        venta.delete()

        with self.assertRaises(Venta.DoesNotExist):
            Venta.objects.get(id=venta_id)
