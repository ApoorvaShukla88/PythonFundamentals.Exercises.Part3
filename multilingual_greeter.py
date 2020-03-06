

#exercise 3 part 3
language = ""


def greet(name):
    print(name)



def name_input():
    name = input("Enter the name\n")
    return name


#name_input()

def language_input():
    choose_language = input(str("Choose from three lanugage HINDI, ENGLISH, SPANISH "))
    name = name_input()
    if choose_language == "HINDI":
        print("Namste " + name)
    elif choose_language == "ENGLISH":
        print("Hello " + name)
    elif choose_language == "SPANISH":
        print("Oye " + name)
    else:
        print("")


language_input()


