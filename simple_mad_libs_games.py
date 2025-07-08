def mad_libs():
    print("Welcome to the Mad libs Game:")
    print("Fill in the blanks with your own words:\n")

    # Taking user input

    adjective = input("Enter and adjective:")
    animal = input("Enter an animal:")
    verb = input("Enter a verb:")
    exclamation = input("Enter an exclamation (e.g, wow! oh no!):")
    noun = input("Enter a noun:")
    verb_past = input("Enter a past tense verb:")
    
    #story using user inputs

    print("\nHere's your story:")
    print("--------------------")
    print(f"the other day, I was walking through the jungle when i saw a {adjective} {animal}.")
    print(f"It started to {verb} toward me. i yelled, '{exclamation}! and ran as fast as i could.")
    print(f"But then i tripped on a {noun} and {verb_past} all the way home.")
    print("-------------------------")
mad_libs()