from django.forms import ValidationError
from django.test import TestCase
from .models import Persona

class PersonaModelTest(TestCase):

    def setUp(self):
        self.persona = Persona.objects.create(
            nombre_completo='Juan Pérez',
            email='juan.perez@example.com',
            tipo_documento='CC',
            numero_documento='123456789',
            numero_telefono='3123456789'
        )

    def test_crear_persona(self):
        self.assertEqual(self.persona.nombre_completo, 'Juan Pérez')
        self.assertEqual(self.persona.email, 'juan.perez@example.com')
        self.assertEqual(self.persona.tipo_documento, 'CC')
        self.assertEqual(self.persona.numero_documento, '123456789')
        self.assertEqual(self.persona.numero_telefono, '3123456789')

    def test_validacion_email(self):
        self.persona.email = 'invalid_email'
        with self.assertRaises(ValidationError):
            self.persona.full_clean()

    def test_numero_documento_unico(self):
        with self.assertRaises(Exception):
            Persona.objects.create(
                nombre_completo='Ana Gómez',
                email='ana.gomez@example.com',
                tipo_documento='CC',
                numero_documento='123456789',
                numero_telefono='3145678901'
            )
    def test_modificar_nombre_completo(self):
        nuevo_nombre = 'Juan Pérez Gómez'
        self.persona.nombre_completo = nuevo_nombre
        self.persona.save()
        self.persona.refresh_from_db()  
        self.assertEqual(self.persona.nombre_completo, nuevo_nombre)
    
    def test_eliminar_persona(self):
        # Verificar que la persona existe antes de eliminar
        self.assertTrue(Persona.objects.filter(numero_documento=self.persona.numero_documento).exists())

        # Eliminar la persona
        self.persona.delete()

        # Verificar que la persona ya no existe
        self.assertFalse(Persona.objects.filter(numero_documento=self.persona.numero_documento).exists())