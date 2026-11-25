# KARAR: Program büyük/küçük harf duyarsız (case-insensitive) olacak şekilde tasarlanmıştır.
raw_text = input("Enter a sentence or paragraph for YODA: ")  # Kullanıcıdan ham metni alır ve değişkene atar.
total_characters = len(raw_text)  # Boşluklar ve noktalama işaretleri dahil toplam karakter sayısını hesaplar.

lower_text = raw_text.lower()  # Büyük/küçük harf farkını ortadan kaldırmak için tüm harfleri küçültür.
punctuation_marks = ".,!?;:\"'()[]{}-"  # Kelime uzunluğunu ve sayımını bozabilecek noktalama işaretlerini tanımlar.
cleaned_text = ""  # Noktalama işaretlerinden arındırılmış temiz metni tutacak boş bir string oluşturur.

for char in lower_text:  # Küçük harfe çevrilmiş metindeki her bir karakteri tek tek gezer.
    if char not in punctuation_marks:  # Mevcut karakter tanımlanan noktalama işaretlerinden biri değilse kontrol eder.
        cleaned_text += char  # Temiz karakteri yeni metin değişkeninin sonuna ekler.

words = cleaned_text.split()  # Temizlenmiş metni boşluklardan bölerek kelimelerden oluşan bir liste (list) oluşturur.
total_words = len(words)  # oluşturulan kelime listesindeki eleman sayısını bularak toplam kelime sayısını hesaplar.

word_counts = {}  # Her bir kelimenin kaç kez geçtiğini (anahtar kelime, değer: adet) tutacak boş bir sözlük (dict) açar.
max_word_length = 0  # En uzun kelimenin karakter uzunluğunu takip etmek için başlangıç değerini 0 olarak belirler.

for word in words:  # Kelime listesindeki her bir kelimeyi sırayla döngüye sokar.
    if len(word) > max_word_length:  # Mevcut kelimenin uzunluğu o ana kadar bulunan en büyük uzunluktan fazlaysa kontrol eder.
        max_word_length = len(word)  # Yeni en uzun kelime uzunluğunu günceller.
    if word in word_counts:  # Kelime daha önce sözlüğe eklenmiş mi diye kontrol eder.
        word_counts[word] += 1  # Kelime sözlükte zaten varsa tekrar sayısını 1 artırır.
    else:  # Kelime sözlükte henüz yoksa bu bloğa girer.
        word_counts[word] = 1  # Kelimeyi sözlüğe ilk kez ekler ve sayacını 1 olarak başlatır.

print("\n--- Text Analysis Results ---")
print("Total characters (including spaces):", total_characters)  # Boşluklar dahil toplam karakter sayısını ekrana basar.
print("Total words:", total_words)  # Hesaplanan toplam kelime sayısını ekrana basar.
print("Length of the longest word:", max_word_length)  # En uzun kelimenin karakter sayısını ekrana basar.
print("Word frequencies:")  # Kelime tekrar sayıları listesi için alt başlık yazdırır.

for word, count in word_counts.items():  # Sözlükteki her bir kelime (key) ve tekrar sayısı (value) çiftini tek tek alır.
    print(f"- '{word}': {count} time(s)")  # Her kelimenin metinde kaç kez tekrar ettiğini formatlı şekilde ekrana yazdırır.
