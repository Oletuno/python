# create a python program that is able to determine whether a number enterred is an even or odd number
number = int(input("enter the number here"))
if number % 2 == 0:
    print("even number")
 else:
    print("the nuber is odd")   

    # create a python program that is able to determine whether a person can donate blood based on age and weight of a person.if the weight is greater than 50 kg and age is above 18,then the person can donate,else not possibler.

    age=int(input("enter age:")) 
    weight=float(input("enter your weight:"))

    if age >=18 and weight >50:
        print("can donate")
     else:
        print("not possible")   