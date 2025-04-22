robot = {
    "Pepa":"Kuchař",
    "Filip":"Autopilot"
    }
dalsiRobot = input("Zadejte jméno robota: ")
if dalsiRobot == robot:
    print(robot)
    for polozky in robot:
    print(polozky)

for polozky2 in robot.items():
    print(polozky2)

for klicoveSlovo, hodnota in robot.items():
    print(f"{klicoveSlovo}:{hodnota}")
