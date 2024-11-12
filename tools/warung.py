import main

def start():
    while True:
        print("Ini warung apps!!")
        play_again = input('Kembali ke menu utama? [yes/no] ')

        if play_again == "yes":
            main.menu()

if __name__ == '__main__':
    start()