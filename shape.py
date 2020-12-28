
pi = 3.1415  #pi sayısı

class Şekil():
    def __init__(self,şekiladı,kenar1):
        self.şekiladı = şekiladı
        self.kenar1 = kenar1
        print("Bu şekil bir {}dir.".format(self.şekiladı))


class ÇeşitkenarUcgen(Şekil):
    def __init__(self,şekiladı,kenar1,kenar2,kenar3):
        self.şekiladı = şekiladı
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.kenar3 = kenar3

    def cevrebulma(self,kenar1,kenar2,kenar3):
        print(self.kenar1 + self.kenar2 + self.kenar3)  # (a+b+c)

    def alanbulma(self,kenar1,kenar2,kenar3):   
        s = (self.kenar1 + self.kenar2 + self.kenar3)/2
        print((s*(s-self.kenar1)*(s-self.kenar2)*(s-self.kenar3))**(1/2))   # s*(s-a)*(s-b)*(s-c) nin karekökü


class Dikdortgen(Şekil):
    def __init__(self,şekiladı,kenar1,kenar2):
        self.şekiladı = şekiladı
        self.kenar1 = kenar1
        self.kenar2 = kenar2
    def cevrebulma(self,kenar1,kenar2):
        print(2*(self.kenar1 + self.kenar2))  #2*(a+b)

    def alanbulma(self,kenar1, kenar2):
        print(self.kenar1 * self.kenar2) #2*a*b

class Kare(Şekil):
    def cevrebulma(self,kenar1):
        print(4 * self.kenar1)  # 4 kenar

    def alanbulma(self,kenar1):
        print(self.kenar1**2) # a kare

class EşkenarUcgen(Şekil):
    def cevrebulma(self,kenar1):
        print(3 * self.kenar1)     #3 kenar
    def alanbulma(self,kenar1):
        print((self.kenar1**2)*(3**(1/2))/4)  #a karekök 3 bölü 4

class Daire(Şekil):
    def cevrebulma(self,yaricap):
        yaricap = self.kenar1   #yariçap bir değişkendir.
        print(2* pi * yaricap)  # 2 pi r

    def alanbulma(self, yaricap):
        print(pi*(yaricap**2)) #  pi r kare


#Dikdörtgen objesi oluşturup, class ta tanımlı fonksiyonlara erişmek
Dikdortgen1 = Dikdortgen("Dikdörtgen",5,20)
Dikdortgen1.cevrebulma(5,20)
Dikdortgen1.alanbulma(5,20)

#Kare objesi oluşturup, class ta tanımlı fonksiyonlara erişmek
Kare1 = Kare("Kare",10)
Kare1.cevrebulma(10)
Kare1.alanbulma(10)

#Daire objesi oluşturup, class ta tanımlı fonksiyonlara erişmek
Daire1 = Daire("Daire",5)
Daire1.cevrebulma(5)
Daire1.alanbulma(5)

#Eşkenar Üçgen objesi oluşturup, class ta tanımlı fonksiyonlara erişmek
EskenarUcgen1 = EşkenarUcgen("Eşkenar Üçgen",10)
EskenarUcgen1.cevrebulma(10)
EskenarUcgen1.alanbulma(10)

#Çeşitkenar Üçgen objesi oluşturup, class ta tanımlı fonksiyonlara erişmek
ÇeşitkenarUcgen1 = ÇeşitkenarUcgen("Çeşitkenar Üçgen",5,12,13)  # 5,12,13 aynı zamanda bir dik üçgen
ÇeşitkenarUcgen1.cevrebulma(5,12,13)
ÇeşitkenarUcgen1.alanbulma(5,12,13)
