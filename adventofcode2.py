# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:58:24 2022

@author: Nicklas Branding
"""

"""
first part of day 2
"""       

input_list = list(map(str, input("Enter multiple weights: ").split()))
print(input_list)
player1 = []
player2 = []

for i, val in enumerate(input_list):
    print(i,val)
    if i%2==0:
        player1.append(val)
    else:
        player2.append(val)
print(player1)
print(player2)

zipped = zip(player1,player2)
zipped_list = list(zipped)
print(zipped_list)
"""
PART 1 converter
"""
convert_C_to_SCISSOR = [tuple(map(lambda i: str.replace(i, "C","SCISSOR"), tup)) for tup in zipped_list]
convert_A_to_ROCK = [tuple(map(lambda i: str.replace(i, "A","ROCK"), tup)) for tup in convert_C_to_SCISSOR]
convert_B_to_PAPPER = [tuple(map(lambda i: str.replace(i, "B","PAPPER"), tup)) for tup in convert_A_to_ROCK]
convert_X_to_ROCK = [tuple(map(lambda i: str.replace(i, "X","ROCK"), tup)) for tup in convert_B_to_PAPPER]
convert_Y_to_PAPPER = [tuple(map(lambda i: str.replace(i, "Y","PAPPER"), tup)) for tup in convert_X_to_ROCK]
convert_Z_to_SCISSOR = [tuple(map(lambda i: str.replace(i, "Z","SCISSOR"), tup)) for tup in convert_Y_to_PAPPER]
converted_list = convert_Z_to_SCISSOR
"""
PART 2 converter
"""
convert_CC_to_SCISSOR = [tuple(map(lambda i: str.replace(i, "C","SCISSOR"), tup)) for tup in zipped_list]
convert_AA_to_ROCK = [tuple(map(lambda i: str.replace(i, "A","ROCK"), tup)) for tup in convert_CC_to_SCISSOR]
convert_BB_to_PAPPER = [tuple(map(lambda i: str.replace(i, "B","PAPPER"), tup)) for tup in convert_AA_to_ROCK]
convert_X_to_LOSS = [tuple(map(lambda i: str.replace(i, "X","LOSS"), tup)) for tup in convert_BB_to_PAPPER]
convert_Y_to_DRAW = [tuple(map(lambda i: str.replace(i, "Y","DRAW"), tup)) for tup in convert_X_to_LOSS]
convert_Z_to_WIN = [tuple(map(lambda i: str.replace(i, "Z","WIN"), tup)) for tup in convert_Y_to_DRAW]
converted_list_part2 = convert_Z_to_WIN

print(converted_list)
points_part1 = 0
points_part2 = 0
dict_points1 = {"ROCK": 1, "SCISSOR": 3, "PAPPER": 2, "WIN": 6, "LOSS": 0, "DRAW": 3}


for opp, me in converted_list:
    if opp == 'PAPPER' and me == 'PAPPER':
        points_part1 += dict_points1["DRAW"] + dict_points1["PAPPER"]
        print("opponent choose: ", opp)
        print("I choose: ", me)     
    elif opp == 'PAPPER' and me == 'SCISSOR':
        points_part1 += dict_points1["WIN"] + dict_points1["SCISSOR"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'PAPPER' and me == 'ROCK':
        points_part1 += dict_points1["LOSS"] + dict_points1["ROCK"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
        
    elif opp == 'SCISSOR' and me == 'SCISSOR':
        points_part1 += dict_points1["DRAW"] + dict_points1["SCISSOR"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'SCISSOR' and me == 'ROCK':
        points_part1 += dict_points1["WIN"] + dict_points1["ROCK"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'SCISSOR' and me == 'PAPPER':
        points_part1 += dict_points1["LOSS"] + dict_points1["PAPPER"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
        
    elif opp == 'ROCK' and me == 'ROCK':
        points_part1 += dict_points1["DRAW"] + dict_points1["ROCK"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'ROCK' and me == 'SCISSOR':
        points_part1 += dict_points1["LOSS"] + dict_points1["SCISSOR"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'ROCK' and me == 'PAPPER':
        points_part1 += dict_points1["WIN"] + dict_points1["PAPPER"]
        print("opponent choose: ", opp)
        print("I choose: ", me)

for opp, me in converted_list_part2:
    if opp == 'PAPPER' and me == 'WIN':
        points_part2 += dict_points1["WIN"] + dict_points1["SCISSOR"]
        print("opponent choose: ", opp)
        print("I choose: ", me)     
    elif opp == 'PAPPER' and me == 'LOSS':
        points_part2 += dict_points1["LOSS"] + dict_points1["ROCK"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'PAPPER' and me == 'DRAW':
        points_part2 += dict_points1["DRAW"] + dict_points1["PAPPER"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
        
    elif opp == 'SCISSOR' and me == 'WIN':
        points_part2 += dict_points1["WIN"] + dict_points1["ROCK"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'SCISSOR' and me == 'LOSS':
        points_part2 += dict_points1["LOSS"] + dict_points1["PAPPER"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'SCISSOR' and me == 'DRAW':
        points_part2 += dict_points1["DRAW"] + dict_points1["SCISSOR"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
        
    elif opp == 'ROCK' and me == 'WIN':
        points_part2 += dict_points1["WIN"] + dict_points1["PAPPER"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'ROCK' and me == 'LOSS':
        points_part2 += dict_points1["LOSS"] + dict_points1["SCISSOR"]
        print("opponent choose: ", opp)
        print("I choose: ", me)
    elif opp == 'ROCK' and me == 'DRAW':
        points_part2 += dict_points1["DRAW"] + dict_points1["ROCK"]
        print("opponent choose: ", opp)
        print("I choose: ", me)

print(points_part1)   
print(points_part2)   