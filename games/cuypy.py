import random
import main

def cuypy_position():
    return random.randint(1, 4)

def start():
    while True:
        bentuk_goa = "|_|"
        goa = [bentuk_goa] * 4
        hasil_goa = " ".join(goa)

        print(f"coba perhatikan goa dibawah ini\n\n{hasil_goa}\n")

        cuyPosition = cuypy_position()
        cuypy_position()
        goa[cuyPosition - 1] = "|0_0|"

        pilihan_user = input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4] ")


        if pilihan_user == str(cuyPosition):
            print(
                f"Selamat kamu menang!! posisi CUYPY di {cuyPosition} dan pilihanmu adalah {pilihan_user}")
            print(" ".join(goa))
        else:
            print(f"KAMU KALAH! pilihan kamu nomor {pilihan_user},tapi CUYPY berada di nomor {cuyPosition}")
            print(" ".join(goa))

        play_again = input("\n\napakah ingin melanjutkan gamenya lagi? [yes/no] ")
        if play_again == "no":
            main.menu()

if __name__ == '__main__':
    start()