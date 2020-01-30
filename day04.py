# writing to files
f = open("myFile.txt", "r+")
# clinder = '''clinder clinder clinder clinder clinder clinder clinder clinder clinder clinder 
#             clinder clinder clinder clinder clinder clinder 
#             clinder clinder clinder clinder 
#             clinder'''
# f.write(clinder)
c = f.readlines()
f.close()
# print(c)


# reading from files


# dictionaries
myDictionary = {
            "name" : "Arnab",
            "surname" : "Bose",
            "Semester" : 4,
            "Marital Status" : False,
            "prefferedSubjects" : ["Compositing", "Time Passing"],
            "Outfit" : {
                "shirt": "T-shirt",
                "Pants": (3,56,123)
                        }
            }

import json

print(json.dumps(myDictionary))

k = open("m.json", "w")
k.write(json.dumps(myDictionary))
k.close()
# exporting dictionaries to json

# basic classes
# examples with import nuke
