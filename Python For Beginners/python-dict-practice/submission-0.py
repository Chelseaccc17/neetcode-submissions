from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count= {}
    #take string return dictionary with count of each character in the sting
    for char in word:
    #for every charater in the word
        if char not in count:
            # if the character has ever been seen initiate to 0
            count[char]=0
        count[char]= count[char] +1 
        #else make that count of the char +1 
    return count 
    pass




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
