import os
import sys
import django
from datetime import date

# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio36Project.settings")
django.setup()

from web.models import Curso, Direccion, Estudiante, EstudianteCurso, Profesor


def crear_profesor():
    profesor = Profesor(
        rut="200000001",
        nombre="Marcelo",
        apellido="Cortes",
        activo=True,
        creacion_registro=date(2024, 8, 17),
        modificacion_registro=date(2024, 8, 17),
        creador_por="Maximiliano Quinteros",
    )
    profesor.save()
    print(f"Profesor creado con el rut: {profesor.rut}")


# crear_profesor()


def crear_curso():
    curso = Curso(
        codigo="0000000002",
        nombre="Lenguaje",
        version=1,
    )
    curso.save()
    print(f"Curso creado con el código: {curso.codigo}")


# crear_curso()


def crear_estudiante():
    estudiante = Estudiante(
        rut="100000001",
        nombre="Adam",
        apellido="Smith",
        fecha_nac="2000-01-01",
        activo=True,
        creacion_registro=date(2024, 8, 17),
        modificacion_registro=date(2024, 8, 17),
        creador_por="Maximiliano Quinteros",
    )
    estudiante.save()
    print(f"Estudiante creado con el rut: {estudiante.rut}")


# crear_estudiante()


def crear_direccion():
    estudiante = Estudiante.objects.get(rut="100000000")

    direccion = Direccion(
        calle="Avenida Siempreviva",
        numero="742",
        comuna="Santiago",
        ciudad="Santiago",
        region="Metropolitana",
        estudiante=estudiante,
    )

    direccion.save()
    print(f"Dirección creada para el estudiante con el rut: {estudiante.rut}")


# crear_direccion()


def obtiene_estudiante():
    estudiante = Estudiante.objects.get(rut="100000000")
    print(
        f"""Estudiante obtenido con el rut {estudiante.rut}
        Apellido: {estudiante.apellido}
        Fecha de nacimiento: {estudiante.fecha_nac}
        Activo: {estudiante.activo}"""
    )


# obtiene_estudiante()


def obtiene_profesor():
    profesor = Profesor.objects.get(rut="200000000")
    print(
        f"""Profesor obtenido con el rut {profesor.rut}
        Nombre: {profesor.nombre}
        Apellido: {profesor.apellido}
        Activo:  {profesor.activo}"""
    )


# obtiene_profesor()


def obtiene_curso():
    curso = Curso.objects.get(codigo="0000000001")
    print(
        f"""Curso obtenido con el código {curso.codigo}
        Nombre: {curso.nombre}
        Version: {curso.version}
        Rut Profesor: {curso.profesor_id}"""
    )


# obtiene_curso()


def agrega_profesor_a_curso():
    profesor = Profesor.objects.get(rut="200000001")
    curso = Curso.objects.get(codigo="0000000002")

    curso.profesor_id = profesor.rut
    curso.save()
    print(f"Profesor {profesor.rut} agregado al curso {curso.codigo}")


# agrega_profesor_a_curso()


def agrega_cursos_a_estudiante():
    estudiante= Estudiante.objects.get(rut="100000001")
    curso = Curso.objects.get(codigo="0000000002")

    estudiante_curso = EstudianteCurso(rut_estudiante=estudiante, codigo_curso=curso)
    estudiante_curso.save()
    print(f"Estudiante de rut {estudiante.rut} agregado a curso con el código {curso.codigo}")

#agrega_cursos_a_estudiante()


def imprime_estudiante_cursos():
    cursos = Curso.objects.all()
    
    for curso in cursos:
        print(f"En el curso {curso.nombre} están los siguientes estudiantes:")
        estudiante_cursos = EstudianteCurso.objects.filter(codigo_curso=curso)
        ruts_estudiantes = estudiante_cursos.values_list('rut_estudiante', flat=True)
        estudiantes = Estudiante.objects.filter(rut__in=ruts_estudiantes)
        
        for estudiante in estudiantes:
            print(f"Estudiante {estudiante.nombre} {estudiante.apellido} con el rut {estudiante.rut}")

imprime_estudiante_cursos()
