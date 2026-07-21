# =========================================================
# Nombre del estudiante: [Samuel David Meneses]
# Grupo: [213022A_2202]
# Programa: [Fundamentos de programacion]
# Código Fuente: autoría propia
# =========================================================

# Reglas de negocio predefinidas por categoría: (Umbral, Porcentaje de descuento)
REGLAS_PROMOCION = {
    "comida rápida": {"umbral": 15000.0, "descuento": 0.15},
    "bebidas": {"umbral": 5000.0, "descuento": 0.10},
    "postres": {"umbral": 8000.0, "descuento": 0.20},
}


def calcular_precio_final(
    categoria, precio_base, reglas_promocion, para_llevar=False, recargo_para_llevar=1000.0
):
    """Calcula el precio final aplicando promociones automáticas y recargos por empaque.

    Flags (parámetros):
    - categoria: str (string/cadena de texto)
    - precio_base: float (número de coma flotante/decimal)
    - reglas_promocion: dict (diccionario/estructura clave-valor)
    - para_llevar: bool (booleano/verdadero o falso)
    - recargo_para_llevar: float (número decimal con recargo fijo)
    """
    cat_key = categoria.lower()
    aplica = False
    monto_descuento = 0.0
    umbral = 0.0
    porcentaje_descuento = 0.0

    if cat_key in reglas_promocion:
        umbral = reglas_promocion[cat_key]["umbral"]
        porcentaje_descuento = reglas_promocion[cat_key]["descuento"]

        if precio_base > umbral:
            aplica = True
            monto_descuento = precio_base * porcentaje_descuento

    costo_empaque = recargo_para_llevar if para_llevar else 0.0
    precio_final = precio_base - monto_descuento + costo_empaque

    return (
        precio_final,
        aplica,
        umbral,
        porcentaje_descuento,
        monto_descuento,
        costo_empaque,
    )


def mostrar_menu(menu):
    print("=" * 65)
    print(" MENÚ DE PRODUCTOS ".center(65, "="))
    print("=" * 65)
    print(
        f"{'No.':<4} | {'Producto':<26} | {'Categoría':<15} | {'Precio Base':>12}"
    )
    print("-" * 65)
    for i, (nombre, categoria, precio) in enumerate(menu, start=1):
        print(f"{i:<4} | {nombre:<26} | {categoria:<15} | ${precio:>10,.2f}")
    print("=" * 65)


def leer_entero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: Ingresa un número entre {minimo} y {maximo}.")
        except ValueError:
            print(
                "Error: Entrada inválida. Ingresa un número entero (int/número sin decimales)."
            )


def leer_booleano_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ["s", "si", "sí"]:
            return True
        if respuesta in ["n", "no"]:
            return False
        print("Error: Responde 's' para Sí o 'n' para No.")


if __name__ == "__main__":
    menu = [
        ["Hamburguesa Especial", "Comida Rápida", 18000],
        ["Perro Caliente XL", "Comida Rápida", 12000],
        ["Jugo Natural de Lulo", "Bebidas", 6000],
        ["Gaseosa Personal", "Bebidas", 4000],
        ["Tarta de Chocolate", "Postres", 9000],
        ["Helado Artesanal", "Postres", 4500],
    ]

    mostrar_menu(menu)

    # 1. Selección del producto por índice
    print("\n--- SELECCIÓN DE PRODUCTO ---")
    opcion_producto = leer_entero_en_rango(
        f"Elige el número del producto a consultar (1-{len(menu)}): ",
        1,
        len(menu),
    )

    # 2. Selección de servicio (para llevar o comer en el sitio)
    para_llevar = leer_booleano_si_no(
        "¿Desea el pedido para llevar? (s/n): "
    )

    # Extracción de datos del producto seleccionado
    nombre, categoria, precio_base = menu[opcion_producto - 1]

    # 3. Cálculo de la regla de negocio (evaluación automática de categoría y umbral)
    (
        precio_final,
        aplica_descuento,
        umbral,
        porcentaje_descuento,
        monto_descuento,
        costo_empaque,
    ) = calcular_precio_final(
        categoria=categoria,
        precio_base=precio_base,
        reglas_promocion=REGLAS_PROMOCION,
        para_llevar=para_llevar,
    )

    # 4. Despliegue de resultados
    print("\n" + "=" * 65)
    print(" DETALLE DE LA COMPRA ".center(65, "="))
    print("=" * 65)
    print(f"Producto seleccionado : No. {opcion_producto} - {nombre}")
    print(f"Categoría              : {categoria}")
    print(f"Precio base            : ${precio_base:,.2f}")
    print(f"Servicio               : {'Para llevar' if para_llevar else 'Para consumir en local'}")
    print("-" * 65)
    print(f"Umbral asignado cat.   : ${umbral:,.2f}")
    print(f"Aplica descuento       : {'SI' if aplica_descuento else 'NO'}")
    if aplica_descuento:
        print(f"Porcentaje descuento   : {int(porcentaje_descuento * 100)}%")
        print(f"Valor descontado       : -${monto_descuento:,.2f}")
    if para_llevar:
        print(f"Recargo por empaque    : +${costo_empaque:,.2f}")
    print("-" * 65)
    print(f"Precio final a pagar   : ${precio_final:,.2f}")
    print("=" * 65)