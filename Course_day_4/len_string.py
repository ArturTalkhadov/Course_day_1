s=input("введите предложение в котором нужно найти самое длинное слово...\n")
slist=s.split(" ")
max_len=0
max_string=''
for i in slist:
    if len(i)>=max_len:
        max_len=len(i)
        max_string=i

print(f"самое длинное слово состоит из {max_len}, это слово: {max_string}")
