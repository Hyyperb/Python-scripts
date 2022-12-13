from english_words import english_words_set as words
from string import ascii_lowercase as letters

words = list(words)
letters = list(letters)

count = {}
prcnt = {}

for i in range(26):
    count[i] = 0
    prcnt[i] = 0

for word in words:
    for letter in letters:
        if(word[0]==letter):
            count[letters.index(letter)] += 1

sorted_count = {k:v for k,v in  sorted(count.items(),key = lambda item:item[1])}

for letter in sorted_count:
	pass
    #print(str(count[letter]/len(words)*100)[0:4],letters[letter],count[letter])
    
print(sorted_count)
