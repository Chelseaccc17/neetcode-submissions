from typing import List

def read_integers() -> List[int]:
    string = input()
    list_string =string.split(',')
    list_int=[]
    for string in list_string:
        list_int.append(int (string))
    return list_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
