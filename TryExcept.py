
# print(10/0) Eğer bu satırı yorum yapmasaydık program direkt olarak hata alırdı ve geri kalan komutlara
# bakmadan sonlanırdı.
try:
    #print(10/0)
    num = float(input("Enter a number: "))
except ZeroDivisionError:
    print("0'a bölme hatası")
except ValueError as err:
    # print("Geçersiz Input")
    print(err)

print("Hello")