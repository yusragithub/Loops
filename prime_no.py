number = int(input("Enter your number: "))
flag = False 
if(number>1):
    for i in range(2, number):
        if(number % i) == 0:
            flag = True
            break

if(flag):
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
             
