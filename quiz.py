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
