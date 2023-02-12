rows = int(input("ป้อนจำนวนแถว: "))
cols = int(input("ป้อนจำนวนหลัก: "))

print("Matrix ขนาด",rows,"x",cols)
matrix1 = []
print("ค่าสำหรับ Matrix ที่ 1")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("ป้อนค่าแถว {0} , หลัก {1}: ".format(i+1, j+1)))
        row.append(val)
    matrix1.append(row)

matrix2 = []
print("ค่าสำหรับ Matrix ที่ 2")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("ป้อนค่าแถว {0} , หลัก {1}: ".format(i+1, j+1)))
        row.append(val)
    matrix2.append(row)

op = input("ป้อนการคำนวณ (+, -, หรือ *): ")

result = []
if op == "+":
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
elif op == "-":
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
elif op == "*":
    for i in range(rows):
        row = []
        for j in range(cols):
            val = 0
            for k in range(cols):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)

print("ผลลัพธ์:")
for row in result:
    print(row)
