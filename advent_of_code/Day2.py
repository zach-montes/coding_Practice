# example_list = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

#  Advent of code day 2 problem 1
with open("inputDay2.txt") as myfile:
    # read file and split lines into list
    reading = myfile.read()
    lines = reading.splitlines()
    cubes_key = {"red": 12, "green": 13, "blue": 14}

    count = 0
    # split each game into a list
    for i in lines:
        # mostly for error checking, each game has a True/False bool for if it is possible
        possible_dict = {i: True}

        game = i.split(": ")
        game_num_list = game[0].split(" ")
        game_num = game_num_list[1]

        hand = game[1].split("; ")
        # continue to split each game into separate cube draws
        # check each cube draw and its color to the cubes_key
        # if the cube draw is greater than the key draw, change possible flag to false
        for each in hand:
            cubes = each.split(", ")

            for draw in cubes:
                draw_list = draw.split(" ")
                comp_color = draw_list[1]
                comp_num = int(draw_list[0])

                for color in cubes_key.keys():
                    if color == comp_color:
                        if comp_num > cubes_key[color]:
                            possible_dict[i] = False

        # after checking each cube draw in a game, if bool is still True, add to final sum
        if possible_dict[i]:
            count += int(game_num)

    print(f"Final sum for problem 1 is {count}")

#  Advent of code day 2 problem 1
with open("inputDay2.txt") as myfile:
    # read file and split lines into list
    reading = myfile.read()
    lines = reading.splitlines()
    cubes_key = {"red": 12, "green": 13, "blue": 14}
    count = 0
    # split each game into a list
    for i in lines:
        possible_dict = {"red": [], "green": [], "blue": []}
        # add each cube draw in a game into a dictionary value to its corresponding color
        game = i.split(": ")
        hand = game[1].split("; ")
        for each in hand:
            cubes = each.split(", ")
            for draw in cubes:
                draw_list = draw.split(" ")
                comp_color = draw_list[1]
                comp_num = int(draw_list[0])
                for key_color in possible_dict.keys():
                    if comp_color == key_color:
                        possible_dict[key_color].append(comp_num)

        # find the largest number for each color, multiply them to find the set
        game_set = 1
        for each_color in possible_dict.keys():
            largest_num = max(possible_dict[each_color])
            game_set *= largest_num

        count += game_set

print(f"Final sum for problem 2 is {count}")
