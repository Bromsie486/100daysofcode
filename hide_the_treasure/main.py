line1 = ["-", "-", "-"]
line2 = ["-", "-", "-"]
line3 = ["-", "-", "-"]
map = [line1, line2, line3]

treasure_spot = input("Where do you want to hide the treasure? (A1-C3)")
letter = treasure_spot[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(treasure_spot[1]) - 1

map[number_index][letter_index] = "X"
print("\n", line1, "\n", line2, "\n", line3)
