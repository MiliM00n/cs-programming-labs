fullname = input()
surname, name, patronymic = fullname.split()
surname_formatted = surname.capitalize()
initials = name[0].upper() + ". " + patronymic[0].upper() + "."
print(f"{surname_formatted} {initials}")
