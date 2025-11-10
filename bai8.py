
can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi"]


nam_duong = int(input("Nhập năm dương lịch: "))

can_index = nam_duong % 10
chi_index = nam_duong % 12

nam_am_lich = can[can_index] + " " + chi[chi_index]


print(f"Năm {nam_duong} là năm âm lịch: {nam_am_lich}")
