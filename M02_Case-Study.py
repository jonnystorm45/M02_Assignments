# Jonathan Storm Anderson
# M02_Case_Study.py
# This App will allow the user to enter either the last name and then first name of a student to test
# a students GPA against the Deans List and Honor Roll requirements or input "ZZZ" and end the program.
# There will also be an option to continue to enter students names and GPAs until there are no more to test.

def main():
    global Student_First_Name
    Student_Last_Name = input("Please Enter Student's Last Name or 'ZZZ' to End Program - ")

    while Student_Last_Name.upper() == "ZZZ":
        print("Program Ended")
        break
        exit()

    if Student_Last_Name != "ZZZ":

        Student_First_Name = input("PLease Enter Student's First Name - ")

        Student_GPA = float(input("Please Enter Student's GPA on a 4.0 Scale -  "))

        if Student_GPA >= 3.5:
            print(Student_First_Name, Student_Last_Name, "has made the Dean's List!")
        elif Student_GPA >= 3.25:
            print(Student_First_Name, Student_Last_Name, "has made the Honor Roll!")
        else:
            print(Student_First_Name, Student_Last_Name, "has not made any lists.")

        restart = input("More Students GPAs to Test? ").lower()
        if restart == "yes":
            main()
        else:
            print("Program Ended!")
            print("Thank you! Goodbye!")
            exit()
    else:
        print("Thank you! Goodbye!")
        exit()


main()
