info = ""
with open("Books.txt", "r") as file:
    info = file.read()

file.close()
info_sents = info.split("--")


i = 0
print(info_sents[i])

inp = input("[enter - read more, press q to quit]: ")
try:
    int_inp = int(inp)
    if i+int_inp < len(info_sents):
        i+=int_inp
    else:
        i+= 1
except:
    i+=1
while inp != 'q' and i < len(info_sents):
    
    print(info_sents[i])
    inp = input("[enter - read more, press q to quit]: ")
    try:
        int_inp = int(inp)
        if i+int_inp < len(info_sents) and i+int_inp >=0:
            i+=int_inp
        else:
            i+= 1
    except:
        i+=1
    