print("=== ЧТЕНИЕ ОТЧЕТА С ДИСКА ===")

with open("daily_report.txt","r", encoding="utf-8") as f:

    lines = f.readlines()

print(f"Всего строк в файле: {len(lines)}\n")


for line in lines:
    clean_line = line.strip()
    print(f">>{clean_line}")