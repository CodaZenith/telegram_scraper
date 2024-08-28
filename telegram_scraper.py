# filename: telegram_scraper.py
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import csv
import sys

def authenticate():
    api_id = input("Please enter your API ID: ")
    api_hash = input("Please enter your API Hash: ")
    phone_number = input("Please enter your phone number (with country code): ")

    client = TelegramClient(phone_number, api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        try:
            client.send_code_request(phone_number)
            client.sign_in(phone_number, input("Enter the code you received: "))

            # Handle 2FA
            if client.is_user_authorized() and client.get_me().is_self:
                try:
                    client.sign_in(password=input("Your account is secured with 2FA. Please enter your password: "))
                except SessionPasswordNeededError:
                    print("Incorrect password entered.")
                    sys.exit(1)
        except Exception as e:
            print(f"Authentication failed: {e}")
            sys.exit(1)

    return client

def show_menu():
    print("\n1. Scrape Members")
    print("2. About Script")
    choice = input("Choose an option: ")
    return choice

def list_groups(client):
    dialogs = client.get_dialogs()
    groups = [d for d in dialogs if d.is_group]

    if not groups:
        print("No groups found.")
        return None

    for i, group in enumerate(groups, start=1):
        print(f"{i}. {group.name}")
    
    return groups

def scrape_members(client, group):
    members = client.get_participants(group)
    
    with open('members.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'username', 'first_name', 'last_name', 'access_hash'])
        
        for user in members:
            writer.writerow([user.id, user.username, user.first_name, user.last_name, user.access_hash])
    
    print(f'Successfully saved {len(members)} members to members.csv')

def main():
    client = authenticate()

    while True:
        choice = show_menu()
        
        if choice == '1':
            groups = list_groups(client)
            if groups:
                group_choice = int(input("\nEnter the number of the group you want to scrape: ")) - 1
                if 0 <= group_choice < len(groups):
                    scrape_members(client, groups[group_choice])
                else:
                    print("Invalid choice.")
        elif choice == '2':
            print("\nThis script allows you to scrape members from any Telegram group you are a part of.")
            print("You can use the scraped data for various purposes, such as data analysis, marketing, etc.")
        else:
            print("Invalid choice. Please try again.")
        
        again = input("Do you want to perform another action? (y/n): ")
        if again.lower() != 'y':
            break

    client.disconnect()

if __name__ == "__main__":
    main()
