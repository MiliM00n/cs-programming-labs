a = float(input())
b = int(input())

if a <= 0 or b < 0 or b > 120:
    print("Ошибка")
elif b <= 5:
    print(f"Стоимость: {a * 0:.2f} руб")
elif b <= 17:
    print(f"Стоимость: {a * 0.5:.2f} руб")
elif b <= 59:
    print(f"Стоимость: {a * 1.0:.2f} руб")
else:
    print(f"Стоимость: {a * 0.7:.2f} руб")