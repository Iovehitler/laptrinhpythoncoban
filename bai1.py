try
So = int(input("Nhap so: "))
if So % 2 == 0:
    print(f"{So} la so chan")
else:
    print(f"{So} la so le")
thang_31 = [1, 3, 5, 7, 8, 10, 12]

m = int(input("Nhập số tháng (1-12): "))

if m in thang_31:
    print(f"Tháng {m} có 31 ngày.")
elif m == 2:
    print("Tháng 2 có 28 hoặc 29 ngày.")
else:
    print(f"Tháng {m} có 30 ngày.")