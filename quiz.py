def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 1:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 2:
        print("The Correct answer is ",answer )

Score = 0
guess2 =input("Who is known as father of our nation?")
check_guess(guess2, "Mahatma Gandhi")
print("Your Score is "+ str(score))
print("Guess the correct answer!")
guess1 = input("Who is known as the God of cricket?")
check_guess(guess1, "Sachin Tendulkar")
print("Your Score is "+ str(score))
