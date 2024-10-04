def race_output(race):
    if race == 1:
        print("cracker")
    elif race == 2:
        print("nigga")
    elif race == 3:
        print("can you even read this")
    elif race == 4:
        print("beaner")

def race_ui():
    print("Type 1 for white")
    print("Type 2 for black")
    print("Type 3 for asian")
    print("Type 4 for mexican")
    print("Type 5 to quit")


def main():
    race_ui()
    while True:
        race = int(input("Enter a race:"))
        if race == 5:
            break
        else:
            race_output(race)

if __name__ == "__main__":
    main()
