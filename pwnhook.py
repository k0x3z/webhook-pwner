import os
import requests
import base64

# ANSI codes for text coloring
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

# Variable to store the webhook URL
current_webhook_url = None

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    """Print the title in ASCII art centered and in blue."""
    title = (
        "              _                   _                                     \n"
        "             | |                 | |                                    \n"
        "__      _____| |__ _______   ___ | | __  _ ____      ___ __   ___ _ __ \n"
        "\\ \\ /\\ / / _ \\ '_ \\_  / _ \\ / _ \\| |/ / | '_ \\ \\ /\\ / / '_ \\ / _ \\ '__|\n"
        " \\ V  V /  __/ |_) / / (_) | (_) |   <  | |_) \\ V  V /| | | |  __/ |   \n"
        "  \\_/\\_/ \\___|_.__/___\\___/ \\___/|_|\\_\\ | .__/ \\_/\\_/ |_| |_|\\___|_|   \n"
        "                                        | |                             \n"
        "                                        |_|                             \n"
    )
    print(f"{BLUE}{title}{RESET}")

def print_description():
    """Print the program's description."""
    print("This program sends messages and images to a Discord webhook.\n")

def print_options():
    """Print the available options."""
    options = [
        "[1] Webhook Spam",
        "[2] Send an image with a message",
        "[3] Pwn a Webhook",  # Added "Pwn a Webhook" option
        "[4] Manage a Webhook",
        "[5] Quit",
        "[6] Attach a webhook"
    ]
    print("Options:")
    for option in options:
        print(f"{RED}{option}{RESET}")

def pwn_webhook(webhook_url):
    """Simulate a conversation with the webhook (like a controlled chat)."""
    print(f"{BLUE}[+] You now have access to a chat with the webhook.{RESET}")
    while True:
        message = input("Enter your message to send to the webhook (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            print(f"{BLUE}[+] Closing the conversation with the webhook.{RESET}")
            break
        else:
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code == 204:
                print(f"{BLUE}[+] Message '{message}' successfully sent to the webhook.{RESET}")
            else:
                print(f"{RED}[-] Failed to send the message. Status code: {response.status_code}{RESET}")

def manage_webhook_menu():
    """Display the webhook management submenu."""
    management_title = (
        "                                                       _     _                 _    \n"
        " _ __ ___   __ _ _ __   __ _  __ _  ___  __      _____| |__ | |__   ___   ___ | | __\n"
        "| '_ ` _ \\ / _` | '_ \\ / _` |/ _` |/ _ \\ \\ \\ /\\ / / _ \\ '_ \\| '_ \\ / _ \\ / _ \\| |/ /\n"
        "| | | | | | (_| | | | | (_| | (_| |  __/  \\ V  V /  __/ |_) | | | | (_) | (_) |   < \n"
        "|_| |_| |_|\\__,_|_| |_|\\__,_|\\__, |\\___|   \\_/\\_/ \\___|_.__/|_| |_|\\___/ \\___/|_|\\_\\\n"
        "                             |___/                                                  \n"
    )
    print(f"{BLUE}{management_title}{RESET}")
    options = [
        "[1] Rename the Webhook",
        "[2] Change the profile picture",
        "[3] Delete the Webhook",
        "[4] Return to the main menu"
    ]
    print("Management options:")
    for option in options:
        print(f"{RED}{option}{RESET}")

def rename_webhook(webhook_url):
    """Rename the webhook by sending a PATCH request."""
    new_name = input("Enter the new name for the webhook: ")
    payload = {"name": new_name}
    response = requests.patch(webhook_url, json=payload)

    if response.status_code == 200:
        print(f"{BLUE}[+] Webhook successfully renamed to '{new_name}'{RESET}")
    else:
        print(f"{RED}[-] Failed to rename the webhook. Status code: {response.status_code}{RESET}")

def change_webhook_avatar(webhook_url):
    """Change the webhook's avatar."""
    image_path = input("Enter the path to the image for the avatar: ")
    try:
        # Replace backslashes with slashes to avoid errors on Windows
        image_path = image_path.replace("\\", "/")

        with open(image_path, "rb") as image_file:
            # Read the image data
            image_data = image_file.read()
            # Encode the data in base64
            encoded_image = base64.b64encode(image_data).decode("utf-8")
            # Prepare the payload with the encoded avatar
            payload = {"avatar": f"data:image/png;base64,{encoded_image}"}
            
            # Send the PATCH request to change the avatar
            response = requests.patch(webhook_url, json=payload)

            if response.status_code == 200:
                print(f"{BLUE}[+] Webhook avatar successfully changed{RESET}")
            else:
                print(f"{RED}[-] Failed to change the avatar. Status code: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{RED}[-] An error occurred while opening the image: {e}{RESET}")

def delete_webhook(webhook_url):
    """Delete the webhook."""
    response = requests.delete(webhook_url)

    if response.status_code == 204:
        print(f"{BLUE}[+] Webhook successfully deleted{RESET}")
    else:
        print(f"{RED}[-] Failed to delete the webhook. Status code: {response.status_code}{RESET}")

def manage_webhook(webhook_url):
    """Function to manage the webhook."""
    while True:
        manage_webhook_menu()
        choice = input("\nChoose a management option: ")

        if choice == '1':
            rename_webhook(webhook_url)
        elif choice == '2':
            change_webhook_avatar(webhook_url)
        elif choice == '3':
            delete_webhook(webhook_url)
            break  # Return to the main menu after deletion
        elif choice == '4':
            break  # Return to the main menu
        else:
            print(f"{RED}Invalid option. Try again.{RESET}")

def send_message_with_image(webhook_url, message, image_path, count):
    """Send a message with an image."""
    try:
        with open(image_path, "rb") as image_file:
            files = {
                "file": (os.path.basename(image_path), image_file, "image/png")
            }
            data = {
                "content": message
            }
            # Send the POST request with the message and image data
            for _ in range(count):
                response = requests.post(webhook_url, data=data, files=files)
                if response.status_code == 204:
                    print(f"{BLUE}[+] Message and image successfully sent{RESET}")
                else:
                    print(f"{RED}[-] Failed to send the message and image. Status code: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{RED}[-] An error occurred while sending the image: {e}{RESET}")

def attach_run_webhook():
    """Attach a webhook for use in the program."""
    global current_webhook_url
    if current_webhook_url:
        print(f"{BLUE}[+] Current webhook: {current_webhook_url}{RESET}")
        change = input("Would you like to change the webhook URL? (y/n): ").lower()
        if change == 'y':
            current_webhook_url = input("Enter the new webhook URL: ")
            print(f"{BLUE}[+] Webhook updated: {current_webhook_url}{RESET}")
    else:
        current_webhook_url = input("Enter the webhook URL to attach: ")
        print(f"{BLUE}[+] Webhook attached: {current_webhook_url}{RESET}")

def main():
    clear_terminal()
    print_title()
    print_description()
    print_options()
    
    while True:
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            if current_webhook_url:
                webhook_url = current_webhook_url
                message = input("Enter the message to send: ")
                count = int(input("How many times to send the message? "))
                send_message_with_image(webhook_url, message, "image.png", count)
            else:
                print(f"{RED}[-] No webhook attached. Please attach a webhook first.{RESET}")
        elif choice == '2':
            if current_webhook_url:
                webhook_url = current_webhook_url
                message = input("Enter the message to send: ")
                image_path = input("Enter the path to the image: ")
                count = int(input("How many times to send the message with the image? "))
                send_message_with_image(webhook_url, message, image_path, count)
            else:
                print(f"{RED}[-] No webhook attached. Please attach a webhook first.{RESET}")
        elif choice == '3':
            if current_webhook_url:
                pwn_webhook(current_webhook_url)
            else:
                print(f"{RED}[-] No webhook attached. Please attach a webhook first.{RESET}")
        elif choice == '4':
            if current_webhook_url:
                manage_webhook(current_webhook_url)
            else:
                print(f"{RED}[-] No webhook attached. Please attach a webhook first.{RESET}")
        elif choice == '5':
            print(f"{BLUE}[+] Thank you for using the program.{RESET}")
            break
        elif choice == '6':
            attach_run_webhook()
        else:
            print(f"{RED}Invalid option. Try again.{RESET}")

if __name__ == "__main__":
    main()
