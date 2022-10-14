def replace_word(s, replace_with):
    
    pos_words = [replace_with[i] for i in range(len(replace_with)) if i%2==0]
    neg_words = [replace_with[i] for i in range(len(replace_with)) if i%2==1]

    split_words = s.split(' ')
    for idx, word in enumerate(split_words):
        if word in pos_words:
            i = pos_words.index(word)
            split_words[idx] = neg_words[i]
    print((' ').join(split_words))

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
replace_word(s, replace_with)