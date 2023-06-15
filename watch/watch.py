import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r"<iframe(.)*><\/iframe>"
    if re.search(pattern,s):
        link = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)*",s)
        if link:
            defactor = link.groups()
            return "https://youtu.be/" + defactor[3]

if __name__ == "__main__":
    main()







if __name__ == "__main__":
    main()