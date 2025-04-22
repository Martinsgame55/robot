ovoce = {
    "název":"jablko",
    "cena":10,
    "fresh":True
}
print (ovoce["cena"])

KlicoveSlovo = input("Zadejte klíčové slovo")
hodnota = input("Zadejte hodnotu")

ovoce["obchod"] = "Lidl"

for polozky in ovoce:
    print(polozky)

for polozky2 in ovoce.items():
    print(polozky2)

for klicoveSlovo, hodnota in ovoce.items():
    print(f"{klicoveSlovo}:{hodnota}")
