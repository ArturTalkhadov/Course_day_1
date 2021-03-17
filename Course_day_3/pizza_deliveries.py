print("Добро пожаловать в PYTHON доставку пиццы")
size=input("Выберите размер пиццы: S, M, L ")
while size!="S" or "M" or "L":
    size=input("Выберите размер пиццы: S, M, L")
    if size=="S" or "M" or "L":
        break

add_pipperoni=input("Будете дополнительно пиперони? Y или N")
extra_cheese=input("Добавить больше сыра в пиццу? Y или N")
Small_Pizza=15
Medium_Pizza=20
Large_Pizza=25
Ps=2
Pml=3
Exch=1
final_bill=0

if size=="S":
    if add_pipperoni=="Y":
        if extra_cheese=="Y":
            print(f"Стоимость пиццы: {Small_Pizza+Ps+Exch}")
        else:
            print(f"Стоимость пиццы: {Small_Pizza+Ps}")
    elif extra_cheese=="Y":
        print(f"Стоимость пиццы: {Small_Pizza+Exch}")
    else:
        print(f"Стоимость пиццы: {Small_Pizza}")

elif size=="M":
    if add_pipperoni=="Y":
        if extra_cheese=="Y":
            print(f"Стоимость пиццы: {Medium_Pizza+Pml+Exch}")
        else:
            print(f"Стоимость пиццы: {Medium_Pizza+Pml}")
    elif extra_cheese=="Y":
        print(f"Стоимость пиццы: {Medium_Pizza+Exch}")
    else:
        print(f"Стоимость пиццы: {Medium_Pizza}")

else:
    if add_pipperoni=="Y":
        if extra_cheese=="Y":
            print(f"Стоимость пиццы: {Large_Pizza+Pml+Exch}")
        else:
            print(f"Стоимость пиццы: {Large_Pizza+Pml}")
    elif extra_cheese=="Y":
        print(f"Стоимость пиццы: {Large_Pizza+Exch}")
    else:
        print(f"Стоимость пиццы: {Large_Pizza}")
