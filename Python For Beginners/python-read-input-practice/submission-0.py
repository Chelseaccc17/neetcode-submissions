def add_two_numbers() -> int:
#first convert the string into int and then get them into a list and then use sum function to get the sum
    string= input()
    list_string = string.split(",")
    list_int= []
    for string in list_string:
        list_int.append(int(string))
    list_sum= sum(list_int)
    return list_sum





# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
