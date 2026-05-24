#Nombre estudiante: William Abraham Sanchez Obando
#Grupo: 213022_514
#Código Fuente: autoría propia
#Fase 5: Evaluación Final POA
#Curso: Fundamentos de Programación
#Tutor: Flor María Hernández Perez
'''Problema 2: Se gestionan los precios de un menú de restaurante. El menú se representa como una matriz: [Nombre del Producto, Categoría, Precio Base].
Se requiere una funcionalidad para aplicar una promoción a productos específicos.
Requisitos de Desarrollo
-
Matriz: Crear una matriz con al menos 6 productos de diversas categorías.
-
Módulos: Se requiere un módulo (función) para calcular el precio final de un producto.
-
Lógica de Negocio:
✓
Aplicar un 15% de descuento si el producto cumple con la categoría objetivo, específica y su precio base es mayor a un umbral definido.
✓
Mantener el precio base si no se cumplen las condiciones.
-
Salida: Mostrar cada producto, su precio base y el precio final con la promoción aplicada.
'''
def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        return precio_base

def main():

    menu_restaurante = [
        ["Hamburguesa Gourmet", "Plato Fuerte", 25000],
        ["Papas Caseras", "Entrada", 8000],
        ["Filete de Pollo", "Plato Fuerte", 18000],
        ["Limonada Cerezada", "Bebida", 7500],
        ["Brownie con Helado", "Postre", 12000],
        ["Crema de Tomate", "Entrada", 12000]
    ]

    print("=== CONFIGURACIÓN DE LA PROMOCIÓN (RESTAURANTE) ===")
    
   
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

   
    for producto in menu_restaurante:
        nombre = producto[0]
        cat = producto[1]
        precio_orig = producto[2]

      
        precio_calculado = calcular_precio_final(cat, precio_orig, categoria_promocion, umbral)

        # 4. Salida de resultados formateada
        print(f"{nombre:<25} | {cat:<15} | ${precio_orig:<8,.0f} | ${precio_calculado:<8,.0f}")
        
    print("="*60)


if __name__ == "__main__":
    main()