ogrenciler =[]
def addStudent(nameAndSurname ):
    ogrenciler.append(nameAndSurname)
    print("{addstudent} adlı öğrenci listeye eklendi".format(addstudent=nameAndSurname))
def deleteStudent(nameAndSurname):
    ogrenciler.remove(nameAndSurname)
    print("{delstudent} adlı öğrenci listeden silindi".format(delstudent=nameAndSurname))
def addStudents(nameAndSurname=[]):
    for ogr in nameAndSurname:
        ogrenciler.append(ogr)
        print("{addstudent} adlı öğrenci listeye eklendi".format(addstudent=ogr))
def deleteStudents(nameAndSurname=[]):
    for ogr in nameAndSurname:
        ogrenciler.remove(ogr)
        print("{delstudent} adlı öğrenci listeden silindi".format(delstudent=ogr))        
def getStudents():
    for ogr in ogrenciler:
      print(ogr)
def getNumberStudent(nameAndSurname):
    sayac=0
    for ogr in ogrenciler:
        if ogr==nameAndSurname:
            return sayac
        else:
            sayac+=1
#1 Öğrenci ekleme kısmı
newOgrName=input("Eklemek istediğiniz öğrencinin adını yazınız")
addStudent(newOgrName)
for ogr in ogrenciler:
    print(ogr)
print(ogrenciler)
#1 Öğrenci silme kısmı
delOgrName=input("Silmek istediğiniz öğrencinin adını yazınız")
deleteStudent(delOgrName)
for ogr in ogrenciler:
    print(ogr)
#Birden fazla Öğrenci ekleme kısmı
print("Eklemek istediğiniz öğrencilerin adlarını yazınız son oğrenciyi arkleyince 1 rakamını giriniz tuşuna basınız" )
kon="0"
addOgr=[]
while(kon=="0"):
    name=input()
    if name=="1":
        kon=name
    else:
         addOgr.append(name)
addStudents(addOgr)
for ogr in ogrenciler:
    print(ogr)
#birden fazla Öğrenci Silme kısmı
print("Silmek istediğiniz öğrencilerin adlarını yazınız son oğrenciyi arkleyince 1 rakamını giriniz tuşuna basınız" )
kont="0"
delOgr=[]
while(kont=="0"):
    name=input()
    if name=="1":
        kont=name
    else:
        delOgr.append(name)
deleteStudents(delOgr)
for ogr in ogrenciler:
    print(ogr)

#Öğrencileri listeleme kısmı
getStudents()
#Öğrenci numarası öğrenme kısmı
ogrname=input("Numarasını öğrenmek istediğiniz öğrenicnin adını ve soyadını giriniz giriniz")
ogrNo=getNumberStudent(ogrname)
print("{ogrname} isimli öğrencinin numarası {ogrNo}".format(ogrname=ogrname,ogrNo=ogrNo))


