#  Advent of code day 1 problem 1
with open("inputD1P1.txt") as myfile:
    # read file and split lines into list
    reading = myfile.read()
    lines = reading.splitlines()
    # start a count for first and last digits in each line
    final_sum = 0
    # create lists of digits of each line, concatenate the first and last digits in those lists, add to final sum
    for each_line in lines:
        line_digits = []
        for char in each_line:
            if char.isdigit():
                line_digits.append(char)
        line_cat = line_digits[0] + line_digits[-1]
        final_sum += int(line_cat)
    print(f"Day 1, Problem 1 Answer: {final_sum}")

#  Advent of code day 1 problem 2
num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
with open("inputD1P1.txt") as myfile:
    # read file and split lines into list
    reading = myfile.read()
    lines = reading.splitlines()
    final_sum = 0
    # create lists of digits of each line, concatenate the first and last digits in those lists, add to final sum
    for each_line in lines:
        line_digits = []
        new_line = ""
        # replace spelled out numbers with digit
        for keys in num_dict:
            if keys in each_line:
                # only replace substring of spelled out number in case of runon, i.e. "eightwo"
                each_line = each_line.replace(keys, f"{keys[0]}{num_dict[keys]}{keys[-1]}")
        for char in each_line:
            if char.isdigit():
                line_digits.append(char)
        line_cat = line_digits[0] + line_digits[-1]
        final_sum += int(line_cat)
    print(f"Day 1, Problem 2 Answer: {final_sum}")


