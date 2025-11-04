
import re
from usuarios import patron_email, patron_telefono, promedio




#Prueba 1 patron email
def test_patron_email_valido():
    "Verifica emails con formato correcto."
    assert patron_email.match("usuario@dominio.com") is not None, "Deberia coincidir con un email estándar"
    assert patron_email.match("nombre.apellido@sub.dominio.net") is not None, "Deberia coincidir con subdominios y puntos"
    assert patron_email.match("a@b.co") is not None, "Deberia coincidir con formatos cortos"

def test_patron_email_invalido():
    "Verifica emails con formato incorrecto."
    assert patron_email.match("usuario@dominio") is None, "No deberia coincidir sin la extensión final"
    assert patron_email.match("usuario.dominio.com") is None, "No deberia coincidir sin el simbolo @"
    assert patron_email.match("@dominio.com") is None, "No deberia coincidir si empieza con @"

#Prueba 2 patron del telefono
def test_patron_telefono_valido():
    "Verifica teléfonos con 8 a 12 digitos."
    assert patron_telefono.match("12345678") is not None, "Deberia coincidir con 8 digitos"
    assert patron_telefono.match("123456789012") is not None, "Deberia coincidir con 12 digitos"
    assert patron_telefono.match("9999999999") is not None, "Deberia coincidir con 10 digitos"

def test_patron_telefono_invalido():
    "Verifica teléfonos fuera del rango de 8 a 12 digitos o con caracteres no numéricos."
    assert patron_telefono.match("1234567") is None, "No deberia coincidir con menos de 8 digitos"
    assert patron_telefono.match("1234567890123") is None, "No deberia coincidir con más de 12 digitos"
    assert patron_telefono.match("1234a678") is None, "No deberia coincidir con caracteres no numéricos"
    assert patron_telefono.match("") is None, "No deberia coincidir con una cadena vacia"

#Prueba3 a la funcion para calcular un promedio
def test_calculo_promedio_simple():
    "Calcula el promedio de una lista simple."
    edades = [20, 30, 40]
    resultado = promedio(edades)
    assert resultado == 30.0, f"El promedio de {edades} deberia ser 30.0, se obtuvo {resultado}"

def test_calculo_promedio_con_decimales():
    "Calcula el promedio que resulta en un decimal."
    numeros = [10, 20, 30, 40, 50]
    resultado = promedio(numeros)
    assert resultado == 30.0, f"El promedio de {numeros} deberia ser 30.0, se obtuvo {resultado}"

def test_calculo_promedio_flotante():
    "Calcula el promedio con números flotantes."
    valores = [1.5, 2.5, 3.5]
    resultado = promedio(valores)
    assert resultado == 2.5, f"El promedio de {valores} deberia ser 2.5, se obtuvo {resultado}"

def test_calculo_promedio_con_cero_o_negativos():
    "Calcula el promedio incluyendo 0 o números negativos."
    valores = [10, 0, -10]
    resultado = promedio(valores)
    assert resultado == 0.0, f"El promedio de {valores} deberia ser 0.0, se obtuvo {resultado}"
