toplam = []
tutar =0
odenecek =0
while True:
    for i in range (1,99999999):
        girilen = int(input(f"{i}. ürün fiyatını girin(Bitirmek için 0 girin): "))
        if girilen == 0:
            break
        else:
            toplam.append(girilen)
    tutar = sum(toplam)

    if tutar >1500:
        odenecek = tutar - (tutar * 0.05)
        print(f"ödenecek tutar = {odenecek}")
    elif tutar <=1500:
        print(f"odenecek tutar = {tutar}")
    break