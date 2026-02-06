# a dictionary is a data type that stores data in terms of key-value pair.
# it is introduced by curly braces
# the valus stored in a dic can be of any data type
# to access values in a dic we use vthe keys


phonebook={
    "Benson" :"2546789456" ,
    "mary" : "2543567896" ,
    "jane" : "2543623125"
}

# showing the entire dictionmary
print(phonebook)
print(type(phonebook))

# print ya benson
print(phonebook["Benson"])



player={
    "name" : "messi" ,
    "age" : "36" ,
    "teams" : ["psg", "barca", "inter miami"],
    "more" :{
        "children" : "3",
        "residence" : "USA",
        "mobile no" : 1745364523, 4123456789, 1765432897
    }

}

# no of messi

print(player [more]["mobile no"] [1])

# print barca only

print(player["teams"][1])
      