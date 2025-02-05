import os
import re

def list_txt_files():
    return [f for f in os.listdir('.') if f.endswith('.txt')]

def print_error(message):
    print(f"\033[91m{message}\033[0m")

def main():
    try:
        print("What file do you want to clean ?")
        txt_files = list_txt_files()
        if not txt_files:
            print_error("No file .txt found here.")
            input("Press Enter to exit.")
            return

        for idx, file_name in enumerate(txt_files, 1):
            print(f"{idx}- {file_name}")

        try:
            choice = int(input("Enter the numero of the file : "))
            if choice < 1 or choice > len(txt_files):
                raise ValueError("Invalid choice.")
            file_to_clean = txt_files[choice - 1]
        except ValueError as e:
            print_error(f"Error : {e}")
            input("Press Enter to exit.")
            return

        print("Enter the words or phrases to delete (separated by commas):")
        user_input = input().strip()
        patterns = [item.strip() for item in user_input.split(',')]

        with open(file_to_clean, 'r', encoding='utf-8') as file:
            content = file.readlines()

        pattern = '|'.join([re.escape(item) for item in patterns])
        text = ''.join(new_content)
        cleaned_content, num_subs = re.subn(pattern, '', text, flags=re.IGNORECASE)
        with open(file_to_clean, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Cleaning completed for file:{file_to_clean}")
        print(f"\033[1m{num_subs} occurrences deleted.\033[0m")
        print(f"\033[1m{lines_removed} lines deleted.\033[0m")

    except Exception as e:
        print_error(f"An error has occurred: {e}")

    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
