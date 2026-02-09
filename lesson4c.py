# a for loop can also be used to iterate through a turple,stringor dictionary

name = "Marcus"

for letter in name:
    print(letter)

for letter in name:
    if letter == "c" :
        print("the letter is c")  
    else:
         print(letter) 

# below is a list of counties
counties = ["Nairobi"] 

player = {
    "name":"mbappe",
    "age" :"26",
    "country":"kenyan"
    
    }
 
 for key in player:
    print(key)


for value in player:
    print(player[value])    
    # print player name

 for team in player["teams"]  
    print(team)