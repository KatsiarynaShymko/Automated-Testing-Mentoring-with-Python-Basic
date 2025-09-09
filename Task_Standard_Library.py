import os
import json
from datetime import datetime, date

today = date.today()

file_name = 'json_program1.json'

if os.path.exists(file_name):
    with open("json_program1.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        new_list = []
        for person in data:
            dob = person.get('birth_date')
            birth_datetime = datetime.strptime(dob, "%Y-%m-%d")
            birth_date = birth_datetime.date()
            person_age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                person_age -= 1
            if person_age < 18:
                new_list.append(person)
        for row in new_list:
            print(row)
else:
    print('File does not exist')
