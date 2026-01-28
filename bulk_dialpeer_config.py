"""

Bu kod, parametrik olarak tanımlanmış voice dial-peer konfigürasyonlarını
cihaz üzerine otomatik şekilde uygular.

Dial-peer numaraları ve destination-pattern bilgileri bir liste/dictionary
üzerinden yönetilir; böylece GSM operatöründen alınan yeni numara blokları
hızlı ve hatasız biçimde konfigüre edilebilir.

"""

from netmiko import ConnectHandler

# Cihaz Bilgileri
router = {
    'device_type': 'cisco_ios',
    'host': 'ip_address',
    'username': 'user.name',
    'password': 'password',
}

SESSION_TARGET = '10.10.10.1'
CODEC = 'g711ulaw'

dial_peers = {
    1001: '555.......',
    1002: '556.......',
    1003: '557.......'
}

def build_dial_peer_config(dp_id, pattern):
    return [
        f'dial-peer voice {dp_id} voip',
        f' destination-pattern {pattern}',
        ' session protocol sipv2',
        f' session target ipv4:{SESSION_TARGET}',
        f' codec {CODEC}',
        ' no vad'
    ]

def configure_dial_peers():
    all_commands = []

    for dp_id, pattern in dial_peers.items():
        all_commands.extend(build_dial_peer_config(dp_id, pattern))

    with ConnectHandler(**router) as net_connect:
        net_connect.enable()
        print("Dial-peer konfigürasyonları uygulanıyor...\n")

        output = net_connect.send_config_set(all_commands)
        print(output)

        net_connect.send_command('write memory')
        print("\nKonfigürasyon kaydedildi.")

if __name__ == "__main__":
    configure_dial_peers()
