import json


def check_url_table(name_website):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['couple']:
            if p['url'] == name_website:
                return p['workaround']
    return 0


def insert_new_url(name_website, workaround_url):
    with open('data.txt') as json_file:
        data = json.load(json_file)
        data['couple'].append({'url': name_website,
                               'workaround': workaround_url})
        while data['couple'].count({'url': name_website, 'workaround': workaround_url}) > 1:
            data['couple'].remove({'url': name_website, 'workaround': workaround_url})
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


def insert_url_in_user_history(chat_id, name_website):
    with open('users_history.txt') as json_file:
        data = json.load(json_file)
        flag = True
        for p in data['users']:
            if p['chat_id'] == chat_id:
                if len(p['names_website']) == 10:
                    p['names_website'].pop(0)
                    p['names_website'].append(name_website)
                else:
                    p['names_website'].append(name_website)
                flag = False
        if flag:
            temp = [name_website]
            data['users'].append({'chat_id': chat_id,
                                  'names_website': temp})

    with open('users_history.txt', 'w') as outfile:
        json.dump(data, outfile)


def get_user_history(chat_id):
    with open('users_history.txt') as json_file:
        data = json.load(json_file)
        for p in data['users']:
            if p['chat_id'] == chat_id:
                return p['names_website']
    return []
