def count_words_vowels(filename):
 vowels = "aeiouAEIOU"
 word_count = 0
 vowel_count = 0
 with open(filename, "r+") as f:
  f.seek(0)
  text = f.read()
  word_count = len(text.split())

 for ch in text:
   if ch in vowels:
    vowel_count += 1


 print("Number of words:", word_count)
 print("Number of vowels:", vowel_count)
 
 
 
 
count_words_vowels("file.txt") 
