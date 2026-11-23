l_nums = [4, 7, 1, 9, 2]

l_nums.sort()
print("Lista ordenada con sort: ", *l_nums,)
print("Lista ordenada con sorted: ", *sorted(l_nums))

print(f"Maximo: {max(l_nums)}")
print(f"Minimo: {min(l_nums)}")