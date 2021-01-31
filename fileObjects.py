with open(r"notlar.txt", 'r') as f:
    # print(f.read()) #fakat bu, tüm dosyayı bir anda okuyacak. Hafızada sıkıntı yaratabilir.
    harf_sayısı = 100
    dosya_içeriği = f.read(harf_sayısı)#her seferinde belirlenen harf sayısı kadar okuyacak. 
    while (len(dosya_içeriği) > 0):
        print(dosya_içeriği, end='')
        dosya_içeriği = f.read(harf_sayısı)
print('')
