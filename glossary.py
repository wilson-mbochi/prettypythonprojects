# dictionary of glossary words
pythonConcepts = {'variables': 'assign data/values to a keyword',
                      'for loops': 'loop through a list, items or range of values and perform actions for duration specified',
                      'conditionals': 'use boolean operators, if, elif, and else cases to test for true or false then perform actions',
                      'dictionaries': 'store data/values to key-value pairs'}
for k, v in pythonConcepts.items():
    print(f"{k.upper()} - {v.lower()}")
userRequest = input("search a concept in glossary: ")
for item in pythonConcepts.keys():
    if item in userRequest:
        print(f"\t\t{item.title()}: {pythonConcepts[item].upper()}")
