phone = input()
cleaned = phone.replace("+", "").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(cleaned)
