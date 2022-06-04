import requests
import database
from url_bot_getter import get_website_url


def url_data_check(name_website):
    try:
        if "https://" in name_website:
            response = requests.get(name_website)
        else:
            name_website = f'https://{name_website}'
            response = requests.get(name_website)

        if response.status_code == 200:

            temp = database.check_url_table(name_website)

            if temp == 0:
                return get_website_url(name_website)
            else:
                return temp
        else:
            return "Нет возможности получить доступ к сайту. Проверьте введенные данные."
    except Exception as ex:
        print(ex)
        return "Нет возможности получить доступ к сайту. Проверьте введенные данные."
