import random
from words import word_list

list_of_words = ["tree", "string","comma","computer","cat","dog","internet","rocket","space","train"]
max_lives = 1
lives = 1



while True:
    difficulty = input("what difficulty you want chose from 1 to 3 (1-easy, 3-hard): ")
    if difficulty == "1":
        max_lives = 7
        lives = 7
        break
    elif difficulty == "2":
        max_lives = 5
        lives = 5
        break
    elif difficulty == "3":
        max_lives = 2
        lives = 2
        break
    else:
        print("please enter exactly 1, 2 or 3")


word = random.choice(list_of_words)

plan = "_ " * len(word)

while True:
    if lives == 0:
        print("that is your end!! But you can try it again.") 
        break
    elif "_" not in plan:
        print(f"\n{plan}\ncongrats you made it\n")
        break
    else:
        print(f"\nyou have {lives} of {max_lives} lives")
        guess = input(f"this is your word: {plan}.\nNow you can write you guess: ").lower()
        if guess in word:
            positions = [pos for pos, char in enumerate(word) if char == guess]
            for position in positions:
                plan = plan[:(position*2)] + plan[(position*2):(position+1)*2].replace('_', guess) + plan[(position+1)*2:]
        else:
            lives = lives - 1


'''
možná vylepšení:
- rozdělení kódu do funkcí 
- možnost dopsat celé slovo
- separování seznamu slov do vedlejšího souboru
- 
'''
