

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

lives=6
#  empty List  display.

display=[]
for _ in chosen_word:
    display+="_"

print(display)


end_of_game= False
while not end_of_game:
    guess = input("Guess a letter: ").lower();

    for position in range(len(chosen_word)):

        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1;
        print(stages[lives])
        if lives==0:
            
            end_of_game=True
            print("You lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win")


    

