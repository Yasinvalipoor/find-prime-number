def prime_number(x):
    prime = True
    for i in range(2,int(x/2)):
        if x%i==0 :
            prime = False  

    if prime:
        print ("it is prime ")

    else:
        print ("Your number is not Prime")


(prime_number(int(input("input your number to check !"))))



