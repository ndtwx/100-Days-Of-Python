#Nesting lists and dictionaries 
#is a matter of putting one inside the other

#Normal_Dictionary = {
#Key: Value, 
#Key2: Value2,
#}

#Putting list as a value instead of just string or number
#List_in_a_dictionary = {
#Key: [list],
#Key2: Value2,
#}

#Putting dictionary as a value instead of just string or number
#List_in_a_dictionary = {
#Key: [list],
#Key2: {Dict},
#}

#Nesting
capitals ={
    "France":"Paris",
    "Germany":"Berlin",

}

#Nesting a list in a Dictionary
travel_log = {
    "France":["Paris", "Lille", "Dijon"],
    "Germany":["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"],"total_visits": 100},
}

#Nesting a dictionary in a list
#A list with two dictionary, each dictionary has three key-value pairs and they all contain
#diffrent types of data (string, list and lastly number)

travel_log = [
    {"Country": "France", 
     "cities_visited":["Paris", "Lille", "Dijon"], 
     "total_visits": 12
    },
    {"Country":"Germany", 
     "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 100
    },
]


#Nesting a list in a list
["A", "B", ["C", "D"]]
#Not quite as useful as nesting a list in a dictionary 
#or a dictonary in a dictionary 
#because of the way that data is structured