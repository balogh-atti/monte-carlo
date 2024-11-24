import random
import matplotlib.pyplot as plt

# Paraméterek
piros_golyok_szama = 5
feher_golyok_szama = 5
osszes_golyok_szama = piros_golyok_szama + feher_golyok_szama
huzasok_szama = 5
szimulaciok_szama = 100000

# Szimulációs eredmények tárolása
legfeljebb_2_piros = 0
pontosan_2_piros = 0
legalabb_2_piros = 0
eredmenyek_legfeljebb = []
eredmenyek_pontosan = []
eredmenyek_legalabb = []

for i in range(1, szimulaciok_szama + 1):
    pirosak = 0
    for _ in range(huzasok_szama):
        # Véletlenszerűen húzunk golyót (0 - fehér, 1 - piros)
        if random.randint(1, osszes_golyok_szama) <= piros_golyok_szama:
            pirosak += 1

    # Események számolása
    if pirosak <= 2:
        legfeljebb_2_piros += 1
    if pirosak == 2:
        pontosan_2_piros += 1
    if pirosak >= 2:
        legalabb_2_piros += 1

    # Minden 1000. szimulációnál elmentjük a valószínűségeket
    if i % 1000 == 0:
        eredmenyek_legfeljebb.append(legfeljebb_2_piros / i)
        eredmenyek_pontosan.append(pontosan_2_piros / i)
        eredmenyek_legalabb.append(legalabb_2_piros / i)

# Végső valószínűségek kiszámítása
p_legfeljebb_2_piros = legfeljebb_2_piros / szimulaciok_szama
p_pontosan_2_piros = pontosan_2_piros / szimulaciok_szama
p_legalabb_2_piros = legalabb_2_piros / szimulaciok_szama

# Eredmények kiírása
print(f"Legfeljebb 2 piros valószínűsége: {p_legfeljebb_2_piros:.4f}")
print(f"Pontosan 2 piros valószínűsége: {p_pontosan_2_piros:.4f}")
print(f"Legalább 2 piros valószínűsége: {p_legalabb_2_piros:.4f}")

# Grafikon készítése
x_vals = range(1000, szimulaciok_szama + 1, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, eredmenyek_legfeljebb, label='Legfeljebb 2 piros', color='blue')
plt.plot(x_vals, eredmenyek_pontosan, label='Pontosan 2 piros', color='green')
plt.plot(x_vals, eredmenyek_legalabb, label='Legalább 2 piros', color='red')
plt.xlabel('Szimulációk száma')
plt.ylabel('Valószínűség')
plt.title('Monte Carlo szimuláció - Golyók húzása visszatevéssel')
plt.legend()
plt.grid(True)
plt.show()
