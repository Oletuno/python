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

print(=======================)

player={
    "name" : "messi" ,
    "age" : "36" ,
    "teams" : ["psg", "barca", "inter miami"]
}

# print barca only

print(player["teams"][1])
      