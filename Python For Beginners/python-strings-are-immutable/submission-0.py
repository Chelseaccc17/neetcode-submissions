def remove_fourth_character(word: str) -> str:
    part1=word[:3]
    part2=word[4:]
    new=part1+part2
    return new
    pass


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
