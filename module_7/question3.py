import pyjokes

def  tell_some_jokes():
    inp = input("Do you want to hear a joke? (y/n) ")
    while inp == "y":
        print(pyjokes.get_joke())
        inp2 = input("Do you want to continue? (y/n) ")
        if inp2 == "n":
            break

tell_some_jokes()