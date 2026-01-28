# Cisco CUBE Network Automation with Python

Bu proje, Cisco Unified Communications (UC) ekosisteminde çalışan sistem ve network mühendisleri için günlük operasyonel görevleri otomatize eden Python scriptlerini içerir. Özellikle **Cisco CUBE (Voice Gateway)** yönetimi, dial-peer konfigürasyonu ve sistem izleme süreçlerine odaklanır.

##  Güvenlik Uyarısı (Warning)
Bu araç dial-peer konfigürasyonlarını değiştirme yeteneğine sahiptir. Canlı ortamlarda kullanmadan önce mutlaka Test/Lab ortamında deneyiniz.

## Proje Hakkında
Kurumsal ölçekli IP telefon ve ses ağlarında, manuel konfigürasyonlar zaman alıcı ve hata yapmaya müsaittir. Bu projede yer alan araçlar:
* **Hızlı İzleme:** Aktif çağrı ve dial-peer durumlarını anlık raporlar.
* **Güvenli Yedekleme:** Cihaz konfigürasyonlarını tarih bazlı yedekler.
* **Parametrik Konfigürasyon:** Yeni numara bloklarını (GSM/SIP) saniyeler içinde tanımlar veya siler.

## Kullanılan Teknolojiler
* **Python 3.x**
* **Netmiko:** Çoklu cihaz bağlantısı ve CLI komut yönetimi için.
* **Cisco IOS/IOS-XE:** ISR 4451, 3845 ve CUBE platformları.

## Bağımlılıkları Yükleme
pip install -r requirements.txt

## Script İçerikleri

| Script Adı | Açıklama |
| :--- | :--- |
| `get_voice_status.py` | CUBE üzerindeki aktif çağrıları ve dial-peer özetini getirir. |
| `backup_config.py` | Cihazın running-config dosyasını yerel dizine tarih bazlı `.txt` olarak yedekler. |
| `configure_dial_peers.py` | Listelenmiş dial-peer ve destination-pattern'leri toplu uygular. |
| `remove_dial_peers.py` | Belirtilen dial-peer numaralarını sistemden temizler. |



