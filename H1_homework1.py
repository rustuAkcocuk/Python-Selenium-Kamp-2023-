#1.Ödev
#str:Metinsel string ifadeleri barındırabilen değişkenlerin veri tipleridir.
#Sayısal tipler: Sayısal ifadeleri barındırabilen değişkenlerin veri tipleridir.3 tip vardır. int,float ve complex dir.
#int : 11,30,100 gibi tam sayıları tutabilen veri tipidir.
#float: 3.4,15.7,101.9 gibi küsüratlı sayıları tutabilen veri tipleridir.
#complex: 1i,27i,95i gibi compleks(sanal) sayıları tutabilen veri tipidir.
#diziler:Bir değişkenin içine aynı tipte birden fazla değer atma (liste oluşturma)durumudur.3 tipi vardır.list,tuple,range dir.
#list:Köşeli parantezler arasına sırası ile aralarına virgül konularak tanımlanan liste dir.
#tuple:Yay parantezler arasına sırası ile aralarına virgül konularak tanımlanan liste dir.
#range:Girilen değerler arasında sayısal bir liste oluşturur fakat son değeri dahil etmez.Bu listenin artış miktarını belirleyebilirsiniz.Kullanımı:range(0,22,2).
#adresleme:Bir anahtar kullanrak değerleri bir değişken içinde toplamak.Anahtar kullanılarak içindeki değerler değiştirilebilir.
#dict:İngilizcedeki sözlük (dictionary) nin kısaltması olarak kullanılıar.Değişken adı={"anahtar":"değer"} ve değerler arasına virgül konularak kullanılır.
#küme tipleri:Küme tipleri değiştirilebilen ve değiştirilemeyen olmak üzere 2 ye ayrılır.Değiştirilebilir kümeler set,değiştirilemez ise frozenset dir.
#set:list değişken tipinin süslüparantezler ile kullanılmış halidir.Set komutu ile alfabetik olarak veya küçükten büyüğe sıralanabilir.remove(değer) komutu ile girilen veriyi silinebilir.
#frozenset:set veri tipinin değiştirlemez (veri eklenemeze,çıkarılamaz) halidir.
#bool:Mantıksal bir türde doğrulama yapma amacı güdülür.True veya False değerlerinden birini alır.
#Binary veri tipleri:Girilen her veri tipini binary sisteme çevirerek bunun karşılığını tutar.3 türü vardır.Bytes,bytearray ve memoryview dir.
#bytes: İçerisine sadece binary sistemdeki veriler atılabilir veya içerisine bir veri atılarak binary karşılığı da tutulabilir.
#bytearray:byte veri tipinde oluşturulan veriler üzerinde değişiklik yapmak için kullanılır.
#memoryview:Pythone da bellek durumunu görüntülemek için kullanılır.
#2.Ödev
courseName="(2023) Yazılım Geliştiric Yetiştirme Kampı-Pyto-hon&Selenium" #Kurs aldarı str veri tipinde tutulan değişkenler
instructorName="Halit Enes Kalaycı" #Eğitmen adı str veri tipinde tutlan değişkenler
completionPercentage=100 #Kursun tamalanma yüzdesi float veri tipinde tutulan bir değişken
#3.Ödev
#Kurs Katagorisi veya Kurs eğitmenleri seçildğinde şart blokları ile seçilen kategorie veya eğitmene göre kurslar gösterilir
category="Programlama"
instructor="Halit Enes Kalaycı"

if category=="Programlama":
 print(category) #Programlama kategorisine ait kursları getir.
elif category=="Grafik Tasarım":
 print(category) #Grafik Tasarım kategorisine ait kursları getir.
else :
  print("Bütün kategorideki eğitimleri getir") 


if instructor=="Engin Demirog":
 print(instructor) #Eğitmeni Engin Demirog olan kursları getir.
elif instructor=="Halit Enes Kalaycı":
 print(instructor) #Eğitmeni Halit Enes Kalaycı olan kursları getir.
else:
 print("Bütün eğitmenlere ait eğitimleri getir")


