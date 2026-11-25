# Banka Hesabı Sınıfı 
class BankAccount:
    # 1. Hesap oluşturulurken ilk bilgileri kaydeder
    def __init__(self, owner, account_no, balance):
        self.owner = owner
        self.account_no = account_no
        self.balance = balance

    # 2. Para yatırma işlemi
    def deposit(self, amount):
        self.balance += amount
        print("Deposited! New balance:", self.balance)

    # 3. Para çekme işlemi
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn! New balance:", self.balance)
        else:
            print("Insufficient balance!")

    # 4. Hesap bilgilerini ve bakiyeyi gösterme
    def show_info(self):
        print("Owner:", self.owner, "| No:", self.account_no, "| Balance:", self.balance)


# Kullanıcıdan bilgileri alıp hesabı başlatma
name = input("Owner Name: ")
acc_no = input("Account Number: ")
start_money = float(input("Initial Balance: "))

# Sınıftan gerçek bir hesap nesnesi üretiyoruz
account = BankAccount(name, acc_no, start_money)

# Kullanıcı çıkış yapana kadar dönen menü
while True:
    print("\n1-Deposit | 2-Withdraw | 3-Show Info | 4-Exit")
    choice = input("Choice (1-4): ")

    if choice == "1":
        money = float(input("Amount to deposit: "))
        account.deposit(money)

    elif choice == "2":
        money = float(input("Amount to withdraw: "))
        account.withdraw(money)

    elif choice == "3":
        account.show_info()

    elif choice == "4":
        print("Exited.")
        break

    else:
        print("Invalid choice!")
