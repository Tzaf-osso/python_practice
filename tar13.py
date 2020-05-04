"""
for i in range(50):
    if i % 3 == 0:
        dict[i] = i * 2
print(dict)

"""
dict = {}

dict = {n: n * 2 for n in range(50) if n % 3 == 0}

print(dict)
