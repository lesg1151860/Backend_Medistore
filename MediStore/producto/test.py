from django.test import TestCase
from .models import Producto

class ProductoModelTest(TestCase):

    def setUp(self):
        # Configuramos un producto de ejemplo para usar en las pruebas
        self.producto = Producto.objects.create(
            registro_invima='INVIMA123456',
            nombre='Paracetamol',
            marca='Genfar',
            presentacion='Tableta',
            precio=1200.50
        )

    def test_producto_creacion(self):
        """Prueba que un producto se crea correctamente"""
        producto = Producto.objects.get(registro_invima='INVIMA123456')
        self.assertEqual(producto.nombre, 'Paracetamol')
        self.assertEqual(producto.marca, 'Genfar')
        self.assertEqual(producto.presentacion, 'Tableta')
        self.assertEqual(producto.precio, 1200.50)

    def test_valores_por_defecto(self):
        """Prueba que los valores por defecto se asignan correctamente"""
        producto_defecto = Producto.objects.create(
            registro_invima='INVIMA987654'
        )
        self.assertEqual(producto_defecto.nombre, 'Nombre por definir')
        self.assertEqual(producto_defecto.marca, 'Sin marca')
        self.assertEqual(producto_defecto.presentacion, 'Tableta')
        self.assertEqual(producto_defecto.precio, 0.00)

    def test_actualizacion_producto(self):
        """Prueba que un producto se puede actualizar correctamente"""
        producto = Producto.objects.get(registro_invima='INVIMA123456')
        producto.nombre = 'Ibuprofeno'
        producto.marca = 'MK'
        producto.presentacion = 'Capsula'
        producto.precio = 1500.00
        producto.save()

        # Refrescamos los datos del producto desde la base de datos
        producto_actualizado = Producto.objects.get(registro_invima='INVIMA123456')
        self.assertEqual(producto_actualizado.nombre, 'Ibuprofeno')
        self.assertEqual(producto_actualizado.marca, 'MK')
        self.assertEqual(producto_actualizado.presentacion, 'Capsula')
        self.assertEqual(producto_actualizado.precio, 1500.00)

    def test_eliminacion_producto(self):
        """Prueba que un producto se puede eliminar correctamente"""
        producto = Producto.objects.get(registro_invima='INVIMA123456')
        producto.delete()

        # Asegurarse de que el producto fue eliminado
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(registro_invima='INVIMA123456')
