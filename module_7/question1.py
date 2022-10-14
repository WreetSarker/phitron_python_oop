def create_string(lst):
    s = ""
    for idx, string in enumerate(lst):
        if idx != len(lst)-1:
            s += string
            s += " "
        else:
            s += string
            
    print(s)
    
create_string(["This", "is", "very", "fantastic"])
