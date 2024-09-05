# dictionary of glossary words
pythonConcepts = {'conditionals': 'use boolean operators, if, elif, and else cases to test for true or false then perform actions',
                  'dictionaries': 'store data/values to key-value pairs',
                  'for loops': 'loop through a list, items or range of values and perform actions for duration specified',
                  'variables': 'assign data/values to a keyword'}
for k, v in pythonConcepts.items():
    print(f"{k.upper()}")
userRequest = input("\nSearch a concept above in the glossary for the definition: ").lower()
for item in pythonConcepts.keys():
    if item in userRequest:
        print(f"\t{item.upper()}: {pythonConcepts[item].lower()}")
        break
else:
    print("sorry, not found!")
