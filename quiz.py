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
guess2 = input("Who is known as Mr. 360?")
check_guess(guess2, "AB De Villiers")
print("Your Score is "+ str(score))

guess4 = input("Who is the fastest man on planet?")
check_guess(guess4, "Usain Bolt")

guess3 = input("Who won the 2023 FIFA world cup?")
check_guess(guess3, "Argentina")
guess4 = input("Who is the current prime minister of India?")
check_guess(guess4,"Narendra Modi")
guess5 = input("Who is the current president of USA?")
check_guess(guess5, "Joe Biden")


guess6 = input("Who won the 2018 FIFA world cup?")
check_guess(guess6, "France")
guess7 = input("Who won the 2011 cricket world cup?")
check_guess(guess7,"India")
guess8 = input("Who is the president of india?")
check_guess(guess8, "Droupadi Murmu")

