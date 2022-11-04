# anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']) 
# [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]


def find_freq(s):
    dic = {}
    for char in s:
        if dic.get(char) is None:
            dic[char] = 1
        else:
            dic[char]+=1

    return dic

def anagrams(ls):
    result = {}
    matches = []
    for word in ls:
        result[word] = []
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            # print(ls[i], ls[j], end="*****\n")
            if find_freq(ls[i]) == find_freq(ls[j]):
                if j not in matches:
                    result[ls[i]].append(ls[j])
                    matches.append(j)
    
    final = dict(result)
    for key in result.keys():
        for value in result.values():
            if key in value:
                del final[key]


    out = [[] for i in final.keys()]

    for idx, key in enumerate(final.keys()):
        out[idx].append(key)
        out[idx].extend(final[key])

    return out

print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))