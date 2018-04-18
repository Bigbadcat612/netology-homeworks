import requests
import json

TOKEN = '1ea6c7dfc081ffbec0a07a5cb6149cdab590ed2b437cfdda7300174d42c4ff46b353861bc3c8d54947701'
V = '5.74'
URL = 'vk.com/id'
id1 = input('Введите первый id\n')
id2 = input('Введите второй id\n')


def get_mutual_friends(source_id, target_id):
    params = dict(
        source_uid = source_id,
        target_uid = target_id,
        access_token = TOKEN,
        v = V
    )

    mutual_friends = requests.get('https://api.vk.com/method/friends.getMutual', params).json()
    
    return mutual_friends['response']


def get_names(ids):
    friends_with_names = {}
    for id in ids:
        params = dict(user_id=id, token=TOKEN, v=V)
        current_id = requests.get('https://api.vk.com/method/users.get', params).json()
        user_name = '{first_name} {last_name}'.format(**current_id['response'][0])
        friends_with_names[id] = user_name
        
    return friends_with_names


common_friends = get_names(get_mutual_friends(id1, id2))

print('Общие друзья для id{} и id{}:\n'.format(id1, id2))
for id, name in common_friends.items():
    print('{}: {}'.format(name, ''.join((URL, str(id)))))
