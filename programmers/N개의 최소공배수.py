def gcm(a, b):
    if b == 0:
        return a
    else:
        return gcm(b, a % b)


arr = [2, 6, 8, 14]
lcd_num = arr[0]
mul_num = arr[0]

for i in range(1, len(arr)):
    mul_num *= arr[i]
    lcd_num = mul_num // gcm(lcd_num, arr[i])
    mul_num = lcd_num

print(lcd_num)
