decimal = input("請輸入0~255的任一數字")
decimal = int(decimal)
binary = []
i = 7
while 0 <= decimal and decimal <= 255:
    if i == -1:
        break
    if decimal >= 2**i:
        binary.append(1)
        decimal -= 2**i
        i -= 1
        continue
    if decimal < 2**i:
        binary.append(0)
        i -= 1
q = 0
while q>=0 and q<=7:
    if binary[q] == 1:
        print("二進位 = ",*binary[q:8],sep="")
        break
    if binary[q] == 0:
        q += 1

hex1 = binary[0] * 2**3 + binary[1] * 2**2 + binary[2] * 2**1 + binary[3] * 2**0
hex2 = binary[4] * 2**3 + binary[5] * 2**2 + binary[6] * 2**1 + binary[7] * 2**0
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
if hex1 == 10:
    hex1 = A
if hex1 == 11:
    hex1 = B
if hex1 == 12:
    hex1 = C
if hex1 == 13:
    hex1 = D
if hex1 == 14:
    hex1 = E
if hex1 == 15:
    hex1 = F
if hex2 == 10:
    hex2 = A
if hex2 == 11:
    hex2 = B
if hex2 == 12:
    hex2 = C
if hex2 == 13:
    hex2 = D
if hex2 == 14:
    hex2 = E
if hex2 == 15:
    hex2 = F

hex = [hex1, hex2] 
print("十六進位 = ",*hex,sep="")
 
