def calculator():
    print("kalkulator programi")
    print("İşlem Seçin: 1. Toplama 2. Çıkarma 3. Çarpma 4. Bölme")

    secim = input("Bir secim daxil edin (1/2/3/4:) ")
        
    num1 = float(input("Birinci ededi daxil edin:"))
    num2 = float(input("Ikinci ededi daxil edin:"))

    if secim =="1":
        print(num1+num2)
    elif secim =="2":
        print(num1-num2)
    elif secim =="3":
        print(num1*num2)
    elif secim =="4":
        if num2 != 0:
            print(num1/num2)
        else:
            print("0-a bolmek olmaz")
    else:
        print("Xeta")
          
if __name__ == "__main__":
    calculator()