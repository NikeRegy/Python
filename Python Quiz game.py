#Python quiz game

questions =("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ", 
            "What is the most abundant gas in Earth's atnosphere?: ", 
            "How many bones are in the human body?: ", 
            "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"), 
           ("A. Mecury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0


for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1



print("--------------")
print("   RESULTS    ")
print("--------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ", 
    "What is the most abundant gas in Earth's atmosphere?: ",  
    "How many bones are in the human body?: ", 
    "Which planet in the solar system is the hottest?: ",
    "What is the chemical symbol for gold?: ",
    "Which organ pumps blood through the body?: ",
    "What is the powerhouse of the cell?: ",
    "How many continents are there on Earth?: ",
    "Which ocean is the largest?: ",
    "What is the capital of France?: ",
    "How many legs does a spider have?: ",
    "Which gas do plants absorb from the atmosphere?: ",
    "What is the boiling point of water in Celsius?: ",
    "Who developed the theory of relativity?: ",
    "Which instrument measures atmospheric pressure?: ",
    "Which part of the human body contains the most bones?: ",
    "What is the hardest natural substance on Earth?: ",
    "Which planet is known as the Red Planet?: ",
    "What is the capital of Japan?:"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Au", "B. Ag", "C. Fe", "D. Pb"),
    ("A. Liver", "B. Heart", "C. Brain", "D. Kidney"),
    ("A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Cytoplasm"),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"),
    ("A. Rome", "B. London", "C. Paris", "D. Berlin"),
    ("A. 6", "B. 8", "C. 10", "D. 12"),
    ("A. Oxygen", "B. Carbon-Dioxide", "C. Hydrogen", "D. Nitrogen"),
    ("A. 90", "B. 100", "C. 110", "D. 120"),
    ("A. Newton", "B. Einstein", "C. Galileo", "D. Tesla"),
    ("A. Thermometer", "B. Barometer", "C. Hygrometer", "D. Anemometer"),
    ("A. Skull", "B. Spine", "C. Hands", "D. Feet"),
    ("A. Gold", "B. Iron", "C. Diamond", "D. Silver"),
    ("A. Mars", "B. Jupiter", "C. Saturn", "D. Uranus"),
    ("A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok")
)

answers = ("C", "D", "A", "A", "B", "A", "B", "B", "D", "D", "C", "B", "B", "B", "B", "B", "D", "C", "A", "C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1

print("--------------")
print("   RESULTS    ")
print("--------------")

print("Answers: ", " ".join(answers))
print("Guesses: ", " ".join(guesses))

print("\nYou scored", score, "out of 20!")

if score >= 18:
    grade = "A1"
    print(f"Excellent! You got {grade}!")
elif score >= 16:
    grade = "B2"
    print(f"Great job! You got {grade}!")
elif score >= 14:
    grade = "B3"
    print(f"Good effort! You got {grade}!")
elif score >= 12 :
    grade = "C4"
    print(f"Nice work! You got {grade}!")
elif score >= 10:
    grade = "C5"
    print(f"Keep it up! You got {grade}!")
elif score >= 8:
    grade = "C6"
    print(f"You passed! You got {grade}!")
elif score >= 6:
    grade = "D7"
    print(f"Almost there! You got {grade}!")
elif score >= 4:
    grade = "E8"
    print(f"Needs improvement! You got {grade}!")
else:
    grade = "F9"
    print(f"Better luck next time! You got {grade}!")




