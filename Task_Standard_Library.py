import json
import os
from datetime import date, datetime
from json import JSONDecodeError

today = date.today()

PERSON_DATA_FILE = "json_program1.json"


def age_calculation(dob):
    """
    Calculates age based on the date of birth.
    :param dob: Date of birth in YYYY-MM-DD format.
    :return: Age as integer or None if format is invalid.
    """
    try:
        birth_datetime = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {dob}")
        return None
    birth_date = birth_datetime.date()
    person_age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        person_age -= 1
    return person_age


def main():
    """
    Main program execution logic.
    """
    if os.path.exists(PERSON_DATA_FILE):
        try:
            with open(PERSON_DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File is not found")
        except JSONDecodeError:
            print("There are issues with JSON file")
        else:
            new_list = []
            for person in data:
                dob = person.get("birth_date", "")
                person_age = age_calculation(dob)
                if person_age is not None and person_age < 18:
                    new_list.append(person)
            for row in new_list:
                print(json.dumps(row, ensure_ascii=False, indent=2))
    else:
        print("File does not exist")


if __name__ == "__main__":
    main()
