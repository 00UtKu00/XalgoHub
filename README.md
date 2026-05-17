Sen kıdemli bir Full-Stack Yazılım Mimarı ve UI/UX Tasarımcısısın. Vibe Coding yaklaşımıyla, kullanıcıların X (Twitter) algoritmasını simüle ederek tweetlerini optimize edebileceği, oturum açma (login) gerektirmeyen, tamamen istemci taraflı (client-side) veya hafif bir Python backend (Streamlit/FastAPI) ile çalışan modern bir "X Algorithm Simulator & Growth Assistant" web sitesi inşa edeceğiz.

Aşağıdaki mimariyi, özellikleri ve kuralları adım adım, modüler ve temiz bir kod yapısıyla oluştur.

### 1. TEKNOLOJİK ALTYAPI VE GÖRÜNÜM
- Tek bir sayfa (Single Page Application) veya temiz sekmeli bir yapı kullan. (Python Streamlit veya Tailwind CSS'li modern bir HTML/JS yapısı tercih edilebilir).
- Arayüz tamamen modern, karanlık mod (dark mode) odaklı, X estetiğine uygun, minimalist ve "scannable" (gözle kolay taranabilir) olmalı.
- Kesinlikle kullanıcı kaydı, veritabanı veya API anahtarı zorunluluğu olmayacak; her şey tarayıcıda veya yerel oturumda dönecek.

### 2. SİSTEM BİLEŞENLERİ VE GİRDİ PANELİ (SOL TARAF)
Kullanıcı şu verileri girebilmeli:
- **Hesap Profili Seçimi (Dropdown & Custom):** 
  * Hazır profiller: "Yeni/Küçük Hesap (0-1K Takipçi, Düşük Güven Skoru)", "Büyümekte Olan (1K-50K Takipçi, Orta Güven)", "Influencer (50K+, Yüksek Güven)", "Onaylı/Mavi Tikli Hesap", "Bot Şüpheli/Gölge Yasaklı Hesap".
  * Manuel Giriş: Takipçi sayısı, Takip edilen sayısı, Hesap yaşı.
- **Tweet Editörü:** Metin alanı (Karakter sayacı ile birlikte - maks 280 veya Premium için 4000).
- **Medya Ekleme Simülatörü:** "Sadece Metin", "Görsel/Fotoğraf", "Video", "GIF", "Anket" seçenekleri. (Video seçilirse algoritmanın kalma süresi çarpanı aktif olmalı).
- **Zamanlama (Post Time):** Saat ve gün seçimi (Algoritmanın aktiflik/etkileşim havuzu çarpanı için).
- **Hedef/Tahmini Etkileşimler:** Kullanıcının bu tweetten beklediği "Beğeni", "Retweet", "Yer İmleri (Bookmark)" ve "Yanıt (Reply)" sayılarını girebileceği kaydırıcılar (sliders).

### 3. ALGORİTMA DOSYASI YÜKLEME MODÜLÜ (DİNAMİK MOTOR)
- Panelde bir "X Algoritma Dosyası Yükle (.txt, .py, .json)" alanı olacak.
- **Çalışma Mantığı:** Kullanıcı bir dosya yüklediğinde, sistem metni tarayacak. Eğer dosyada `Like_Weight`, `Reply_Weight`, `Retweet_Weight`, `Video_Multiplier`, `Link_Penalty` gibi anahtar kelimeler veya katsayılar varsa bunları regex/metin analizi ile yakalayıp simülatörün arkasındaki matematiksel formülü güncelleyecek.
- **Yedek Plan (Fallback):** Eğer dosya yüklenmezse, sistem X'in bilinen güncel resmi algoritma ağırlıklarını varsayılan (default) olarak kullanacak (Örn: Like = 1x, Retweet = 20x, Reply = 54x, Link Cezası = -20x vb.).

### 4. ANALİZ VE RAPORLAMA PANELİ (SAĞ TARAF)
Kullanıcı "Simüle Et" butonuna bastığında şu çıktılar canlı ve grafiksel olarak üretilmeli:
- **Algoritma Uygunluk Skoru (0-100):** Tweetin bütününe verilen genel puan.
- **Tahmini Erişim Skoru (Impression Predictor):** Hesap büyüklüğü, hedef etkileşimler ve zamanlama çarpanı formüle edilerek hesaplanan tahmini gösterim aralığı.
- **Algoritma Karnesi (Yeşil/Kırmızı Işıklar):**
  * Örn: "🟢 Video kullanımı görünürlüğü 2x artırdı."
  * Örn: "🔴 Dış link (Youtube/Web sitesi) tespiti! Algoritma erişimi %50 baskılayabilir."
  * Örn: "🟡 Çok fazla hashtag kullanımı! Spam filtresine takılma riski."

### 5. GELİŞMİŞ YAPAY ZEKA ÖZELLİKLERİ (EKSTRA MODÜLLER)
- **Modül A: AI A/B Testi (Varyasyon Üretici):** Girilen tweeti analiz edip, algoritma skorunu artıracak 3 farklı alternatif metin önersin (Daha güçlü kanca cümle, daha kısa yapı vb.). (Not: Gerçek API yoksa bunu prompt mühendisliği kurallarına göre yerel şablonlarla veya mock-AI mantığıyla simüle et ya da kullanıcıya isteğe bağlı olarak kendi Gemini/OpenAI API anahtarını girebileceği geçici bir alan sun).
- **Modül B: Yankı Odası (Topic Clustering):** Tweet metnindeki kelimelerden konuyu tahmin etsin (Örn: Teknoloji, Siyaset, Kripto) ve o kategorinin güncel algoritma trend ağırlığını göstersin.
- **Modül C: Troll ve Linç Riski Ölçer:** Metnin duygusal tonunu (Sentiment) analiz ederek "Tartışma ve Yorum Çekme Gücü" ile "Linç/Şikayet Riski" oranını bir bar grafik olarak versin. (X algoritması tartışmalı içerikleri öne çıkarır kuralına sadık kal).

### SİZDEN BEKLENTİM:
Bu sistemi modüler parçalar halinde yazmaya başla. İlk adım olarak bana projenin temel dosya yapısını kur ve ardından **Girdi Paneli (Hesap seçimi, tweet editörü, dosya yükleme)** ile **Arka plandaki puanlama motorunu** içeren ilk çalışan prototip kodlarını ver. Her adımı açıklayarak ilerle.