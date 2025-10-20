import random
import os
import time
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def analyzing_calculating():
    user_choice = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ], k=2)
    computer_choice = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ], k=2)
    while True:
        if sum(computer_choice) <17:
            another_computer_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ])
            computer_choice.append(another_computer_choice)
        else:
            break

    while True:

        if  1 in user_choice:
           if sum(user_choice) <=10:
              index=user_choice.index(1)
              user_choice.remove(1)
              user_choice.insert(index,11)

        if 1 in computer_choice:
           if sum(computer_choice)<=10:
               index = computer_choice.index(1)
               computer_choice.remove(1)
               computer_choice.insert(index, 11)

        print(f'your cards are {user_choice} current score is {sum(user_choice)} ')
        print(f"computer first's card is {computer_choice[0]}")


        if input("Get another card ? y/n").lower() == 'y':
            another_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ])
            user_choice.append(another_choice)
            clear()
        else:
            break
    print(f'Your final hand : {user_choice} with score{sum(user_choice)} ')
    print(f'Computer final hand: {computer_choice} with score {sum(computer_choice)} ')
    if sum(user_choice)<=21 and sum(computer_choice)<=21:
        if sum(user_choice)==sum(computer_choice):
            print('You Draw')
        elif sum(computer_choice)>sum(user_choice):
            print('You lose')
        elif sum(computer_choice)<sum(user_choice):
            print('You win')
    elif sum(user_choice)>21 and sum(computer_choice)>21:
       print('You both went over 21')
    elif sum(computer_choice)<21 or  sum(user_choice)>21 :
        print('You lose because you went over 21')
    elif  sum(computer_choice)>21 or  sum(user_choice)<21:
        print('You win,Computer went over 21')




def black_jack():
   to_games= True
   while True:
      clear()
      while True:
          choice = input('Choose a game to start\n1.Foggy\n2.Twenty one\n3.Snake\n').lower()
          if choice=='2' or choice=='twenty one':
              break
      print('Starting Game...')
      time.sleep(2)
      if to_games:
          to_game = r'''88          88                       88        88                       88         
                   88          88                       88        ""                       88         
                   88          88                       88                                 88         
                   88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
                   88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
                   88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
                   88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
                   8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                                 ,88                                  
                                                               888P"                                  '''
          print(to_game)
          to_games=False
      analyzing_calculating()
      retry=input('Do you want to play again y/n') .lower()
      if retry!='y':
          break
black_jack()