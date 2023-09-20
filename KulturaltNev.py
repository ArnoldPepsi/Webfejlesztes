
szamok = [10, -3, 18, 23, 21]

pozitiv_szamok = []
negativ_szamok = []
nagyobb_mint_20_szamok = []

for szam in szamok:
    if szam > 0:
        pozitiv_szamok.append(szam)
    elif szam < 0:
        negativ_szamok.append(szam)

    if szam > 20:
        nagyobb_mint_20_szamok.append(szam)



print(f"Olyan számok, amik nagyobbak mint 20 ({len(nagyobb_mint_20_szamok)} db): {', '.join(map(str, nagyobb_mint_20_szamok))}")

for szam in szamok:
    print(f"Szám: {szam}")
    if szam > 0:
        print("Pozitív\n")
    elif szam < 0:
        print("Negatív\n")
    else:
        print("Nulla\n")
