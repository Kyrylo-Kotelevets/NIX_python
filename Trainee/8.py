"""
создайте файл с таким содержанием:
\"""
    some line blablabla you dont need to catch this line try to catch me but not me I'm here, catch me!!!
\"""
откройте данный файл при помощи контекстного менеджера в режиме чтения и соберите список всех строк,
которые содержат текст "catch me" в один список после чего выведите в консоль количество найденных в файле строк
"""

text = """some line blablabla
you dont need to catch this line
try to catch me
but not me
I'm here, catch me!!!"""

with open("input.txt", "wt") as input_file:
    input_file.write(text)

with open("input.txt", "rt") as input_file:
    cached_lines = [line for line in input_file if "catch me" in line]
    print(cached_lines)
