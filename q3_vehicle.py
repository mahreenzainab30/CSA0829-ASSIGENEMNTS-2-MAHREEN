
def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[0:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not reg[4:-4].isalpha():
        return False

    if not (1 <= len(reg[4:-4]) <= 2):
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_number(reg):
    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN09AB1234",
    "TN 22 1234 AB",
    "MH 12 CD 5678",
    "KL-07-A-4321"
]

for number in numbers:
    clean = normalise(number)

    if is_valid(clean):
        print(number, "->", format_number(clean), "VALID")
    else:
        print(number, "->", clean, "INVALID")
