import random

def hangman():
    word = random.choice(['python', 'java', 'coding', 'computer', 'program'])
    guessed = []
    wrong = 0
    
    while wrong < 6:
        # Show word with blanks
        display = ''.join([letter if letter in guessed else '_' for letter in word])
        print(f"\nWord: {display}")
        
        if '_' not in display:
            print(f"You win! The word was: {word}")
            return
        
        # Show hangman
        print(f"Wrong guesses: {wrong}/6")
        print("  O\n /|\\\n / \\"[:(wrong*5)])
        
        # Get guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter only!")
            continue
        
        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            print("Good guess!")
            guessed.append(guess)
        else:
            print("Wrong!")
            guessed.append(guess)
            wrong += 1
    
    print(f"\nGame over! The word was: {word}")

# Play the game
hangman()