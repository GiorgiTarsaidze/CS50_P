def convert(c):
    x = c.replace(":)","🙂")
    y = x.replace(":(","🙁")
    return y

def main():
    c = str(input())
    final = convert(c)
    print(final)

main()