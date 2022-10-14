def replace_comma_with_space(text):
    clean_arr = s.split(',')
    output = (' ').join(clean_arr)

    return output
s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
