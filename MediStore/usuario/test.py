from django.test import TestCase
from .models import Usuario, Persona
from django.contrib.auth.hashers import check_password

class UsuarioModelTest(TestCase):

    def setUp(self):
        self.persona = Persona.objects.create(
            nombre_completo='Luis Pérez',
            email='luis@example.com',
            tipo_documento='CC',
            numero_documento=1,
            numero_telefono='123456789'
        )

        self.usuario = Usuario.objects.create(
            username='luis123',
            rol='admin',
            status='activo',
            numero_documento=self.persona
        )
        self.usuario.set_password('password123')
        self.usuario.save()

    def test_usuario_creacion(self):
        usuario = Usuario.objects.get(username='luis123')
        self.assertEqual(usuario.username, 'luis123')
        self.assertEqual(usuario.rol, 'admin')
        self.assertEqual(usuario.status, 'activo')
    
    def test_password_encriptado(self):
        usuario = Usuario.objects.get(username='luis123')
        self.assertTrue(check_password('password123', usuario.password))
        self.assertFalse(check_password('wrongpassword', usuario.password))

    def test_cambiar_username(self):
        self.usuario.username = 'luis456'
        self.usuario.save()
        usuario_actualizado = Usuario.objects.get(numero_documento=self.persona)
        self.assertEqual(usuario_actualizado.username, 'luis456')

    def test_cambiar_rol(self):
        self.usuario.rol = 'regente'
        self.usuario.save()

        usuario_actualizado = Usuario.objects.get(numero_documento=self.persona)
        self.assertEqual(usuario_actualizado.rol, 'regente')

    def test_cambiar_status(self):
        self.usuario.status = 'inactivo'
        self.usuario.save()

        usuario_actualizado = Usuario.objects.get(numero_documento=self.persona)
        self.assertEqual(usuario_actualizado.status, 'inactivo')
    
    def test_eliminar_usuario(self):
        self.usuario.delete()
        with self.assertRaises(Usuario.DoesNotExist):
            Usuario.objects.get(username='luis123')