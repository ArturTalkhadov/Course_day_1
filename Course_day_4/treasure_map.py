row1 = ["a","a","a"]
row2 = ["a","a","a"]
row3 = ["a","a","a"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#we get the indices from the entered string
first_index=int(position)//10
last_index=int(position)%10

map[last_index-1][first_index-1]="X"

print(f"{row1}\n{row2}\n{row3}")
