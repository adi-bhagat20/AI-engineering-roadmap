'''
    store the document into this string
'''

text = "" 
with open("text.txt", "r") as file:
    content = file.read()
    text += content
    # print(content)
print(text)
print("-"*100)

'''
    converting to lower case
'''

text = text.lower()

'''
    strip punctuations
'''

import string

clean_text = "".join(char for char in text if char not in string.punctuation)
print(clean_text)
print("-"*100)

'''
    split into words
'''

lst = clean_text.split()
print(lst)
print("-"*100)
# print(len(lst))

'''
    remove stopwords
'''

stopwords = ['am' , 'is' , 'are' , 'was' , 'were' , 'the' , 'a' , 'an' , 'and' , 'in']
lst = [word for word in lst if word not in stopwords]

'''
    count word frequencies
'''

count = {}
for word in lst:
    count[word] = count.get(word , 0) + 1
print(count)
print("-"*100)
# print(len(count))

'''
    top 10 most frequent values
'''

top_10 = sorted(count , key=count.get , reverse=True)[:10]
for word in top_10:
    print(f"{word} : {count[word]}")
print('-'*100)

'''
    make a new file and store everything in key value pair
'''

file_name = input("Enter the name of the file to write word count- ")
with open(f"{file_name}.txt" , 'w') as new_file:
    for word , c in count.items():
        new_file.write(f"{word} : {c} \n")

