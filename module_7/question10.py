import re

def create_new_string(a, s):
    new_str = ""
    split_str = re.split('; |, | ', s)
    split_sent = re.split('. ', s)
    for word in a:
        for j in range(len(split_str)):
            if word.lower() == split_str[j].lower():
                new_str += split_str[j+1]
                new_str += " "
                j+=1
    with open('out.txt', 'w') as f:
        f.write(new_str)

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


create_new_string(a, s)