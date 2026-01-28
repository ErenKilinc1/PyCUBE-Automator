"""

Kurumsal ağlarda konfigürasyon yedeği
hayati önem taşır. Bu script, router'ın
running-config bilgisini çekip tarihle
beraber bir .txt dosyasına kaydeder.

"""

from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'host': 'ip_address',
    'username': 'user.name',
    'password': 'password',
}

# Dosya adını tarihle oluşturur (Örn: config_backup_2026-01-26.txt)
date_str = datetime.now().strftime("%Y-%m-%d")
filename = f"config_backup_{date_str}.txt"

print(f"{device['host']} için yedekleme başlatılıyor...")

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show run')

    with open(filename, 'w') as f:
        f.write(output)

print(f"İşlem tamamlandı. Konfigürasyon '{filename}' dosyasına kaydedildi.")