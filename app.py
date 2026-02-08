# app.py

from don.age_calculator import run_age_calculator
from uriah.greeting import greet_user
from noxiusm.favorite_color import ask_color
from jassan.lucky_number import ask_lucky


def main():
    print("\n===== TEAM APPLICATION =====")
    print("1. Calculate Age (Don)")
    print("2. Greeting (Uriah)")
    print("3. Favorite Color (NoxiusM)")
    print("4. Lucky Number (Jassan)")
    print("5. Exit")
    print("============================")

    choice = input("Select option (1-5): ")

    if choice == "1":
        run_age_calculator()
    elif choice == "2":
        greet_user()
    elif choice == "3":
        ask_color()
    elif choice == "4":
        ask_lucky()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
