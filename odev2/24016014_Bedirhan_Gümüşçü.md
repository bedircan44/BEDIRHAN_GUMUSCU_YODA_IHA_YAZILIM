İHANIN GÜNLÜK KULLANIM ALANLARI
- YEMEK SERVİSİ (KURYELİK)
- UZUN BİNALAR VE CAMLI YAPILARDA DIŞ TEMİZLİK
-BELLİ BİR ALANI 3D MODELDE ÇIKTISINI ALMAK
- ARAMA KURTARMA

İHA TÜRLERİ 2 TEMEL SINIF
-MULTİROTOR
-SABİT KANATLI


 MULTİROTOR(DÖNERKANAT)
BİRDEN FAZLA MOTOR (TRİCOPTER,HEXACOPTER...)
MOTOTR SAYISI İTKİYİ BELİRLER...
DRONENUN AĞIRLIĞININ 2 KATI İTKİ DAHA HIZLI GİTMESİ İÇİN.

  SABİTKANATLI İHA
 ASIL İSTENEN UZUN MESAFEDE UÇABİLMEK.
PİSTE İHTİYAÇ DUYAR.


MULTİROTOR İHA NASIL ÇALIŞIR?(DÖNERKANAT)

MOTORLARIN FARKLI DEVİRLERDE CALISMASINA GÖRE HAREKETİ BELİRLENİR.
YAW SAĞ SOL
ROLL YANAL EKSENDE HAREKET
PITCH ÖNE ARKAYA
LİFT<WEİGHT--DRONE SABİT KALIR (buna bak)
LİFT=WEİGHT-- YERDEYSE KALKMAZ HAVADA İSE SBT KALIR(HOWERİNG)
LİFT>WEİGHT--DRONE YÜKSELİR


SABİT KANATLI NASIL ÇALIŞILIR(FİXED-WİNG)
ANLATMADI :d


  İHA MİMARİSİ: TEMEL BİLEŞENLER

1COMPANİON COMPUTER:KOD ÇALIŞTIRMA/GÖREV BİLGİSAYARI İHANIN İÇİNDE
  2FLİGHT CONTROLLER:VERİLEN VERİYİ İŞLİYOR. DRONUN STABİL OLMASINI SAĞLIYOR
 3 TELEMETRY SYSTEM:iha ile yer istasyonu arasındaki iletişimi sağlar
4 SENSORS:GPS/KAMERA/(HEPSİ FLİGHT KONTROLE BAGLI)
5 GROUND CONTROL STATİON: ADINDAN BELLİ


  MOTORLAR
 DÖRT HANELİ RAKAM ANLAMI= İLK İKİ RAKAM GENİŞLİK SON İKİ RAKAM YÜKSEKLİK
KV = HER 1 VOLT BAŞINA YÜKSÜZ DAKİKADA KAÇ DEVİR(RPM) DÖNECEĞİNİ İFade eder.
UZUN SÜRELİ UÇAN DRONELARDA DÜŞÜK KV TERCİH EDİLİR.

MOTOR SEÇİMİ VERİMLİLİĞE VE GÜVENLİ SINIRLAR İÇİNCDE YAPILIR.

ESC TANIMI VE ÇALIŞMA PRENSİBİ
ELEKTRONİK HIZ KONTROLCÜ(ESC) BATARYADAN GELEN AKIMI(DC) MOTORUN DÖNMESİ SONUCUNDA ÜÇ FAZLI ALTERNATİF AKİMA (AC) DÖNÜŞÜR.


FLİGHT CONTROLLER;
UÇUŞ KONTROL CİHAZI(FC), TEMEL UÇUŞ DİNAMİĞİNİ YÖNETİR VE ENTEGRE SENSÖRLERDEN(GPS,LIDAR,AİRSPEED,BAROMETRE,MAGNETOMETRE) GELN TÜM VERİLER SAYESİNDE EKF GİBİ YAZILIMLARLA İHA ANLIK DURUMA KARAR VERİR.
-STABİLİZASYON
-NAVİGASYON
-MOTOR YÖNETİMİ
- GÜVENLİK PROTOKOLLERİ : ACİL DURUM İNİŞLER
 VE FAİLSAFE

    SENSÖRLER
LİDAR/RADAR YER İLE ARANDAKİ MESAFE
MANYETOMETRE SAPMALARI TESPİT EDER
IMU(FC İÇİNDE) İHANIN İVMESİNİ DÖNÜŞÜNÜ YÖNELİMİNİ ÖLÇER.
GPS HASSAS KONUM

IMU(INERTIAL MEASUREMENT UNİT)
A) İVME ÖLÇER
SABİTSE YER ÇEKİMİNİ HİSSEDER
İVMELİYSE ANLAR

B) JIROSKOP
  NE KADAR VE HANGİ HIZLA DÖNDÜĞÜNÜ ANLAR

PID KONTROLÜ DRONE DENGEYİ KORUYAN MATEMATİKSEL KONTROL SİSTEMİ
PROPOTİONAL--ANLIK HATAYA TEPKİ VERİR
INTEGRAL--ZAMANLA BİRİKEN HATAYI SIFIRLAR
DERIVATIVE--HATA DEĞİŞİM HIZINI İZLER

GPS
HEM POSITION HOLD HEM DE WAYPOİNTS GÖREVİ GÖRÜR.RTL(RETURN TO LAUNCH) GÜVENLİ DÖNÜŞ SAĞLAR

RTK GPS VERİLERİNİ DOĞRULAR (REAL TİME KİNEMATİC GPS)
HATA PAYI DÜŞER.


SENSÖR FÜZYONUI VE GENİŞLETİLMİŞ KALMAN FİLTRESİ (EKF)
STATE ESTIMITION ÜRETME SÜRECİ( SENSÖR VERİLERİNİ BİRLEŞTİRİR)


GÖRÜNTÜ AKTARIM SİSTEMLERİ
1.ANALOG GÖRÜNTÜ AKTARIM SİSTEMİ:
DAHA ÇOK FPV YARIŞ DRONUNDA TERCİH EDİLİR.
AVANTAJLARI NEREDEYSE SIFIR GECİKME DÜŞÜK MALİYET VE HAFİF. ANCAK GÖRÜNTÜ ÇÖZÜNÜRLÜĞÜ DÜŞÜK

2. DİJİTAL GÖRÜNTÜ AKTARIM SİSTEMLERİ:
 GÖRÜNTÜ ÖNCE SIKIŞTIRILIR ARDINDAN DİJİTAL OLARAK İLETİLİR. AVANTAJI YÜKSEK ÇÖZÜNÜRLÜK,YÜKSEK MENZİL. ANCAK GECİKME VVAR VE MALİYETİ YÜKSEK.


COMPANİON COMPUTER:İHANIN BEYNİ
-GÖRÜNTÜ İŞLEME
-GÖREV PLANLAMA
-YAPAY ZEKA:MACHINE LEARNING
-VERİ ANALİZİ


AUTOPİLOT YAZILIMININ TEMEL İŞLEVLERİ
SENSOR FUSION & STATE ESTİMATİON
FLIGHT CONTROL
MİSSİON MANAGEMENT
FAİLSAFE AND SAFETY SYSTEM
FLİGHT MODES AND USER INTERFACES


PX4 OUTOPILOT (GUIDE)

!!FLIGHT MODES (MULTICOPTER)

1 MANUEL YARDIMLI MODLAR
>POSITION MODE:(IMU+BAROMETRE+GPS) RÜZGARA KARŞI YERİNİ KORUR
>ATTITUDE MODE :(IMU+BAROMETRE)ARAÇ İRTİFSDINI SABİT TUTAR
>STABILIZED MODE: (IMU)SADECE YATAY DURUŞUNU KORUR.
2 AKROBATIK MODLAR
 FLİP VE ROLL
3 OTONOM MODLAR

!!FLIGHT MODES (FIXED WINGS)
>POSITION MODE:UÇAK DÜZ ROTADA İLERLER.
>ALTUDE MODE:GPS GEREKMEZ PİLOT ROLL KONTROL EDER.
>STABILIZED MODE:pilot roll ve pitch açılarını kumanda eder.


OTONOM MODLAR
mission
hold
return
take off/land
orbit/follow me


DRONE PROGRAMLAMA KÜTÜPHANELERİ

 
İLETİŞİM PROTOKOLLERİ

*MAVLink komutumuzu taşıyan bir iletişim protokolü.
*PyMAVLink:MAVLinkin python temsili.KULLANIMI ZOR
*MAVSDK:MODERN VE KULLANICI DOSTU BİR YAKLAŞIM
*ROS KÜTÜPHANESİ:ROBOTİK PROJELERDE TERCİH EDİLİR. PX4 VE ARDUPILOT İLE UYUMLU.
*DRONEKIT: KÜÇÜK ORTA ÖLÇEKLİ PROJELER İÇİN UYGUN. EĞİTİM AMÇLI PROJE İÇİN İDEAL.


MAVSDK EN İDEAL. PX4
------------------------------------------------------------------------------------------------------------------------------------
GitHub Nedir: Projeye ait tüm dosyaların ve yapılan değişikliklerin tutulduğu, web tabanlı bir versiyon kontrol aracıdır.

Neden Kullanılır: Bilgisayarda yaşanabilecek donanımsal veya yazılımsal sorunlara karşı ilerlemeyi kaybetmemek ve önemli değişiklikler öncesinde projenin kaydını (yedeğini) almak için kullanılır. Günümüzde endüstri standardı haline gelmiştir.

Açık Kaynak (Open Source) ve Lisans: Açık kaynaklı projeler, kodların diğer kullanıcılara ve değiştirmelere açık olduğu projelerdir. Bu sayede dünyanın dört bir yanından geliştiricilerin ilgisi çekilebilir. Ancak açık kaynak olması her zaman ücretsiz dağıtım hakkı verildiği anlamına gelmez; insanların bu kodu nasıl ve ne kadar kullanabileceğini belirlemek için projeye bir lisans eklenir.

Download ZIP ve Clone Farkı: Projeyi ZIP olarak indirdiğinizde (örneğin starter-master şeklinde iner; burada 'starter' dosyanın ismi, 'master' ise branch'in ismidir) sadece kaynak kodları indirmiş olursunuz. Clone işlemi uyguladığınızda ise projenin geçmişini ve tüm Git özelliklerini de bilgisayarınıza klonlamış olursunuz.

.gitignore: GitHub reposuna gitmesini veya takip edilmesini istemediğimiz dosyaları belirttiğimiz özel dosyadır.

GitHub arayüzü üzerinden de proje üzerinde doğrudan değişiklikler yapılabilir. Ayrıca repo içindeki "Commits" kısmına tıklayarak projedeki hangi dosyalara nelerin eklendiğini (+ ile gösterilir) ve nelerin çıkarıldığını (- ile gösterilir) detaylıca görüntüleyebilirsiniz.

Git Bash ve Temel Terminal İşlemleri
Git komutlarını çalıştırmak için genellikle Git Bash kullanılır. Temel terminal komutları şunlardır:

mkdir <klasör_adı>: Yeni bir klasör oluşturur (Örnek: mkdir githubprojects).

cd <klasör_adı>: Oluşturulan veya halihazırda var olan klasörün içine girmeyi sağlar.

clear: Terminal ekranındaki geçmiş yazıları temizler.

Git Çalışma Akışı ve Senkronizasyon
git remote add origin: Bilgisayarımızdaki yerel Git reposuna, web üzerindeki uzak repoya bağlanması gerektiğini söyler.

git add <dosya_adı> veya git add .: Belirli bir dosyayı veya klasöre eklenen her şeyi Git'e tanıtmak (sahnelemek) için kullanılır.

git commit -m "Yorum": Yapılan değişiklikleri bir açıklama yazarak kaydeder. Push işleminden önce mutlaka commit atılmalıdır, aksi halde değişiklikler uzak repoya yansımaz. Not: Commit işlemi, bilgisayarda değişikliğin yapıldığı zamanı kaydeder. Dosyayı web reposuna saatler sonra push etseniz bile, commit ekranında değişikliğin ilk yapıldığı zaman (örneğin "8 dk önce") görünür.

git push: Commit edilmiş yerel kodları web'deki uzak repoya gönderir.

git pull: Uzak repodaki kodları yerel bilgisayara alır. Arka planda git fetch ve git merge işlemlerinin birleşimiyle çalışır.

Eğer bilgisayarınızdaki repo ile web'deki repo birebir aynıysa, push veya pull komutlarında bir değişiklik olmadığını belirten already up to date uyarısı alınır.

Önemli Kural: Web reposunda bir değişiklik yapıldıysa ve yerel bilgisayarda da değişiklik yapıp push etmek isterseniz hata alırsınız. Bu durumu önlemek için önce git pull ile web'deki güncel kodları yerel bilgisayara çekmek gerekir.

Çakışma (Conflict) Çözümü ve Branch (Dallanma) İşlemleri
Conflict (Çakışma): Bir dosyanın aynı kısmına hem web'de hem de yerel bilgisayarda farklı düzenlemeler yapıp push uygulanmak istendiğinde ortaya çıkar. git status komutu yazıldığında, dosyanın iki tarafta da değiştirildiğini belirten both modified uyarısı alınır.

Çözüm Yöntemi (Kafanın karıştığını belirtmişsin ancak temel mantığı tamamen doğru kavramışsın): Hangi versiyonun geçerli olmasını istiyorsak (örneğin local değişikliği korumak istiyorsak) dosyayı açıp remote'dan gelen ve istenmeyen kod satırlarını siliyoruz. Ardından git add . ile bu temizlenmiş hali tanımlayıp git commit -m "local değişikliği korudum" yazarak kaydediyoruz. Son olarak git push ile bu nihai dosyayı web reposuna dikte ediyoruz.

git checkout -b <isim>: Yeni bir branch (dal) oluşturur ve doğrudan o branch'e geçer.

git branch: Mevcut branch'leri görüntüler.

git branch -d <branch_adı>: Belirtilen branch'i siler.

git push origin <branch_ismi>: Yapılan değişiklikleri sadece o branch'e özel olarak uzak repoya gönderir.
