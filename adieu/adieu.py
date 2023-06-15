import inflect

p = inflect.engine()

names = []

while True:
    try:
        a = input("Name: ")
        if a != "":
            names.append(a)
        else:
            continue
    except EOFError:
        print("Adieu, adieu, to " + p.join(names))
        break


