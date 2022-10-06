# The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to evaluate your performance.

# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:


# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!
current_year = 2021


def ageto100(num):
    if age_or_year < 100:
        hundred = current_year - age_or_year
        hundred = hundred + 100
        print(f"In year {hundred} your age will be hundred")
    elif len(str((age_or_year))) >= 4:
        if age_or_year >= current_year - 100:
            hundred = age_or_year + 100
            print(f"In year {hundred} your age will be hundred")
    elif age_or_year >= 100:
                print(f"your are already {age_or_year}")


def agetorandom(num):
    r_age = int(input("Enter the year till you want to know your age"))
    if len(str((age_or_year))) >= 4:
        age = r_age - age_or_year
        print(f"In year {r_age}, you age will be {age}")


if __name__ == '__main__':

    age_or_year = int(input("Enter your age or date of birth year to calculate the future age:"))


    if len(str((age_or_year))) >= 4:
        if age_or_year > current_year:
            print("you are not born yet but if you someone will born in that year you can calculate the age")
        elif age_or_year < current_year - 100:
            print("you seems to be oldest person alive.No worry we will calculate your age too")

    print("what you want to do ?\n"
          "press 1 to know when your age become 100\n"
          "press 2 to know what will be your age at random year ")
    value = int(input("Value:"))
    if value == 1:

        ageto100(age_or_year)
    elif value == 2:
        agetorandom(age_or_year)
