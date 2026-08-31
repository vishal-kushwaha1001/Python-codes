sentence = "hii i am vishal kumar kushwaha"
words = sentence.split()
rev_words = []
for word in words:
    rev_word = word[: :-1]
    rev_words.append(rev_word)

rev_sentence = " ".join(rev_words)    
print(rev_sentence)