import json
import os

from colorama import Fore, Style, init
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest

# Initialize Colorama
init(autoreset=True)

# Define title, version, and developer information
title = """
 ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ██╗███╗   ██╗███████╗██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██║████╗  ██║██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝
██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝██║██╔██╗ ██║███████╗██║██║  ███╗███████║   ██║   
██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ██║██║╚██╗██║╚════██║██║██║   ██║██╔══██║   ██║   
╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ██║██║ ╚████║███████║██║╚██████╔╝██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
"""

version = "Version: 1.0"
developer_info = f"""
{Fore.LIGHTGREEN_EX}↳ {Fore.YELLOW}DEVELOPER    {Fore.RESET}: {Fore.CYAN}CadaZenith
{Fore.LIGHTGREEN_EX}↳ {Fore.YELLOW}EMAIL        {Fore.RESET}: {Fore.CYAN}zenith.fusionsphere@gmail.com
{Fore.LIGHTGREEN_EX}↳ {Fore.YELLOW}WEBSITE      {Fore.RESET}: {Fore.CYAN}www.codazenith.blogspot.com
"""

# Privacy notice
privacy_notice = """
{Fore.RED}NOTICE:{Fore.RESET}
{Fore.LIGHTYELLOW_EX}We do not store or use any of your personal data. Your API ID, API Hash, phone number, and OTP are only used to authenticate with Telegram and are not saved or used for any other purpose.
{Fore.LIGHTYELLOW_EX}Your privacy and security are our top priorities. If you have any concerns, please contact us at zenith.fusionsphere@gmail.com.
"""

# Simplified menu options without borders
menu_options = [
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}01{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}SCRAPE MEMBERS FROM GROUP",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}02{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}EXPORT MEMBERS TO FILE",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}03{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}SETTINGS",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}04{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}LOGIN",
    f"{Style.BRIGHT + Fore.LIGHTGREEN_EX}[{Fore.RED}05{Fore.LIGHTGREEN_EX}] {Fore.LIGHTYELLOW_EX}EXIT"
]

# Settings data
settings_data = """
{Fore.CYAN}Settings{Fore.RESET}:
1. {Fore.LIGHTGREEN_EX}API ID{Fore.RESET}: The unique identifier for your Telegram application.
2. {Fore.LIGHTGREEN_EX}API Hash{Fore.RESET}: The secret key for your Telegram application.
3. {Fore.LIGHTGREEN_EX}Phone Number{Fore.RESET}: The phone number associated with your Telegram account.
4. {Fore.LIGHTGREEN_EX}OTP{Fore.RESET}: The one-time password sent by Telegram for authentication.
5. {Fore.LIGHTGREEN_EX}Privacy Notice{Fore.RESET}: We do not store your data. Read our privacy policy for more details.

{Fore.LIGHTYELLOW_EX}To update these settings, please re-enter your API ID, API Hash, phone number, and OTP.
"""

# Function to initialize the Telegram client with user input
def initialize_client():
    print(privacy_notice)
    api_id = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your API ID: ")
    api_hash = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your API Hash: ")
    phone_number = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your phone number: ")
    otp = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter your OTP: ")
    return TelegramClient('session_name', api_id, api_hash), phone_number, otp

# Function to check if the user is logged in
def is_logged_in(client):
    try:
        client.start()
        return True
    except SessionPasswordNeededError:
        print(Fore.RED + "Two-step verification is enabled. Please provide your password.")
        return False
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        return False

# Function to display the title, version, and developer information
def print_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + Style.BRIGHT + title)
    print(Fore.YELLOW + Style.BRIGHT + version)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + developer_info)

# Function to display the simplified menu options
def print_menu():
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n[•] MENU OPTIONS:\n")
    for option in menu_options:
        print(option)  # Print options line by line

# Function to display settings
def print_settings():
    print(settings_data)

# Function to scrape members from selected group
def scrape_members(client, group_name, num_members):
    try:
        all_dialogs = client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            limit=100,
            hash=0
        ))
        groups = [dialog for dialog in all_dialogs.chats if dialog.title]

        group = next((g for g in groups if g.title == group_name), None)
        if not group:
            print(Fore.RED + f"Failed to find group: {group_name}")
            return

        # Placeholder for scraping members
        print(Fore.LIGHTGREEN_EX + f"Scraping members from {group.title}...")
        scraped_members = []
        failed_members = []
        # Simulate member scraping
        for i in range(num_members):
            if i % 10 == 0:
                # Simulate a failure for every 10th member
                failed_members.append(f"User_{i}")
            else:
                scraped_members.append(f"User_{i}")

        # Output results
        if scraped_members:
            print(Fore.GREEN + f"Successfully scraped {group.title}.")
            print(Fore.GREEN + "Scraped members:")
            for member in scraped_members:
                print(f" - {member}")
        if failed_members:
            print(Fore.RED + "Failed to scrape members:")
            for member in failed_members:
                print(f" - {member}")

        return scraped_members, failed_members
    except Exception as e:
        print(Fore.RED + f"An error occurred during scraping: {e}")
        return [], []

# Function to export members to a file
def export_members(scraped_data):
    if not scraped_data:
        print(Fore.RED + "No data to export. Please scrape members first.")
        return

    print(Fore.LIGHTYELLOW_EX + "[>>] SELECT YOUR OPTION:")
    print(Fore.LIGHTYELLOW_EX + "[01] Download to phone storage")
    print(Fore.LIGHTYELLOW_EX + "[02] Download to SD card")

    choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Select download option: ")

    if choice == '1':
        path = os.path.expanduser("~/Downloads/scraped_members.json")
    elif choice == '2':
        path = "/storage/emulated/0/sdcard0/scraped_members.json"
    else:
        print(Fore.RED + "Invalid option. Exiting...")
        return

    with open(path, 'w') as file:
        json.dump(scraped_data, file)

    print(Fore.GREEN + f"Members exported to {path}")

def main():
    client, phone_number, otp = initialize_client()

    if not is_logged_in(client):
        print(Fore.RED + "Please log in with your Telegram account.")
        return

    scraped_data = {}

    while True:
        print_title()
        print_menu()
        choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n[>>] SELECT YOUR OPTION: ")

        if choice == '1':
            print(Fore.LIGHTYELLOW_EX + "\n[>>] SELECT A GROUP TO SCRAPE:")
            # Fetch groups
            all_dialogs = client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                limit=100,
                hash=0
            ))
            groups = [dialog for dialog in all_dialogs.chats if dialog.title]

            for idx, group in enumerate(groups):
                print(Fore.LIGHTGREEN_EX + f"[{idx + 1}] {group.title}")

            group_choice = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the number of the group: ")) - 1
            if 0 <= group_choice < len(groups):
                selected_group = groups[group_choice]
                num_members = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the number of members to scrape: "))

                scraped_members, failed_members = scrape_members(client, selected_group.title, num_members)
                if scraped_members:
                    scraped_data[selected_group.title] = scraped_members
                if failed_members:
                    print(Fore.RED + "Some members failed to scrape.")

                print(Fore.LIGHTYELLOW_EX + f"You selected scrapped member {num_members} is completed.")
            else:
                print(Fore.RED + "Invalid group selection.")

        elif choice == '2':
            if not scraped_data:
                print(Fore.RED + "No scraped data available. Please scrape members first.")
            else:
                print(Fore.LIGHTYELLOW_EX + "[>>] LIST OF SCRAPED GROUPS:")
                for idx, (group_name, members) in enumerate(scraped_data.items()):
                    print(Fore.LIGHTGREEN_EX + f"[{idx + 1}] {group_name} - {len(members)} members")

                print(Fore.LIGHTYELLOW_EX + "[>>] SELECT A GROUP TO EXPORT:")
                export_choice = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Enter the number of the group: ")) - 1
                if 0 <= export_choice < len(scraped_data):
                    group_name = list(scraped_data.keys())[export_choice]
                    export_members(scraped_data[group_name])
                else:
                    print(Fore.RED + "Invalid selection.")

        elif choice == '3':
            print_settings()

        elif choice == '4':
            # Login - handle re-authentication if needed
            client, phone_number, otp = initialize_client()
            if not is_logged_in(client):
                print(Fore.RED + "Login failed.")
            else:
                print(Fore.GREEN + "Login successful.")

        elif choice == '5':
            print(Fore.RED + "Exiting...")
            break

        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

