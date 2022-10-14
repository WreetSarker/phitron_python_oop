def create_list(dic):
    lst = []
    for item in dic.items():
        lst.extend(item)
    print(lst)

create_list({'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6})