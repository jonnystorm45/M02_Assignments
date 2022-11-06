guess_me = 5

for number in range(10):
    if number < guess_me:
        print("Too Low!")
    if number > guess_me:
        print("Opps!")
    if number == guess_me:
        print("Found it")
exit()
