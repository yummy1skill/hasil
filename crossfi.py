# Made with ❤ by yummy
import requests
import time
from colorama import init, Fore, Style
import sys
import os
init(autoreset=True)

def print_welcome_message():
    print(r"""
            jamet
          """)


    print(Fore.GREEN + Style.BRIGHT + "CROSSSFI")
    print(Fore.GREEN + Style.BRIGHT + "Telegram: @hisha\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# url endpoint
url_get_user = 'https://test-bot.crossfi.org/api/v1/user/stat'
# Headers yang diperlukan untuk request
headers = {
    'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://bot.crossfi.org',
        'dnt': '1',
        'Referer': 'https://bot.crossfi.org/',
        'priority': 'u=1, i',
        'Sec-Ch-Ua': '"Not A;Brand";v="99", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-mobile': '?1',
        'Sec-Ch-Ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'X-Tg-Data:': 'tokens',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',

}

def load_credentials():
    try:
        with open('authorization.txt', 'r') as file:
            credentials_list = file.readlines()
        credentials = [cred.strip() for cred in credentials_list]
        return credentials
    except FileNotFoundError:
        print("File 'authorization.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script.")
        return []

def get_user():
    response = requests.get(url_get_user, headers=headers)
    if response.status_code == 200:
        # Menguraikan response JSON
        profile_data = response.json()
        # Mengakses nama dari data
        name = profile_data['data']['name']
        print(f"{Fore.CYAN+Style.BRIGHT}============== [ Akun | {name} ] ==============")  # Mencetak nama

        # Mengakses bagian 'upgrades' dari data dan mengelompokkan berdasarkan tipe upgrade
        upgrades = {}
        for upgrade in profile_data['data']['upgrades']:
            upgrade_type = upgrade['upgrade_type']
            upgrade_level = upgrade['upgrade_level']
            if upgrade_type in upgrades:
                # Memperbarui level jika level yang baru lebih tinggi
                if upgrade_level > upgrades[upgrade_type]:
                    upgrades[upgrade_type] = upgrade_level
            else:
                upgrades[upgrade_type] = upgrade_level

        # Mencetak 'upgrade_level' dari setiap upgrade dengan level ditambah 1
        for upgrade_type, level in upgrades.items():
            print(f"{Fore.BLUE+Style.BRIGHT}[ {upgrade_type.capitalize()} Level ]: {level + 1}")
    else:
        print("Gagal mendapatkan data, status code:", response.status_code)
        return None  # Mengembalikan None jika gagal mendapatkan profil


def telegram(authorization):
    url = 'https://testpad.xfi.foundation/api/v1/authenticate/telegram'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {authorization}',
        'Content-Type': 'application/json',
        'Origin': 'https://bot.crossfi.org',
        'dnt': '1',
        'Referer': 'https://bot.crossfi.org/',
        'priority': 'u=1, i',
        'Sec-Ch-Ua': '"Not A;Brand";v="99", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-mobile': '?1',
        'Sec-Ch-Ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',

     }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def get_tapCoinImage(authorization):
    url = 'https://bot.crossfi.org/images/tapCoin.png'
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control:': 'no-cache',
        'Pragma:': 'no-cache',
        'dnt': '1',
        'Referer': 'https://bot.crossfi.org/',
        'priority': 'u=1, i',
        'Sec-Ch-Ua': '"Not A;Brand";v="99", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-mobile': '?1',
        'Sec-Ch-Ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
     }

def main():
    print_welcome_message()


    while True:  # Loop eksternal yang membuat program berjalan terus menerus

        for index, authorization in enumerate(credentials): # type: ignore
            info = telegram( authorization)
            print(f"{Fore.CYAN+Style.BRIGHT}============== [ Akun {index} | {info['first_name']} ] ==============")

        time.sleep(2)
        # Hitung mundur selama 1 menit setelah semua akun telah diproses
        print(f"{Fore.CYAN+Style.BRIGHT}==============Semua akun telah diproses=================")
        for i in range(600, 0, -1):
            sys.stdout.write(f"\rMemproses ulang semua akun dalam {i} detik...")
            sys.stdout.flush()
            time.sleep(1)
        print()  # Cetak baris baru setelah hitungan mundur selesai

        # Membersihkan konsol setelah hitungan mundur
        clear_console()