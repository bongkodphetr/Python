import math

print("โปรแกรมคำนวณพื้นที่รูปทรง")
print("1. สามเหลี่ยม")
print("2. วงกลม")
print("3. สี่เหลี่ยม")

choice = int(input("เลือกหาพื้นที่ของรูปทรงหมายเลข: "))

if choice == 1:
    base = float(input("ป้อนความยาวฐาน: "))
    height = float(input("ป้อนความสูง: "))
    area = 0.5 * base * height
    print("พื้นที่ของสามเหลี่ยม = ", area)

elif choice == 2:
    radius = float(input("ป้อนความยาวรัศมี: "))
    area = math.pi * radius ** 2
    print("พื้นที่ของวงกลม = ", area)

elif choice == 3:
    length = float(input("ป้อนความยาวด้าน: "))
    width = float(input("ป้อนความกว้าง: "))
    area = length * width
    print("พื้นที่ของสี่เหลี่ยม = ", area)

else:
    print("เลือกหมายเลขไม่ถูกต้อง")

