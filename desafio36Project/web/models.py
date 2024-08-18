from django.db import models


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    profesor_id = models.CharField(unique=True, max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField('Estudiante', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direccion'


class Estudiante(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateField(blank=True, null=True)
    modificacion_registro = models.DateField(blank=True, null=True)
    creador_por = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class EstudianteCurso(models.Model):
    rut_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='rut_estudiante', blank=True, null=True)
    codigo_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='codigo_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante_curso'


class Profesor(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateField(blank=True, null=True)
    modificacion_registro = models.DateField(blank=True, null=True)
    creador_por = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'