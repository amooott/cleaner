import os
import re

def list_txt_files():
    """Liste les fichiers .txt dans le dossier courant."""
    return [f for f in os.listdir('.') if f.endswith('.txt')]

def print_error(message):
    """Affiche un message d'erreur en rouge."""
    print(f"\033[91m{message}\033[0m")  # Code ANSI pour le rouge

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

        # Demander à l'utilisateur les mots ou expressions à supprimer
        print("Enter the words or phrases to delete (separated by commas):")
        user_input = input().strip()
        patterns = [item.strip() for item in user_input.split(',')]

        # Nettoyage du fichier
        with open(file_to_clean, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # Suppression des lignes commençant par "🇲🇦" et autres conditions
        new_content = []
        lines_removed = 0
        for line in content:
            # Supprimer les lignes qui commencent par "🇲🇦"
            if line.startswith("🇲🇦"):
                lines_removed += 1
                continue
            # Suppression des lignes commençant par "hit by" ou des phrases spécifiques
            if re.match(r'^\s*hit by', line, flags=re.IGNORECASE) or \
               re.match(r'^\s*🇲🇦💎====== HIT By MANZERA AYENNA ======💎🇲🇦\s*$', line, flags=re.IGNORECASE) or \
               re.match(r'^\s*🔥🔥===== Telegram:', line, flags=re.IGNORECASE):
                lines_removed += 1
                continue
            # Ajout de la ligne nettoyée à la nouvelle liste
            new_content.append(line)

        # Construction du pattern de suppression basé sur l'entrée utilisateur
        pattern = '|'.join([re.escape(item) for item in patterns])
        text = ''.join(new_content)
        cleaned_content, num_subs = re.subn(pattern, '', text, flags=re.IGNORECASE)

        # Écriture du contenu nettoyé dans le fichier
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
