import random
import time
import matplotlib.pyplot as plt

# 1. Diplomaták listája
diplomatak = ['angol'] * 5 + ['francia'] * 3 + ['olasz'] * 4

# 2. Szimulációk száma
szimulaciok_szama = 100000
sikeres_esetek = 0

# Időmérés indítása
kezdeti_ido = time.time()

# 3. Szimulációk végrehajtása és adatgyűjtés a grafikonhoz
eredmenyek = []
for i in range(1, szimulaciok_szama + 1):
    random.shuffle(diplomatak)
    elso_harom = diplomatak[:3]

    if elso_harom == ['angol', 'francia', 'olasz']:
        sikeres_esetek += 1

    if i % 1000 == 0:  # Minden 1000. lépésnél mentjük a valószínűséget
        eredmenyek.append(sikeres_esetek / i)

# Időmérés vége
vegso_ido = time.time()
futasi_ido = vegso_ido - kezdeti_ido

# 5. Valószínűség kiszámítása
valoszinuseg = sikeres_esetek / szimulaciok_szama

# Idő és eredmény kiírása
print(f'A becsült valószínűség: {valoszinuseg}')
print(f'A szimuláció futási ideje: {futasi_ido:.4f} másodperc')

# 6. Grafikus megjelenítés
plt.figure(figsize=(10, 6))
plt.plot(range(1000, szimulaciok_szama + 1, 1000), eredmenyek, label='Becsült valószínűség')
plt.axhline(y=1 / 22, color='r', linestyle='--', label='Elméleti valószínűség: 1/22')
plt.xlabel('Szimulációk száma')
plt.ylabel('Valószínűség')
plt.title('Monte Carlo szimuláció eredményei')
plt.legend()
plt.grid(True)
plt.show()
