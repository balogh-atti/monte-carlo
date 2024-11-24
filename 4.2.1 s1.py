import random
import matplotlib.pyplot as plt

# Paraméterek
vizsgak_szama = 4
siker_valoszinuseg = 0.25
szimulaciok_szama = 100000

# Szimuláció
osszes_vizsgak = 0
eredmenyek = []

for i in range(1, szimulaciok_szama + 1):
    vizsgak = 0
    while vizsgak < vizsgak_szama:
        vizsgak += 1
        if random.random() < siker_valoszinuseg:  # Ha átmegy a vizsgán
            break
    osszes_vizsgak += vizsgak

    # Minden 1000. szimulációnál mentjük a becsült átlagot
    if i % 1000 == 0:
        eredmenyek.append(osszes_vizsgak / i)

# Átlagos vizsgaszám kiszámítása
atlagos_vizsgaszam = osszes_vizsgak / szimulaciok_szama

# Eredmény kiírása
print(f'Átlagosan {atlagos_vizsgaszam:.4f} vizsgát tesz egy lezser hallgató.')

# Grafikus megjelenítés
plt.figure(figsize=(10, 6))
plt.plot(range(1000, szimulaciok_szama + 1, 1000), eredmenyek, label='Becsült átlagos vizsgaszám')
plt.axhline(y=2.734, color='r', linestyle='--', label='Elméleti átlagos vizsgaszám: 2.734')
plt.xlabel('Szimulációk száma')
plt.ylabel('Átlagos vizsgaszám')
plt.title('Monte Carlo szimuláció a vizsgaszámokhoz')
plt.legend()
plt.grid(True)
plt.show()
