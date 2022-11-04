def main():
    secret_Number = 6

    num_Guess = int(input("Please enter a Number Between 1 and 10 to Guess the Secret Number - "))

    if num_Guess > secret_Number:
        print("Too High!")
        try_Again = input("Try Again? ").lower()
        if try_Again == "yes":
            main()
        else:
            print("Thanks for Playing!")
            exit()

    elif num_Guess < secret_Number:
        print("Too Low!")
        try_Again = input("Try Again? ").lower()
        if try_Again == "yes":
            main()
        else:
            print("Thanks for Playing!")
            exit()
    else:
        print("Just Right!")
        print("Thanks for Playing!")
        exit()


main()
