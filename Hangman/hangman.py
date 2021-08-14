import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = list(string.ascii_uppercase)
    used_letters = []

    lives = 6

    stage1_1 = '    +---+'
    stage1_2 = '    |   |'
    stage1_3 = '        |'
    stage1_4 = '        |'
    stage1_5 = '        |'
    stage1_6 = '        |'
    stage1_7 = '========='
    stage1 = [stage1_1,stage1_2,stage1_3,stage1_4,stage1_5,stage1_6,stage1_7]

    stage2_1 = '    +---+'
    stage2_2 = '    |   |'
    stage2_3 = '    O   |'
    stage2_4 = '        |'
    stage2_5 = '        |'
    stage2_6 = '        |'
    stage2_7 = '========='
    stage2 = [stage2_1, stage2_2, stage2_3, stage2_4, stage2_5, stage2_6, stage2_7]

    stage3_1 = '    +---+'
    stage3_2 = '    |   |'
    stage3_3 = '    O   |'
    stage3_4 = '    |   |'
    stage3_5 = '        |'
    stage3_6 = '        |'
    stage3_7 = '========='
    stage3 = [stage3_1, stage3_2, stage3_3, stage3_4, stage3_5, stage3_6, stage3_7]

    stage4_1 = '    +---+'
    stage4_2 = '    |   |'
    stage4_3 = '    O   |'
    stage4_4 = '   /|   |'
    stage4_5 = '        |'
    stage4_6 = '        |'
    stage4_7 = '========='
    stage4 = [stage4_1, stage4_2, stage4_3, stage4_4, stage4_5, stage4_6, stage4_7]

    stage5_1 = '    +---+'
    stage5_2 = '    |   |'
    stage5_3 = '    O   |'
    stage5_4 = '   /|\  |'
    stage5_5 = '        |'
    stage5_6 = '        |'
    stage5_7 = '========='
    stage5 = [stage5_1, stage5_2, stage5_3, stage5_4, stage5_5, stage5_6, stage5_7]

    stage6_1 = '    +---+'
    stage6_2 = '    |   |'
    stage6_3 = '    O   |'
    stage6_4 = '   /|\  |'
    stage6_5 = '   /    |'
    stage6_6 = '        |'
    stage6_7 = '========='
    stage6 = [stage6_1, stage6_2, stage6_3, stage6_4, stage6_5, stage6_6, stage6_7]

    stage7_1 = '    +---+'
    stage7_2 = '    |   |'
    stage7_3 = '    O   |'
    stage7_4 = '   /|\  |'
    stage7_5 = '   / \  |'
    stage7_6 = '        |'
    stage7_7 = '========='
    stage7 = [stage7_1, stage7_2, stage7_3, stage7_4, stage7_5, stage7_6, stage7_7]

    while len(word_letters) > 0 and lives > 0:
        if lives == 6:
            print('\n'.join(stage1))
        elif lives == 5:
            print('\n'.join(stage2))
        elif lives == 4:
            print('\n'.join(stage3))
        elif lives == 3:
            print('\n'.join(stage4))
        elif lives == 2:
            print('\n'.join(stage5))
        elif lives == 1:
            print('\n'.join(stage6))

        for letter in alphabet:
            if letter in used_letters:
                alphabet.remove(letter)

        print('You have used these letters: ', ', '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', word_list)

        user_input = input('Guess a letter: ').upper()

        if user_input in alphabet:
            if user_input in word_letters:
                word_letters.remove(user_input)
                used_letters.append(user_input)
            else:
                lives = lives - 1
                used_letters.append(user_input)
                print('Letter not in word. Try again: ')
        elif user_input in used_letters:
            print('You already used that letter. Try again: ')
        else:
            print('Invalid character. Try again:')
        
    if lives == 0 and len(word_letters) > 0:
        print('\n'.join(stage7))
        print('You lost. The word was', word)
    elif lives > 0 and len(word_letters) == 0:
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', word_list)
        print('You won! The word was', word)
        
hangman()        