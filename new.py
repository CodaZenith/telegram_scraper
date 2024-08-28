import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "╔═══════════════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + "         WELCOME TO THE MAIN MENU         " + Fore.CYAN + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚═══════════════════════════════════════════╝\n")

    print(Fore.MAGENTA + Style.BRIGHT + " 1." + Fore.WHITE + " Termux Set-Up")
    print(Fore.MAGENTA + Style.BRIGHT + " 2." + Fore.WHITE + " Termux Front and Theme")
    print(Fore.MAGENTA + Style.BRIGHT + " 3." + Fore.WHITE + " Python Encryption")
    print(Fore.MAGENTA + Style.BRIGHT + " 4." + Fore.WHITE + " Facebook Brute Force\n")
    
    print(Fore.MAGENTA + Style.BRIGHT + " 5." + Fore.WHITE + " Termux Banner [V1]")
    print(Fore.MAGENTA + Style.BRIGHT + " 6." + Fore.WHITE + " Termux Banner [V2]")
    print(Fore.MAGENTA + Style.BRIGHT + " 7." + Fore.WHITE + " Kali Linux Nethunter")
    print(Fore.MAGENTA + Style.BRIGHT + " 8." + Fore.WHITE + " Wifi Hacking [Rooted Device]\n")

    print(Fore.MAGENTA + Style.BRIGHT + " 9." + Fore.WHITE + " OSINT")
    print(Fore.MAGENTA + Style.BRIGHT + " 10." + Fore.WHITE + " Ultra DDoS")
    print(Fore.MAGENTA + Style.BRIGHT + " 11." + Fore.WHITE + " Number Info")
    print(Fore.MAGENTA + Style.BRIGHT + " 12." + Fore.WHITE + " Fix Termux\n")

    print(Fore.MAGENTA + Style.BRIGHT + " 13." + Fore.WHITE + " U Phisher")
    print(Fore.MAGENTA + Style.BRIGHT + " 14." + Fore.WHITE + " Brute")
    print(Fore.MAGENTA + Style.BRIGHT + " 15." + Fore.WHITE + " Info X")
    print(Fore.MAGENTA + Style.BRIGHT + " 0." + Fore.WHITE + " Exit Program\n")

    print(Fore.CYAN + Style.BRIGHT + "═════════════════════════════════════════════")
    print(Fore.YELLOW + Style.BRIGHT + "Select an option:" + Fore.RESET + " ", end='')

def main():
    while True:
        display_menu()
        option = input()
        if option == '0':
            print(Fore.RED + "\nExiting program...")
            break
        else:
            print(Fore.GREEN + f"\nYou selected option {option}. This is where the function would be executed.")
            input(Fore.CYAN + Style.BRIGHT + "\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
