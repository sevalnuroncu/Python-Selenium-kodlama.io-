**HTML (Hyper Text Markup Language)**

Web sayfalarında gördüğümüz iskelet yapısını oluşturmak için kullanılan metin işaretleme dilidir.
Bir programlama dili değildir.

**HTML LOCATORS**

Bir web sayfasındaki bir html ögesini tanımlamanın yoludur. Html ögesi bazı özelliklere(class, name vb.) sahiptir. Bu özelliklere bakarak htmldeki ögelerin konumunu öğrenebiliriz. Bu html konum bilgileri sayesinde selenium web sitesi ile iletişime geçmiş olur. Ama bunu yaparken unique html özelliklerini öncelikli tutmalıyız. Çünkü birden fazla aynı özellikte öge varsa istediğimiz ögeye erişemeyebiliriz.

**SELENIUM'DA AKSİYONLAR**

Html elemantlerine ne yapmasını anlattığımız fonksiyonlardır diyebiliriz. Actions classının nesnesi ile erişilirler.

click(): istediğimiz web elemente tıklar

clickAndHold(): istediğimiz web elemente basılı bekler

contextClick(): sağ tıklama

doubleClick(): çift tıklama

dragAndDrop(source, target): istediğimiz web elementi alıp istediğimiz başka bir elementin üzerine bırakır.

sendKeys():parametre olarak hangi tuşu girersek o tuşa bir kere basar. ("a","e", Keys.TAB, Keys.ENTER)

keyDown(): bir tuşa basılı tutma

keyUp():Basılı tuttuğumuz tuştan elimizi kaldırma

perfom(): istediğimiz methodlar bittiğinde sona perfom() metodunu eklemek gerekir yoksa çalışmaz.
