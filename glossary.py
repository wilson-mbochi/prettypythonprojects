# dictionary of glossary words
pythonConcepts = {'variables': 'assign data/values to a keyword',
                      'for loops': 'loop through a list, items or range of values and perform actions for duration specified',
                      'conditionals': 'use boolean operators, if, elif, and else cases to test for true or false then perform actions',
                      'dictionaries': 'store data/values to key-value pairs'}
for k, v in pythonConcepts.items():
    print(f"{k.upper()}")
userRequest = input("\nSearch a concept above in the glossary for the definition: ").lower()
for item in pythonConcepts.keys():
    if item in userRequest:
        print(f"\t{item.upper()}: {pythonConcepts[item].lower()}")
else: print("sorry, not found!")
