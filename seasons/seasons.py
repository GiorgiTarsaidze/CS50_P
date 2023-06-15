from datetime import date
import sys
import inflect
p = inflect.engine()


def main():
    # Asking for birthdate in YYYY-MM-DD format
    birth = input("Date of Birth: ")
    # Checking that format in format_check function
    user_input = format_check(birth)
    # After, transfering our input that is the date class object to another function
    minutes = date_to_minutes(user_input)
    # returning the minutes value and printing it with the inflect module, capitalizing the first letter
    print(minutes_to_text(minutes).capitalize() + " minutes")

def format_check(birth):
    try:
        # Checking for the right format
        inputed_date = date.fromisoformat(birth)
        return inputed_date
    # Expecting the ValueError and exiting via sys
    except ValueError:
        sys.exit("Invalid Date")

def date_to_minutes(inputed_date):
    # Here, we check get the exact date for today and store it in a variable
    date_today = date.today()
    # we subtract our inputted value from today
    delta = date_today - inputed_date
    # Using timedelta function of datetime library, we get the day parameter from it and store it in a variable
    day = delta.days
    # If the day value is negative, we exit via sys
    if day < 0:
        sys.exit("Invalid Date")
    else:
        # Transforming our day value into minutes
        minutes = day*24*60
        return minutes

def minutes_to_text(minutes):
    # Using inflect library, transforming numbers into words
    result = p.number_to_words(minutes, andword= "")
    return result

if __name__ == "__main__":
    main()
