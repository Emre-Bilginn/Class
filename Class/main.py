class personel:
    def __init__(self, adi ,departmani ,calisma_yili ,maas) :
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maas = maas

kisi1 = personel("Ahmet","İnsan Kaynakları",10,25000)
kisi2 = personel("Mehmet","Güvenlik",2,20000)
kisi3 = personel("Ayşe","Satış ve Pazarlama",8,32000)
kisi4 = personel("Emre","Yazılım",5,50000)

class firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self,person):
        self.personel_listesi.append(person)
    
    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adi : ",personel.adi)
            print("Departmanı : ",personel.departmani)
            print("Çalışma Yılı : ",personel.calisma_yili)
            print("Maaş : ",personel.maas)
            print()

    def maas_zammi(self, person, zam_orani):
        yeni_maas = person.maas + (person.maas*zam_orani)/100
        person.maas = int(yeni_maas)
        print(person.adi,"isimli personelin yeni maaşı",int(yeni_maas))
        print()
    
    def personel_cikart(self, person):
        ad = person.adi
        self.personel_listesi.remove(person)
        print(person.adi, "adlı kişi listeden silindi.")
        print()


firma1 = firma()
firma1.personel_ekle(kisi1)
firma1.personel_ekle(kisi2)
firma1.personel_ekle(kisi3)
firma1.personel_ekle(kisi4)

firma1.personel_listele()
firma1.maas_zammi(kisi2,25)
firma1.personel_listele()
firma1.personel_cikart(kisi3)
firma1.personel_listele()