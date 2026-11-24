
households = [
    (80, False, False),
    (100, True, False),
    (101, True, False),
    (150, False, False),
    (200, True, False),
    (201, False, False),
    (250, False, True),
    (300, True, True)
]

print("USING IF-ELIF-ELSE")

for units, ration, elderly in households:

    if units <= 100:
        print("Full subsidy")

    elif 101 <= units <= 200 and ration:
        print("Partial subsidy")

    elif units > 200 and elderly:
        print("Special subsidy")

    else:
        print("No subsidy")
