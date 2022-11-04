info = ""
with open("Books.txt", "r") as file:
    info = file.read()

file.close()
info_sents = info.split("--")


i = 0
print(info_sents[i])
i+=1
inp = input("[enter - read more, press q to quit]: ")
while inp != 'q' and i < len(info_sents):
    print(info_sents[i])
    i+= 1
    inp = input("[enter - read more, press q to quit]: ")