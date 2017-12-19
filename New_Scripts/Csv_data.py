import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile


def get_row(filepath):
    with open(filepath, "r") as csvfile:
        reader = csv.reader(csvfile)
        length = list(reader)
        return len(length)


def append_data(filepath, name, email):
    fieldnames = ["id", "name", "email"]
    row = get_row(filepath)
    with open(filepath, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow({
            "id": row,
            "name": name,
            "email": email,
        })


#append_data("data.csv", "kuldip", "kkvkicktheworldup7@gmail.com")


def read_csv(id=None, email=None):
    filename = "data.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        unkown_id = None
        unkown_email = None
        for row in reader:
            if id is not None:
                if int(row.get("id")) == id:
                    return row
                else:
                    unkown_id = id
            if email is not None:
                if row.get("email") == email:
                    return row
                else:
                    unkown_email = email
        if unkown_id is not None:
            return "User id {id} is unkown".format(id=id)
        if unkown_email is not None:
            return "email {email} is unkown".format(email=email)
    return None

print(read_csv(id=5))


def edit_csv(sent, id=None):
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "rb") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ["id", "name", "email", "item", "sent"]
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if id is not None:
                if int(row["id"]) == id:
                    row["sent"] = sent
            writer.writerow(row)
        shutil.move(temp_file.name, filename)

#edit_csv(False, id=5)
