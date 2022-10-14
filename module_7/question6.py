def clean_string(text):
    clean_arr = [i for i in text if (ord(i)>=65 and ord(i)<=90) or (ord(i) >=97 and ord(i)<=122)]
    output = ('').join(clean_arr)
    return output
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)

