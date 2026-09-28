import random
#import hangman_words.word_list
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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
placeholder = ""

i=0
for i in range(len(chosen_word)):
    placeholder += "_"
    i+=1
print("Word to guess: " + placeholder)

lives = 6
correct_letters = []

while placeholder.count("_")!=0 and lives>-1:
    guess = input("Guess a letter: ").lower()
    placeholder = list(placeholder)

    if guess in correct_letters:
        print("You have already guessed " + guess + ".")

    j=0
    for j in range(len(chosen_word)):
        if list(chosen_word)[j]==guess:
             placeholder[j] = guess
             correct_letters.append(guess)
    print("".join(placeholder))
    if guess not in list(placeholder):
        print("You guessed " + guess + ", that's not in the word. You lose a life.")
        print(stages[lives])
        lives-=1
        if lives>-1:
            print("*******************"+str(lives)+"/6 LIVES LEFT*******************")
    if lives ==-1:
        print("*******************IT WAS "+chosen_word+"! YOU LOSE!*******************")
    

if "_" not in placeholder:
    print("*******************YOU WIN! CONGRATULATIONS!*******************")

