import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    format_search = re.search(pattern,s)
    if format_search:
        startH, startM, sAP = int(format_search.group(1)), int(format_search.group(2) or 0), format_search.group(3)
        finishH, finishM, fAP = int(format_search.group(4)), int(format_search.group(5) or 0), format_search.group(6)

    else:
        raise ValueError("Incorrect time format")

    if startH < 1 or startH > 12 or finishH < 1 or finishH > 12 or startM < 0 or startM > 59 or finishM < 0 or finishM > 59:
            raise ValueError("Incorrect time format")

    if sAP == "PM" and startH != 12:
        startH += 12
    elif sAP == "AM" and startH == 12:
        startH = 0

    if fAP == "PM" and finishH != 12:
        finishH += 12
    elif fAP == "AM" and finishH == 12:
        finishH = 0

    return f"{startH:02d}:{startM:02d} to {finishH:02d}:{finishM:02d}"


if __name__ == "__main__":
    main()