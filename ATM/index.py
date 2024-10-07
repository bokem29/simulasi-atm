"""
ATM Sederhana dengan Python
--------------------------

"""


class ATM:
    def __init__(self, pin, balance):
        self.balance = balance
        self.pin = pin

    def check_pin(self):
        entered_pin = input("Masukkan PIN Anda: ")
        if entered_pin == self.pin:
            print("PIN Benar")
            return True
        else:
            print("PIN Salah")
            return False
    
    def check_balance(self):
        print(f"Saldo Anda saat ini adalah: Rp {self.balance}"  )

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Berhasil {amount} ditambahkan")
            self.check_balance()
        else:
            print("Jumlah yang dimasukkan harus lebih besar dari 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Berhasil {amount} dikurangi")
            self.check_balance()
        else:
            print("Jumlah yang dimasukkan harus lebih besar dari 0 dan kurang dari saldo")

    def exit(self):
        print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
        exit()


def atm_menu(atm):
    while True:
        print("\nMenu ATM:")
        print("1. Cek Saldo")
        print("2. Deposit Uang")
        print("3. Tarik Uang")
        print("4. Keluar")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = int(input("Masukkan jumlah deposit: Rp "))
            atm.deposit(amount)
        elif choice == '3':
            amount = int(input("Masukkan jumlah yang akan ditarik: Rp "))
            atm.withdraw(amount)
        elif choice == '4':
            atm.exit()
        else:
            print("Pilihan tidak valid. Coba lagi.")

def main():
    pin = "1234"  # PIN default
    atm = ATM(pin, balance=500000)  # Saldo awal Rp 500.000

    # Proses login
    print("Selamat datang di ATM!")
    while not atm.check_pin():
        pass

    # Tampilkan menu ATM
    atm_menu(atm)

if __name__ == "__main__":
    main()