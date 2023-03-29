Pythone decoraterler:Decoraterler aslında birer warpaper dır.Fonksyonun davranşında,fonksyon çalışmadan önce veya çalışması esnansında belirli durumlarda belirlenen işlemleri yapmak için kullanılabilirler.Decoraterler herhangi bir sınıfın herhangi bir fonksyonunda işlem yapabilirler.Decoraterler içerisine parametre,değişkenler,liste türünde değişkenler alabilirler.Decoraterlerin farklı görevde olan biçok çeşidi vardır bunlardan bazıları:
@pytest.mark.parametrize():Test fonksiyonunu değişken parametrelerle kullanılmasını sağlar.
@pytest.fixture():Fixture testleri düzenler ve tekrar kullanılabilirliği sağlar.
@pytest.mark.xfail():Testin beklenen bir şekilde başarısız olması durumunda kullanılır.
@pytest.mark.skip():Bir testin belirli bir koşulda atlanması için kullanılır.
@pytest.mark.timeout():Bir testin belirli bir sürede tamamlanması gerektiği durumlarda kullanılır.Eğer belirtilen sürede test sonlanmaz ise testi sonlandırır.