import random


def get_distance(guess, target):
    return abs(guess - target)


def give_feedback(distance, guess, secret_number):
    if distance == 0:
        return "Congratulations! You guessed the number."
    elif distance <= 10:
        if guess < secret_number:
            return "You're very close! Try a bit higher."
        elif guess > secret_number:
            return "You're very close! Try a bit lower."
    elif distance <= 20:
        if guess < secret_number:
            return "You're getting closer. Try a bit higher."
        elif guess > secret_number:
            return "You're getting closer. Try a bit lower."
    else:
        if guess < secret_number:
            return "You're far away. Try higher."
        elif guess > secret_number:
            return "You're far away. Try lower."


secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Please enter a valid number between 1 and 100.")
        continue

    distance = get_distance(guess, secret_number)
    feedback = give_feedback(distance, guess, secret_number)

    print(feedback)
