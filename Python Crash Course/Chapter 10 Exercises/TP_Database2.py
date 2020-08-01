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
    tp_database = "tp_userinfo.json"
    with open(tp_database, 'w') as f_obj:
        json.dump(techpriest_un, f_obj)
    return techpriest_un


def greet_user():
    """Greets the user by their inputted name"""
    techpriest_un = get_stored_username()
    if techpriest_un:
        print("Welcome back, tech priest " + techpriest_un.title() + "!")
    else:
        techpriest_un = get_new_username()
        print("We will remember when you get back, tech priest " + techpriest_un.title()
              + "!")

greet_user()