import numpy as np

Carlos_matriz= np.array([[3, 4, 1], [3, 2, 1]])

soma_total = 0
for linha in Carlos_matriz:
    for elemento in linha:
        soma_total += elemento

print(f"A soma de todos os elementos da matriz é: {soma_total}")