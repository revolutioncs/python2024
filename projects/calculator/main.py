def calculater(x,y):
    print('''1.avg
2.sum
3.subtract
4.divide
5.multiply
0.exit''')
    choice=int(input("enter a number: "))
    if choice==1:
        avg=(x+y)/2
        print("average is: ",avg)
    elif choice==2:
        sum=x+y
        print("sum is: ",sum)
    elif choice==3:
        subtract=x-y
        print("subtract is: ",subtract)
    elif choice==4:
        divide=x/y
        print("divide is: ",divide)
    elif choice==5:
        multiply=x*y
        print("multiply is: ",multiply)
    else:
        print("Error, please enter a number mentioned above")

c=int(input("enter a number: "))
d=int(input("enter another number: "))
calculater(c,d)