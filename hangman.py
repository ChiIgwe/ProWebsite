import random


def hangman(word_list, guessed_letter, length_of_word, strikes):
    if guessed_letter in random_word:

        for i in range(len(random_word)):
            if random_word[i] == guessed_letter:
                length_of_word = length_of_word[:i] + guessed_letter + length_of_word[i + 1:]
    if not guessed_letter.islower() or len(guessed_letter) != 1:
        print("Invalid input. Please enter a lowercase letter.")
        return length_of_word, strikes
    elif guessed_letter not in random_word:
        strikes += 1
        print(f"This letter is not present in the word. This is strike {strikes}/{MAX_STRIKES}")

    return length_of_word, strikes


word_list = {

    1: 'Apple',
    2: 'Banana',
    3: 'Carrot',
    4: 'Dog',
    5: 'Elephant',
    6: 'Frog',
    7: 'Giraffe',
    8: 'Hippopotamus',
    9: 'Ice cream',
    10: 'Jellyfish',
    11: 'Kangaroo',
    12: 'Lion',
    13: 'Monkey',
    14: 'Narwhal',
    15: 'Octopus',
    16: 'Penguin',
    17: 'Quokka',
    18: 'Rabbit',
    19: 'Strawberry',
    20: 'Tiger',
    21: 'Unicorn',
    22: 'Violin',
    23: 'Watermelon',
    24: 'Xylophone',
    25: 'Yak',
    26: 'Zebra',
    27: 'Pizza',
    28: 'Guitar',
    29: 'Butterfly',
    30: 'Dolphin',
    31: 'Rainbow',
    32: 'Dragon',
    33: 'Robot',
    34: 'Fireworks',
    35: 'Moon',
    36: 'Sunflower',
    37: 'Starfish',
    38: 'Cactus',
    39: 'Football',
    40: 'Baseball',
    41: 'Basketball',
    42: 'Soccer',
    43: 'Volleyball',
    44: 'Tennis',
    45: 'Golf',
    46: 'Swimming',
    47: 'Hiking',
    48: 'Cycling',
    49: 'Cooking',
    50: 'Reading',
    51: 'Chinedu',
    52: 'Ezinne',
    53: 'Michael'
}
# List of words
word_list = [word.lower() for word in word_list.values()]

# Maximum number of strikes
MAX_STRIKES = 4

strikes = 0

# Select a random word
random_word = random.choice(word_list)

# Initialize the game state
counter = len(random_word)
length_of_word = '_ ' * counter
while length_of_word != random_word and strikes < MAX_STRIKES:
    guessed_letter = input("What letter will you choose: ")
    length_of_word, strikes = hangman(word_list, guessed_letter, length_of_word, strikes)
    print(length_of_word)
# Prompt the player for a letter
print(length_of_word)
if length_of_word == random_word:
    print("Congratulations you have beat this game!!")
if strikes == MAX_STRIKES:
    print("GAME OVER")
    print(f"{random_word}")

# Call the hangman function
hangman(word_list, guessed_letter, length_of_word, strikes)