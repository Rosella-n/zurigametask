# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
   open_file=open("./story.txt","r")
   read_text=open_file.read()
   return read_text


read_file_content("./story.txt")



import string
def count_words():
    text = read_file_content("./story.txt")
  
    # [assignment] Add your code here
    dictionary = dict()
    words = text.split(" ")
    for word in words:
        if word in dictionary:
                dictionary[word] = dictionary[word] + 1
        else:
                dictionary[word] = 1

    for key in list(dictionary.keys()):
        print(key, ":", dictionary[key])
   

count_words()
