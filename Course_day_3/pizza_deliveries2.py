print("Добро пожаловать в PYTHON доставку пиццы ")
size=input("Выберите размер пиццы: S, M, L ")
add_pipperoni=input("Будете дополнительно пиперони? Y или N ")
extra_cheese=input("Добавить больше сыра в пиццу? Y или N ")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25

if add_pipperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+3

if extra_cheese=="Y":
    bill+=1

print(f"Стоимость вашей пиццы равна:$ {bill} ")
