from django.db import models


# Create your models here.
class Circuito (models.Model):

    nombre = models.TextField()
    pos_latitud = models.FloatField()
    pos_longitud = models.FloatField()
    longitud = models.FloatField()
    imagen = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        unique_together = ('nombre', 'pos_latitud', 'pos_longitud', 'longitud')


class GranPremio (models.Model):
    circuito = models.ForeignKey(Circuito)
    fecha = models.DateField()

    def __str__(self):
        return str(self.circuito) + ' - ' + str(self.fecha)

    class Meta:
        verbose_name = 'Gran Premio'
        verbose_name_plural = 'Grandes Premios'
        unique_together = ('circuito', 'fecha')


class Persona (models.Model):

    nombre = models.TextField()
    apellidos = models.TextField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

    class Meta:
        unique_together = ('nombre', 'apellidos', 'fecha_nacimiento')


class Escuderia (models.Model):

    nombre = models.TextField()
    fecha_fundacion = models.DateField()
    empleados = models.IntegerField()
    duenio = models.ForeignKey(Persona)

    def __str__(self):
        return self.nombre

    class Meta:
        unique_together = ('nombre', 'fecha_fundacion', 'empleados', 'duenio')


class Piloto (models.Model):
    persona = models.ForeignKey(Persona)
    escuderia = models.ForeignKey(Escuderia)
    numero_victorias = models.IntegerField()
    numero_podios = models.IntegerField()
    oficial = models.BooleanField(default=False)

    def __str__(self):
        return str(self.persona)

    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'
        unique_together = ('persona', 'escuderia', 'numero_victorias',
                           'numero_podios')


class Clasificacion(models.Model):
    gran_premio = models.ForeignKey(GranPremio)
    piloto = models.ForeignKey(Piloto)
    posicion = models.IntegerField()

    def __str__(self):
        return str(self.gran_premio) + ' - ' + str(self.piloto) + ' - ' \
              + str(self.posicion)

    class Meta:
        verbose_name = 'Clasificacion'
        verbose_name_plural = 'Clasificaciones'
        unique_together = ('gran_premio', 'piloto')
