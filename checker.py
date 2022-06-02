import requests
from config_bd import host, user, password, db_name
from url_bot_getter import get_website_url
import pymysql


def url_data_check(name_website):

    if "https://" in name_website:
        response = requests.get(name_website)
    else:
        response = requests.get(f'https://{name_website}')

    if response.status_code == 200:

        temp = check_database(name_website)

        if temp == 0:
            return get_website_url(name_website)
        else:
            return temp
    else:
        return "Нет возможности получить доступ к сайту. Проверьте введенные данные."


def check_database(name_website):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Подключение выполнено успешно...")
        try:
            with connection.cursor() as cursor:
                select_all_id = "SELECT url FROM urls_list;"  # Ра
                cursor.execute(select_all_id)
                rows = cursor.fetchall()
                for row in rows:
                    if row['url'] == name_website:
                        return row['workaround_url']
            return 0
        except Exception as ex:
            print(ex)
        finally:
            connection.close()
    except Exception as ex:
        print(ex)
        print("Не удалось подключиться к БД...")


print(url_data_check("vk.com"))
