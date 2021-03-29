def prime_checker(number):
    # эта функция проверяет является ли ввелденное число простым
    
    if number in (2,3):
        print("It's a prime number ")
    elif (number%2==0) or (number%3==0):
        print("It's not a prime number ")
    else:
        print("It's a prime number ")


n = int(input("Check this number:(введенное число должно быть больше 1...) "))
prime_checker(number=n)
