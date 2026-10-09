text = input()
count = 0

for word in text.split():
    cleaned = word.strip(".,!?;:").lower()
    if not cleaned or "ра" not in cleaned:
        continue
    print(cleaned)
    count += 1

if count == 0:
    print("Нет совпадений")
print(f"Количество: {count}")
