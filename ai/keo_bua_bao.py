import random

# Yeu cau:
# Trong chuong trinh nay nguoi lap trinh vien duoc yeu cau viet mot chuong trinh oan tu ti
# 1. Nguoi choi co the tra loi bang cach nhap vao ban phim 'keo', 'bua', 'bao'
# 2. Chuong trinh lay thong tin nguoi choi va in ra man hinh luot di cua may tinh
# 3. Neu nguoi choi chien thang, in ra man hinh 'Ban da thang!' (chu B viet hoa)
# 4. Neu nguoi choi thua cuoc, in ra man hinh 'Ban da thua!' (chu B viet hoa)
# 5. Neu hoa, in ra man hinh 'Hoa roi!' (chu H viet hoa)
print("Chung minh cung choi oan tu ti nhe!")

random_number = random.randint(
    0, 2
)  # lenh randint(0, 1) tra ve 1 trong 3 so 0, 1, 2 mot cach ngau nhien
if random_number == 0:
    computer_choice = "keo"
elif random_number == 1:
    computer_choice = "bua"
else:
    computer_choice = "bao"

# Goi y:
# so sanh du lieu nguoi dung nhap vao voi bien computer_choice:  
# trong nhung truong hop nao thi may tinh va nguoi choi hoa nhau?
# trong nhung truong hop nao thi nguoi choi thang?
# trong nhung truong hop nao thi may tinh thang?
#
# TODO: Hoc sinh chi duoc lap trinh tu dong lenh nay tro xuong
player_choice = input("Ban ra gi? ")
print("May tinh ra", computer_choice)

if player_choice == computer_choice:
    print("Hoa roi!")
elif (computer_choice == 'keo' and player_choice == 'bua') or (computer_choice == 'bua' and player_choice == 'bao') or (computer_choice == 'bao' and player_choice == 'keo'):
    print("Ban da thang!")
else:
    print("Ban da thua!")
      