
guess_me = 7
number = 1


while number < guess_me:
    print("Too Low!")
    number += 1

    if number > guess_me:
        print("Opps!")
        number += 1

    if number == guess_me:
        print("Found It!")
