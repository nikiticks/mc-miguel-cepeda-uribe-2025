import numpy as np

def gauss_jordan(matrix, b):
    n = len(b)
    augmented_matrix = np.hstack((matrix, b.reshape(-1, 1)))

    for i in range(n):
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
            else:
                raise ValueError("No se puede resolver el sistema, ya que no hay un pivote válido.")

        augmented_matrix[i] /= augmented_matrix[i, i]

        for j in range(n):
            if j != i:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]

    return augmented_matrix[:, -1]

A = np.array([[2, 0, 2],
              [4, 0, -1],
              [3, 2, -2]], dtype=float)

b = np.array([7, 18, 16], dtype=float)

try:
    solution = gauss_jordan(A, b)
    print("Solución del sistema:")
    for i, val in enumerate(solution, start=1):
        print(f"x{i} = {val}")
except ValueError as e:
    print(e)