# ROCK,PAPER,SCISSOR-GAME

import random

user_wins = 0 
cpt_wins = 0
match_draw = 0

opt = ["ROCK" , "PAPER" , "SCISSOR"]

while True:
    user_input= input('Type \nRock \nPaper \nScissor \nQ to Quit: ').upper()
    if user_input == 'Q':
        break
    
    if user_input not in opt:
        print('---Please select a valid input---')
        continue
    
    random_number = random.randint(0,2)
    # rock: 0  paper: 1  scissor: 2
    
    cpt_input = opt[random_number]
    print('Computer picked',cpt_input)
    
    if user_input == 'ROCK' and cpt_input == "SCISSOR":
        print('You won!')
        user_wins += 1
        continue
    if user_input == 'ROCK' and cpt_input == "PAPER":
        print('You won!')
        user_wins += 1
        continue
    if user_input == 'PAPER' and cpt_input == "SCISSOR":
        print('Yoy lost!')
        cpt_wins += 1
        continue
    if user_input == 'PAPER' and cpt_input == "ROCK":
        print('You lost!')
        cpt_wins += 1
        continue
    if user_input == 'SCISSOR' and cpt_input == "ROCK":
        print('You lost!')
        cpt_wins += 1
        continue
    if user_input == 'SCISSOR' and cpt_input == "PAPER":
        print('You won!')
        user_wins += 1
        continue
    if user_input == 'PAPER' and cpt_input == "PAPER":
        print('--Match Draw--')
        match_draw += 1
        continue
    if user_input == 'ROCK' and cpt_input == "ROCK":
        print('--Match Draw--')
        match_draw += 1
        continue
    if user_input == 'SCISSOR' and cpt_input == "SCISSOR":
        print('--Match Draw--')
        match_draw += 1
        continue
     # You can use 'elif' in place of 'continue' and 'if'
       
print('\tYou won', user_wins ,'times')    
print('\tComputer won', cpt_wins ,'times')
print('\tMatches Drawn', match_draw)
print('Thank You \nGoodbye!')