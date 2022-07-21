# personal task organizer using lists and conditional statements
mylist = ['read a chapter of Python by Eric Matthes', 'return amazon package', 'find a new recipe']
# program loops 6 times
for task in range(0, 6):
    myChoice = input("I have a list of things to address. What do I want to do? "
                     "\n\t(A)Look at list of things to do (B)Sleep til problems go away (C)Add more to list :")
    if myChoice == "A":
        print(f"{mylist} \nLet's do the last task first:")
        print(f"{mylist[-1]} ...Done\n")
        del mylist[-1]
    elif myChoice == "B":
        print("\nEnjoy a blissful nap!...Zzz...\n")
    elif myChoice == "C":
        moreThings = input("Add to list..")
        mylist.append(moreThings)
    else:
        print("\nchoice not valid...end of world...Boom!\n")
        exit()