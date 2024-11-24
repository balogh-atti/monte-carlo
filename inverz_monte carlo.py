import numpy as np


def monte_carlo_matrix_inverse(matrix, iterations=10000):
    """
    Monte Carlo-alapú mátrix inverz közelítés.
    :param matrix: Az nxn méretű mátrix, amelynek az inverzét keressük.
    :param iterations: Iterációk száma.
    :return: A mátrix közelítő inverze.
    """
    n = matrix.shape[0]
    identity = np.eye(n)  # Egységmátrix
    inverse_estimate = np.zeros_like(matrix, dtype=float)  # Kezdeti becslés

    for _ in range(iterations):
        # Véletlenszerű vektor generálása
        random_vector = np.random.rand(n, 1)  # oszlopvektor

        # Az eredeti mátrix megoldása az adott véletlen vektorra
        try:
            solution_vector = np.linalg.solve(matrix, random_vector)
        except np.linalg.LinAlgError:
            raise ValueError("A mátrix nem invertálható.")

        # Inverz becslés frissítése (külső szorzattal)
        inverse_estimate += np.outer(solution_vector, random_vector.flatten())

    # Átlagolás az iterációk számával
    inverse_estimate /= iterations

    return inverse_estimate


# Például egy 3x3-as mátrix inverzének közelítése
A = np.array([[4, 7, 2],
              [3, 5, 1],
              [2, 1, 3]], dtype=float)

inverse_approx = monte_carlo_matrix_inverse(A, iterations=10000)
exact_inverse = np.linalg.inv(A)

print("Monte Carlo közelítő inverz:")
print(inverse_approx)
print("\nPontosan számított inverz:")
print(exact_inverse)

# Az eltérés megjelenítése
difference = np.abs(inverse_approx - exact_inverse)
print("\nEltérés:")
print(difference)
