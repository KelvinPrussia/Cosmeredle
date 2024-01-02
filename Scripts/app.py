import simplejson as json
import sys


def main():
    # import test data
    with open('characters.json') as f:
        characters = json.load(f)

    # set test character to kaladin
    correct_char = characters[3]
    guess_char = {}

    # get user input and validate if it's a correct character
    while True:
        try:
            guess = input("Guess a cosmere character: ")
        except ValueError:
            print("Incorrect input, try again!")
            continue

        if guess not in ("Shallan", "Kaladin", "Vin"):
            print("Character not recognised, try again!")
            continue
        else:
            break

    # check if name is 
    if guess == correct_char["name"]:
        print("Correct!")
        sys.exit()

    for character in characters:
        if character["name"] == guess:
            guess_char = character

    for attribute in correct_char:
        match attribute:
            case "species":
                guess_species = guess_char["species"]
                correct_species = correct_char["species"]
                if guess_species == correct_species:
                    print(2)
                elif "(" in guess_species and correct_species:
                    compare_prefix(guess_species, correct_species.split("(")[0]) 
                else:
                    print(0)
            case "investiture":
                if guess_char[attribute] == correct_char[attribute]:
                    print(2)
                else:
                    compare_lists(guess_char[attribute], correct_char[attribute])
            case _:
                if guess_char[attribute] == correct_char[attribute]:
                    print(2)
                else:
                    print(0)

def compare_prefix(guess_species, correct_species):
    if guess_species.split("(")[0] == correct_species.split("(")[0]:
        print(1)
    else:
        print(0)


def compare_lists(guess_list, correct_list):
    if sorted(guess_list) == sorted(correct_list):
        print(2)
    elif (set(guess_list) & set(correct_list)):
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()