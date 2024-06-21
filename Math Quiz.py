# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

                    ⭐⭐⭐⭐ Instructions ⭐⭐⭐⭐

 During this quizz you will have to answer 5 mathematical equations to finsh!
                             
                            😊 GOOD LUCK 😊''')


def int_checker(question):
    while True:
        try:
            check = int(input(question))
            return check
        except ValueError:
            print()
            print("Please enter a number")
            print()


# Program starts here (with a heading)
print()
print(" 📚📚 Math Quiz 📚📚 ")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()

# Counter to track how many questions you got right
counter = 0

# Recorde game history
quiz_history = []
history_item = f"round: {counter}"

# Math quiz question starts here
print()
question_1 = int_checker("1)  What is 8 x 7 ?")
if question_1 == 56:
    print(" ✅ Correct! ✅")
    print()
    counter += 1
else:
    print(" ❌ Incorrect! ❌ The answer was 56")
    print()
quiz_history.append(question_1)

# Question 2
question_2 = int_checker("2)  What is 150 ÷ 3 ?")
if question_2 == 50:
    print(" ✅ Correct! ✅")
    print()
    counter += 1
else:
    print(" ❌ Incorrect! ❌ The answer was 50")
    print()
quiz_history.append(question_2)

# Question 3
question_3 = int_checker("3)  What is 9 + 6 ?")
if question_3 == 15:
    print(" ✅ Correct! ✅")
    print()
    counter += 1
else:
    print(" ❌ Incorrect! ❌ The answer was 15")
    print()
quiz_history.append(question_3)

# Question 4
question_4 = int_checker("4)  What is 5 x 12 ?")
if question_4 == 60:
    print(" ✅ Correct! ✅")
    print()
    counter += 1
else:
    print(" ❌ Incorrect! ❌ The answer was 60")
    print()
quiz_history.append(question_4)

# Question 5
question_5 = int_checker("5)  What is 22 - 3?")
if question_5 == 19:
    print(" ✅ Correct! ✅")
    print()
    counter += 1
else:
    print(" ❌ Incorrect! ❌ The answer was 19")
    print()
    quiz_history.append(question_5)

# Calculate counter of questions you got right
print(f" 🥳 You got {counter} answers correct 🥳")
print()

# Do you want to read the quizz history and will print if the user says yes
# It will print the questions, there answers then the correct answers

history_print = yes_no("Do you want to read the quiz history?")
if history_print == "yes":
    print()
    print("Question 1: What is 8 x 7")
    print(f"Your answer was {quiz_history[0]}")
    print("The answer was 56")
    print()

    print("Question 2: What is 150 ÷ 3")
    print(f"Your answer was {quiz_history[1]}")
    print("The answer was 50 ")
    print()

    print("Question 3: What is 9 + 6")
    print(f"Your answer was {quiz_history[2]}")
    print("The answer was 15 ")
    print()

    print("Question 4: What is 5 x 12")
    print(f"Your answer was {quiz_history[3]}")
    print("The answer was 60 ")
    print()

    print("Question 5: What is 22 - 3")
    print(f"Your answer was {quiz_history[4]}")
    print("The answer was 19")
    print()

print()
print(" 😎 Thank you for taking the quiz 😎")
