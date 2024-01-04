import simplejson as json
import sys
import db


def main():
    # load list of characters/columns
    character_list = db.get_names()
    character__tabs = db.get_columns()

    # TEST DATA
    correct_char = map_character_data(db.get_columns(), db.get_character_data("'Adolin'"))
    print(correct_char)
    guess_char = {}
    #TEST DATA

    # get user input and validate if it's a correct character
    while True:
        try:
            guess = input("Guess a cosmere character: ")
        except ValueError:
            print("Incorrect input, try again!")
            continue

        if guess not in (character_list):
            print("Character not recognised, try again!")
            continue
        else:
            break

    # check if guess is correct
    if guess == correct_char["name"]:
        print("Correct!")
        sys.exit()

    # if not correct, get data and print closeness (0, 1, 2) to correct criteria
    guess_char = map_character_data(db.get_columns(), db.get_character_data(f"'{guess}'")) 
    get_matches(correct_char, guess_char)



def get_matches(correct_char, guess_char):
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


def map_character_data(columns, data):
    character_dict = {}
    investitures = []
    for idx, x in enumerate(columns):
        if x == "investiture":
            for investure_type in data[idx].split(","):
                investitures.append(investure_type.strip())
            character_dict[columns[idx]] = investitures
        else:
            character_dict[columns[idx]] = data[idx]
    return character_dict


if __name__ == "__main__":
    main()