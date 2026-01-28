"""

Daha önce tanımlanmış voice dial-peer konfigürasyonlarını
Router/Gateway cihazı üzerinden otomatik olarak silmek için
kullanılan python betiği.

"""

from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': 'ip_address',
    'username': 'user.name',
    'password': 'password',
}

# Silinecek Dial-Peer numaraları (örn: 1001, 1002, 1003)
dial_peers = [1001, 1002, 1003]

def remove_dial_peers():
    commands = []

    for dp_id in dial_peers:
        commands.append(f'no dial-peer voice {dp_id} voip')

    with ConnectHandler(**router) as net_connect:
        net_connect.enable()
        print("Dial-peer konfigürasyonları siliniyor...\n")

        output = net_connect.send_config_set(commands)
        print(output)

        net_connect.send_command('write memory')
        print("\nDeğişiklikler kaydedildi.")

if __name__ == "__main__":
    remove_dial_peers()
