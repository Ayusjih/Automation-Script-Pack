import sys
import file_renamer
import extractor
import email_sender

def main_menu():
    while True:
        print("\n==============================")
        print("   AUTOMATION SCRIPT PACK     ")
        print("==============================")
        print("1. File Renamer")
        print("2. Data Extraction (Regex)")
        print("3. Email Automation (SMTP)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            file_renamer.rename_files()
        elif choice == '2':
            extractor.extract_data()
        elif choice == '3':
            email_sender.send_email()
        elif choice == '4':
            print("Exiting Automation Pack. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main_menu()