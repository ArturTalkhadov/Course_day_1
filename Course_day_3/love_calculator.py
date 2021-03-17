print("Добро пожаловать в LOVE калькулятор!")
name1=input("Напиши свое имя... \n").lower()
name2=input("Напиши имя твое/й(го) возлюбленн/ой(ого)...\n ").lower()

tl="true"
lo="love"
total_name=name1+name2
sum_name1=0
sum_name2=0

for words in tl:
    sum_name1+=total_name.count(words)

for words in lo:
    sum_name2+=total_name.count(words)

total=int(str(sum_name1)+str(sum_name2))

if total<10 or total>90:
    print(f"Ваш результат теста:{total} балла, вы совместимы как ментос и кола")
elif 40<=total<=50:
    print(f"Ваш результат теста:{total} балла, вам будет хорошо вместе")
else:
    print(f"Ваш результат теста:{total} балла, при желании все получится")
