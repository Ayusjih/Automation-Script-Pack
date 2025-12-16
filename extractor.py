import re
import os

def extract_data():
    print("\n--- Data Extraction Tool (Regex) ---")
    file_path = input("Enter the path of the .txt file to scan: ").strip()

    if not os.path.exists(file_path):
        print("Error: File not found.")
        return

    # Defined Regex Patterns (from requirements)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d{1,2}[- ]?)?\d{10}'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find all matches
        emails = re.findall(email_pattern, content)
        phones = re.findall(phone_pattern, content)

        # Save results to output files
        with open("emails.txt", "w") as e_file:
            e_file.write("\n".join(emails))
            
        with open("phones.txt", "w") as p_file:
            # Phone matches might return tuples depending on groups, 
            # so we ensure we grab the full match if needed or join them.
            # Ideally, we clean the list before writing.
            cleaned_phones = [p[0] if isinstance(p, tuple) else p for p in phones]
            p_file.write("\n".join(str(p) for p in phones)) # simple dump for now

        print(f"\nExtraction Complete!")
        print(f"Found {len(emails)} emails -> Saved to emails.txt")
        print(f"Found {len(phones)} phone numbers -> Saved to phones.txt")

    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    extract_data()