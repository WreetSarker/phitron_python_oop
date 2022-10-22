import uuid
new_id = uuid.uuid1()
name = input("Enter student's name': ")
mark = float(input("Enter student's mark: "))

with open(f"{name}_{new_id}_info.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Marks:{mark}")