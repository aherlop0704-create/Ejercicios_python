l_nums = list(range(1,6))
print(f"Lista: {l_nums}")

num_quitado = l_nums.pop(1)

print(f"Numero quitado: {num_quitado}")
print(f"Lista final: {l_nums}")

l_nums.append(num_quitado)
print(f"Numero insertado al final: {l_nums}")

sublista = l_nums[2:5]
print(f"Contenido entre el 3 y 5 elmento: {sublista}")

l_nums.insert(len(l_nums)-1, 10)
print(f"Insetado 10 en la penultima posicion: {l_nums}")

l_nums.clear()
print(f"Lista vaciada: {l_nums}")

del l_nums
print(f"Lista Eliminada")