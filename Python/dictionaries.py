import pprint
Rohith = {
    "name": {"first_name":'Rohith', 
            "last_name": 'Sharma'},
    "age": 38, 
    "city": 'Mumbai',
    123: ['Batting','Fielding'],
    }



 

# Rohith["name"]["first_name"] = "R"


print(Rohith.items())



[
    ['first_name', 'Rohith'],
    ('last_name', 'Sharma'), 
    ('age', 38), 
    ('city', 'Mumbai'), 
    ('skills', ['Batting', 'Fielding'])]