# 1) taskınız ilk olaraq bir text faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız .
# 2) daha sonra həmin textin ilk sətrindəki  sözlərin bütün hərflərini böyük hərflərə çeviririk .
# 3) Ən sonda bu sözləri başqa  bir text faylı yaradıb onun içərisində yazırıq.

with open("cumle.txt",encoding="utf-8",mode="r") as data:
    mezmun=data.readline().upper()
    print(mezmun)
    data.close()

with open("yeni_cumle.txt",encoding="utf-8",mode="w") as yeni_data:
    yeni_data.write(mezmun)
    data.close()
