from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    direccion = models.CharField(max_length=255, verbose_name="Dirección", blank=True, null=True)

    def __str__(self):
        texto = "{0} - {1} - {2} - {3} - {4}"
        return texto.format(self.id, self.nombre, self.email, self.telefono, self.direccion)