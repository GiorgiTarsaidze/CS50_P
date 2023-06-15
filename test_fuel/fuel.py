def main():
    fraction = input("Fraction: ")
    to_convert = convert(fraction)
    to_gauge = gauge(to_convert)
    print(to_gauge)

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError

            result = round(x/y*100)
            return result
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        output = str(percentage)
        return output+"%"

if __name__ == "__main__":
    main()