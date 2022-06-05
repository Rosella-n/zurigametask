# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word,anagram):
    # [assignment] Add your code here
    word=input('Enter first_word:')
    anagram=input('Enter second_word:')

    first_string=word.lower()
    second_string=anagram.lower()


    if len(first_string)==len(second_string):
        str_1=sorted(first_string)
        str_2=sorted(second_string)
        if str_1 == str_2:
            print('True')
        else:
            print('False')
    else:
        print("Not equal number of letters")
    
    

find_anagram('','')
