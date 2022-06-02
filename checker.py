import requests
import pymysql


def url_data_check(name_website):
    if "https://" in name_website:
        response = requests.get(name_website)
    else:
        response = requests.get(f'https://{name_website}')

    if response.status_code == 200:

    else:
        return "Нет возможности получить доступ к сайту. Проверьте введенные данные."


print(url_data_check("vk.com"))