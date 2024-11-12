from libs import welcome_message, exit_program
from games import cuypy
from tools import warung

def menu():
    user_option = int(input(f"Silahkan pilih menu programnya:\n1. Games CUYPY\n2. Warung Mini\n3. Keluar program\n\nsilahkan pilih: "))

    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print("Hanya boleh pilih yang berada di menu!")

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()
