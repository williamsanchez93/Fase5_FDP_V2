# =====================================================================
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
# Problema Seleccionado: Problema #2 (Menú de Restaurante con Matriz)
# Programa: Ingeniería de Sistemas
# Universidad Nacional Abierta y a Distancia (UNAD)
# =====================================================================

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    """
    Módulo (función) que aplica la lógica de negocio.
    Retorna el precio con un 15% de descuento si cumple los criterios,
    de lo contrario retorna el precio base original.
    """
    # Convertimos a minúsculas las categorías para evitar errores por mayúsculas/minúsculas
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        return precio_base

def main():
    # 1. Datos Iniciales: Matriz bidimensional con 6 productos [Nombre, Categoría, Precio Base]
    menu_restaurante = [
        ["Hamburguesa Gourmet", "Plato Fuerte", 25000],
        ["Papas Caseras", "Entrada", 8000],
        ["Filete de Pollo", "Plato Fuerte", 18000],
        ["Limonada Cerezada", "Bebida", 7500],
        ["Brownie con Helado", "Postre", 12000],
        ["Crema de Tomate", "Entrada", 11000]
    ]

    print("=== CONFIGURACIÓN DE LA PROMOCIÓN (RESTAURANTE) ===")
    
    # 2. Captura de datos por consola (Interacción con el usuario)
    categoria_promocion = input("Ingrese la categoría objetivo para el descuento (ej: Plato Fuerte): ")
    
    try:
        umbral = float(input("Ingrese el umbral de precio mínimo para aplicar descuento (ej: 15000): "))
    except ValueError:
        print("Error: El umbral debe ser un valor numérico.")
        return

    print("\n" + "="*60)
    print(f"REPORTE DE PRECIOS - PROMOCIÓN PARA: {categoria_promocion.upper()}")
    print(f"Criterio: Categoría '{categoria_promocion}' con precio mayor a ${umbral:,.0f} (15% Desc.)")
    print("="*60)
    print(f"{'Producto':<25} | {'Categoría':<15} | {'P. Base':<10} | {'P. Final':<10}")
    print("-"*60)

    # 3. Estructura cíclica para recorrer la matriz y aplicar el módulo
    for producto in menu_restaurante:
        nombre = producto[0]
        cat = producto[1]
        precio_orig = producto[2]

        # Invocación del módulo/función de lógica de negocio
        precio_calculado = calcular_precio_final(cat, precio_orig, categoria_promocion, umbral)

        # 4. Salida de resultados formateada
        print(f"{nombre:<25} | {cat:<15} | ${precio_orig:<8,.0f} | ${precio_calculado:<8,.0f}")
        
    print("="*60)

# Punto de entrada del script
if __name__ == "__main__":
    main()