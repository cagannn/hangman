import random
import os
import time
from pyfiglet import Figlet
hayvan=["Köpek","Koyun","Domuz","Keçi","Sığır","Kedi","Tavuk","Fare","Eşek","Ördek","Bufallo","At","Deve","Güvercin","Kaz","Lama","Kumru","Hindi","Tavşan","Kanarya","Tilki","Kirpi"]
bitki=["Domates","Kaktüs","Gül","Kenevir","Patates","Orkide","Mısır","Salatalık","Buğday","Lavanta","Palmiye","Ortanca","Ayçiçeği","Zambak","Soğan","Çilek","Fesleğen","Sarımsak","Avokado","Yasemin"]
alan=["_"]
kacinci_harf=[]
hata=0
yanlis=0
cevir=""
yedek_sozcuk=""
kaybettin=False 
take=0
bitir=True
yanlis_islem=False
while bitir: #Oyunun döngüsünü başlatıyoruz.
    f = Figlet(font='slant')
    print(f.renderText('ADAM ASMACA'))
    if take==0:#Menüye yönlendirecek olan sorgumuzu yapıyoruz.
        take=int(input("1.Başla\n2.Nasıl Oynanır\n"))

    if take==1:#Oyuncunun seçtiği şıkkı uyguluyoruz. Oyun Başladı.
        os.system('cls' if os.name=='nt' else 'clear')#Ekran temizlendi.
        type=input("Hangi alandaki kelimelerle oynamak istediğinizi yazınız:\nHayvan\tBitki\n").lower()
        if type=="hayvan": 
            kelime=random.choice(hayvan).lower() #Üsteki listemizden rastgele bir eleman seçtiriyoruz
        elif type=="bitki":
            kelime=random.choice(bitki).lower()
        elif type!="bitki" or "hayvan":                  #Girilen türün doğru yazılıp yazılmadığını sorguluyoruz.
            print("Lütfen doğru yazdığınızdan emin olun")      
            kelime=" "
            yanlis_islem=True                          
        if yanlis_islem==True: #Yanlış ise döngüyü sonlandırıyoruz.                           
                bitir=False
                break
        uzunluk=len(kelime)
        list_kelime=list(kelime) #Seçtiğimiz elemanı listeye çeviriyoruz ki girilen harfin doğruluğunu daha rahat kontrol edebilelim.
        for zed in range(uzunluk):#Seçilen elemanın iki kelimeden mi tek kelimeden mi oluştuğunu bulmak için bir döngü oluşturuyoruz.
            if kelime[zed]==" ":#Sorgumuzu yaptık.
                print("2 KELİMEDEN OLUŞMAKTADIR!!!!!!")
        for i in range(uzunluk-1):#Seçilen elamanın harf sayısı kadar "_"koymasını sağlıyoruz
            alan.append("_")
            
        for string in alan: #Liste formatında olan "_" lerimizi daha estetik durması için stringe çeviriyoruz.
            cevir=cevir+" "+string
        print(cevir)
        for l in range(1000):
            print(kelime)
            a=input("Bir harf sorgulayınız:").lower()#Karşıdan sorgulamak için harf istiyoruz .lower() fonksiyonunu büyük harf küçük harf problemi yaratmamsı için kullanıyoruz.
            for j in range(uzunluk):      #[
                if kelime[j]!=a:          #[  Girilen harfin rastgele seçilen elemanın içinde kaç kere olmadığına bakıyoruz eğer yoksa yanlis değişkenini artırıyoruz.
                    yanlis=yanlis+1       #[
                if kelime[j]==a:      
                    kacinci_harf.append(j) #[
                    for m in kacinci_harf: #[ Girilen harf eğer ki seçilen elemanın içinde varsa o dizindeki "_" işaretini eşleşen harfle değiştiriyoruz.
                        alan[m]=kelime[j]  #[



                if yanlis-uzunluk==0: #[  Yukarıda artırdığımız yanlis değişkeni eğer seçilen eleman uzunluğundaysa girilen değer seçilen elemanın içinde olmadığını gösteriyor.
                    hata=hata+1       #[    Bu yüzden hata değişkenini 1 artırıyoruz.


                if hata==1: #Hata sayısına göre asılan adamımızı çiziyoruz.
                    print("\n""\n""\n""\n""\n""\n""\n""\n""\n""-----")

                if hata==2:
                    print("\n""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""-----")

                if hata==3:
                    print("__________""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""-----")

                if hata==4:
                    print("__________""\n""  ""|""     |""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""-----")

                if hata==5:
                    print("__________""\n""  ""|""     |""\n""  ""|""     O""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""  ""|""\n""-----")

                if hata==6:
                    print("__________""\n""  ""|""     |""\n""  ""|""     O""\n""  ""|""     |""\n""  ""|""     |""\n""  ""|""\n""  ""|""\n""  ""|""\n""-----")

                if hata==7:
                    print("__________""\n""  ""|""     |""\n""  ""|""     O""\n""  ""|""    /|\\""\n""  ""|""     |""\n""  ""|""\n""  ""|""\n""  ""|""\n""-----")

                if hata==8:
                    print("__________""\n""  ""|""     |""\n""  ""|""     O""\n""  ""|""    /|\\""\n""  ""|""     |""\n""  ""|""    / \\""\n""  ""|""\n""  ""|""\n""-----")
                    kaybettin=True # Hata hakkı kalmadığı için kaybettin değişkenini True yapıyoruz.
            if alan==list_kelime:#Oyuncunun kelimeyi bulup bulmadığını sorguluyoruz
                x=input("Tebrikler kazandınız çıkmak için bir tuşa basınız...")
                time.sleep(1)
                os.system('cls' if os.name=='nt' else 'clear')
                bitir=False #while döngüsünü bitirmek için False yapıyoruz
                break       #for döngüsünden çıkmak için break komutunu giriyoruz
            if kaybettin==True: #Oyuncunun hakkı kalıp kalmadığını sorhuluoruz.
                y=input("Oyunu kaybettiniz tekrar deneyin...")
                time.sleep(3)
                os.system('cls' if os.name=='nt' else 'clear')
                bitir=False #while döngüsünü bitirmek için False yapıyoruz
                break       #for döngüsünden çıkmak için break komutunu giriyoruz
            
            yanlis=0 #Döngü tekrarlandığında problem olmaması için yanlis değerini 0'lıyoruz
            kacinci_harf=[] #Döngü tekrarlandığında problem olmaması için kacinci_harf list'ini boş yapıyoruz.
            for x in alan:                                 #[
                yedek_sozcuk=yedek_sozcuk+" "+x            #[ List'i stringe çeviriyoruz
                                                            
            print(yedek_sozcuk)                            #[List'i stringe çevirmek için kullandığımız değeri ekrana veriyoruz.
            yedek_sozcuk=" "                               #[Stringi boş yapıyoruz.
            


    if take ==2:
        os.system('cls' if os.name=='nt' else 'clear')
        nasil = Figlet(font='eftitalic')
        print(f.renderText('Nasıl Oynanir?'))
        print("Bilgisayar seçtiğiniz katagoride bir kelime belirleyecek.\nSiz de bilgisayara harf önererek bilgisayarın seçtiği kelimeyi bilmeye çalışacaksınız\nama dikkat adamımızı dar ağacında sallanmadan önce kelimeyi tahmin etmeyi unutmayın.\nOnun da ailesi ve çocukları var :(\nBoşluk da bir karakter sayılıyor!!!!!!")
        devam=input("Geri gitmek için bir tuşa basınız...")
        take=0 #Ana menüye geri dönmek için take değişkenini 0'lıyoruz
        os.system('cls' if os.name=='nt' else 'clear')
    