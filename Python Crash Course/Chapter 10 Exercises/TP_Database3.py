import json

def get_stored_username():
    """Get stored username if available."""
    tp_database = "tp_userinfo.json"
    try:
        with open(tp_database) as f_obj:
            techpriest_un = json.load(f_obj)
            # Loads the Memory.json file, and checks to see if there is a familiar user
    except FileNotFoundError:
        return None
    else:
        return techpriest_un

def get_new_username():
    """Prompts the user to input their name into system"""
    techpriest_un = input("What is your name, tech priest? Type here: ")
    # Asks the user for their name
    tp_database = "tp_userinfo.json" # JSON file directory
    with open(tp_database, 'w') as f_obj:
        json.dump(techpriest_un, f_obj)
        # Writes a new user name into the system
    return techpriest_un


def greet_user():
    """Greets the user by their inputted name"""
    techpriest_un = get_stored_username() # Calls upon the get_stored_username method
    valid_tp = input("Is your name tech priest " + techpriest_un + "?\n" +
                     "(Type 'y' for yes, 'n' for no)")
    # Prompts the user if their name is displayed in the system
    if valid_tp.lower() == "y":
        print("Welcome back, tech priest " + techpriest_un.title() + "!")
        # If so, this welcome prompt triggers
    elif valid_tp.lower() == "n":
        techpriest_un = get_new_username() # If not, calls the get_new_username() method...
        print("We will remember when you get back, tech priest " + techpriest_un.title()
              + "!")
        # then it stores a memory of that user for a second run of the program

greet_user()