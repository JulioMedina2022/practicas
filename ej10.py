ventas = [
    {"producto": "teclado", "cantidad": 3, "precio": 50},
    {"producto": "mouse", "cantidad": 10, "precio": 20},
    {"producto": "monitor", "cantidad": 2, "precio": 300},
]

cantidad = [c['cantidad'] for c in ventas]
precio = [p['precio'] for p in ventas]
total_vendido = {v['producto']: v['cantidad']* v['precio'] for v in ventas}

print(f'El total vendido de cada producto es: {total_vendido}')
print(f'La suma total de ventas es de: {sum(total_vendido.values())}')
print(f'Mejor producto: {max(total_vendido, key=total_vendido.get)}')