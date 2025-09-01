"""
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
"""

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}



#defined a nested list
nested_list = ["A","B",["C","D"]]

print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(nested_list[2][0])
print(nested_list[2][1])


# defined a nested dictionary
trave_log = {
"France" :{
    "Cities Visited":  ["Paris","Liille", "Oijon"],
    "Times visited": 12
},

"Germany" :{
    "Cities Visited": ["Berlin", "Hamburg", "Stuttart"],
    "Times visited":7
}

}

print(trave_log["Germany"])
print(trave_log["Germany"]["Cities Visited"][2])


starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"]=7

print(final_dictionary)
print(starting_dictionary)


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])



