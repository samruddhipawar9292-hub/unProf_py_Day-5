import re


def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


def extract_phone_numbers(text):
    pattern = r"(?:\+91[-\s]?)?[6-9]\d{9}"
    return re.findall(pattern, text)


def extract_dates(text):
    pattern = r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})\b"
    return re.findall(pattern, text)


def clean_text(text):
    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove extra blank lines
    text = re.sub(r"\n+", "\n", text)

    return text.strip()


def main():

    with open("sample_text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("=" * 60)
    print("TEXT INFORMATION EXTRACTOR")
    print("=" * 60)

    cleaned_text = clean_text(text)

    emails = extract_emails(cleaned_text)
    phones = extract_phone_numbers(cleaned_text)
    dates = extract_dates(cleaned_text)

    print("\n📧 Email Addresses")
    print("-" * 30)
    if emails:
        for email in emails:
            print(email)
    else:
        print("No email found.")

    print("\n📱 Phone Numbers")
    print("-" * 30)
    if phones:
        for phone in phones:
            print(phone)
    else:
        print("No phone number found.")

    print("\n📅 Dates")
    print("-" * 30)
    if dates:
        for date in dates:
            print(date)
    else:
        print("No date found.")

    print("\nSummary")
    print("-" * 30)
    print(f"Total Emails : {len(emails)}")
    print(f"Total Phones : {len(phones)}")
    print(f"Total Dates  : {len(dates)}")


if __name__ == "__main__":
    main()  
