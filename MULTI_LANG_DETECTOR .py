#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#06-09-2021
#Chandan M


from googletrans import Translator, LANGUAGES
from langdetect import detect

translator= Translator()


input_sentences = [] 

print("ENTER TEXT:")

#Take multiline or single line input from user

while True:
    line = input()
    if(line):
        input_sentences.append(line)
    else:   #If line is empty, break loop
        break

lemmatizer_names= ['Language Code', 'Input Sentence']
format_text= '{:24}' *(len(lemmatizer_names)+1)


print ( format_text.format("Language Name", *lemmatizer_names),'\n','='*120)
for data in input_sentences:
    wordlist = data.split()
    for word in wordlist:
        detection= translator.detect(word)
        sentence= [LANGUAGES.get(detection.lang).title(), detection.lang, word]
        print(format_text.format(*sentence))
        


# In[ ]:




