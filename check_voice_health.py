"""

Bu script, bir CUBE (Voice Gateway) üzerindeki
aktif çağrı durumunu ve dial-peer özetini hızlıca
kontrol etmek için kullanılır. Manuel log bakmaktan
çok hızlıdır.

"""

from netmiko import ConnectHandler

# Cihaz bilgileri
cisco_cube = {
    'device_type': 'cisco_ios',
    'host': 'ip_address',
    'username': 'user.name',
    'password': 'password',
    'secret': 'password',
}

def get_voice_status():
    try:
        connection = ConnectHandler(**cisco_cube)
        connection.enable()

        print("--- CUBE Aktif Çağrı Durumu ---")
        calls = connection.send_command('show cube calls all')
        print(calls)

        print("------------------------------------------------------------------------------")

        print("\n--- Dial-Peer Özet Tablosu ---")
        dial_peers = connection.send_command('show dial-peer voice summary')
        print(dial_peers)

        connection.disconnect()
    except Exception as e:
        print(f"Bağlantı hatası: {e}")

if __name__ == "__main__":
    get_voice_status()