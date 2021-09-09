#!/usr/bin/env python
# coding: utf-8

# In[4]:



from googletrans import Translator, LANGUAGES
#LANGUGAES is an in-built dictionary in googletrans with keys as codes and values as language names.

translator= Translator()

#Creating an empty list to store input sentences
input_sentences = [] 

print("ENTER TEXT:")

#Take multiline or single line input from user
while True:
    line = input()
    if(line):
        input_sentences.append(line)
    else:   #If line is empty, break loop
        break

heading= ['Language Code', 'Input Sentence']
format_text= '{:25}' *(len(heading)+1)

print('\n',('Language Name', *heading), '\n', '='*120)

for data in input_sentences:
    wordlist = data.split()
    for word in wordlist:
        detection= translator.detect(word)
        sentence= [LANGUAGES.get(detection.lang).title(), detection.lang, word]
        print(format_text.format(*sentence))


# In[ ]:





# In[ ]:




