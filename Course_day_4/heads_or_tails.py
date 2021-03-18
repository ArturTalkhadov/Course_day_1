import random

chois = int(input("Угадай- Орел или Решка нажми 1 если орел или 0 если думаешь что выпадет решка\n"))
pc_chois= random.randint(0,1)
if pc_chois==1 and chois==1:
    print(f"выпал орел вы угадали")
elif pc_chois==1 and chois==0:
    print(f"выпал орел вы не угадали")
elif pc_chois==0 and chois==0:
    print(f"выпала решка вы угадали")
else:
    print(f"выпала решка вы не угадали")
