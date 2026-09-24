# Práctica de módulos e imports

Resuelve los ejercicios creando los archivos `.py` que se indican. No mires soluciones hasta haberlos intentado.

## 1. Función de limpieza

Crea `texto_utils.py` con una función `limpiar_nombre(nombre)` que use `.strip()` para quitar espacios al inicio y al final.

Desde `main_ejercicio_1.py`, importa el módulo completo y muestra el resultado para:

```python
nombre = "  Maria Lopez  "
```

La salida debe ser:

```text
Maria Lopez
```

## 2. Validar un dominio

En `texto_utils.py`, añade `tiene_dominio(email)`.

Debe devolver `True` únicamente si hay un punto en la parte posterior al `@`. Usa `split("@")[-1]`.

Pruébala con:

```python
"ana@empresa.com"
"ana@empresa"
"ana.lopeze@empresa"
```

## 3. Validar email

Añade `validar_email(email)` a `texto_utils.py`.

Debe devolver `True` si el texto contiene `@` y `tiene_dominio(email)` también devuelve `True`.

Pruébala con cuatro correos: dos válidos y dos no válidos.

## 4. Formatear precio

Crea `precios.py` con la función `formatear_precio(precio)`. Debe devolver el importe con dos decimales y el símbolo `€`.

Ejemplo:

```python
formatear_precio(12.5)  # "12.50€"
```

Importa solo esta función en `main_ejercicio_4.py` y muestra el precio de `49.9`.

## 5. Calcular una venta

En `precios.py`, crea estas funciones:

```python
def calcular_total(cantidad, precio_unitario):
    # devuelve cantidad multiplicada por precio_unitario

def aplicar_iva(importe, tasa=0.21):
    # devuelve el importe con IVA
```

En `main_ejercicio_5.py`, importa `precios` con el alias `p` y calcula el total de 4 unidades a 15.5 euros. Después, aplica el IVA y formatea el resultado.

## 6. Descuento

Añade `calcular_descuento(importe, porcentaje)` a `precios.py`.

En un archivo principal:

1. Calcula el total de 3 unidades a 120 euros.
2. Aplica el IVA.
3. Aplica un descuento del 15 %.
4. Muestra subtotal, total con IVA y total final, todos con dos decimales.

Usa f-strings para los mensajes.

## 7. Pedido completo

Crea `pedido_utils.py` con estas funciones:

```python
def limpiar_texto(texto):
    # usa strip

def es_email_valido(email):
    # usa @ y un punto después del @

def resumen_pedido(cliente, email, cantidad, precio_unitario):
    # limpia cliente y email, calcula el total y devuelve un texto resumen
```

El resumen debe tener este formato:

```text
Cliente: Ana | Email válido: True | Total: 39.90€
```

Prueba con datos que incluyan espacios extra al principio o al final.

## 8. Import correcto

Sin ejecutar código, escribe qué forma de import usarías en cada caso y explica por qué en un comentario:

1. Necesitas usar muchas funciones de `precios.py`.
   R/ Usaria el "import precios as p"
2. Solo necesitas `formatear_precio`.
   R/ Usaria "from precios import formatear_precio as fp"
3. Quieres acortar el nombre del módulo `pedido_utils`.
   R/Usaria "import pedido_utils as pu"

No uses `from modulo import *`.
