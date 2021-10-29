month_conversion = {
    1: "Ocak",
    2: "Şubat",
    3: "Mart",
    4: "Nisan",
    5: "Mayıs",
    6: "Haziran",
    7: "Temmuz",
    8: "Ağustos",
    9: "Eylül",
    10: "Ekim",
    11: "Kasım",
    12: "Aralık"
}

print(month_conversion[1])
print(month_conversion[9])
print(month_conversion.get(5))
print(month_conversion.get(17, "Geçersiz anahtar!!!"))
