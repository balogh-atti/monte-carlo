import numpy as np
import matplotlib.pyplot as plt


def simulate_game_distribution(prob_A, prob_B, max_shots, simulations=100000):
    """
    Monte Carlo szimuláció a dobások számának eloszlásához.

    :param prob_A: A játékos találati valószínűsége.
    :param prob_B: B játékos találati valószínűsége.
    :param max_shots: Maximum dobásszám a játékban.
    :param simulations: Szimulációk száma.
    :return: Dobások számának eloszlása.
    """
    shot_counts = []

    for _ in range(simulations):
        shots = 0
        for i in range(max_shots):
            shots += 1
            if i % 2 == 0:  # A játékos dob
                if np.random.rand() < prob_A:
                    break
            else:  # B játékos dob
                if np.random.rand() < prob_B:
                    break
        shot_counts.append(shots)

    return shot_counts


# Szimuláció paraméterei
prob_A = 0.51
prob_B = 0.39
max_shots = 4
simulations = 100000

# Szimuláció futtatása
shot_counts = simulate_game_distribution(prob_A, prob_B, max_shots, simulations)

# Histogram készítése
plt.figure(figsize=(8, 5))
plt.hist(shot_counts, bins=np.arange(1, max_shots + 2) - 0.5, density=True, color='skyblue', edgecolor='black')
plt.xticks(range(1, max_shots + 1))
plt.xlabel("Dobások száma")
plt.ylabel("Relatív gyakoriság")
plt.title("A játékbeli dobások számának eloszlása")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
