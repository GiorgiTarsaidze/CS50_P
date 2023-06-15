def main():
    #We store our input value into variable time and send this value into convert function where it converts to float time.
    time = input("What time is it?")
    float_Time = convert(time)

    if 7.0 <= float_Time <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_Time <= 13.0:
        print("lunch time")
    elif 18.0 <= float_Time <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    #Using split function, we seperate hours and minutes and store them into new variables.
    hours, minutes = time.split(":")
    #Here we convert minutes that are in 1 - 60 range to float and then add hour float to minute float and we return our float time.
    float_minutes = float(minutes)/60
    float_hours = float(hours)
    time = float_hours + float_minutes
    return float(time)


if __name__ == "__main__":
    main()

