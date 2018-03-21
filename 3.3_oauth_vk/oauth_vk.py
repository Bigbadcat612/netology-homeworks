import requests
import json

TOKEN = '7d84b19514bf4763e1fb6e4f2a2bdb1f2f23b6952ab4353ee57cd2a8ece4ad74bc7ab3d80980b2787a739'
V = '5.73'
URL = 'vk.com/id'


def get_friends_list(ids):
    """Выводит список друзей заданых айди в виде словаря 'айди пользователя: список друзей'"""
    friends_by_ids = {}
    print('Подключаюсь к vk.com...\n')
    for id in ids:
        params = dict(user_id=id, token=TOKEN, v=V)
        current_id = requests.get('https://api.vk.com/method/friends.get', params)
        current_id = json.loads(current_id.text)
        friends_by_ids[id] = set(current_id['response']['items'])

    return friends_by_ids


def get_common_friends(id_friends):
    """Создает множество общих друзей. Принимает значения в формате 'айди пользователя: список друзей'"""
    friend_list = []
    common_ids = set()
    common_friends = dict()

    for friends in id_friends.values():
        friend_list.append(friends)

    common_ids.update(friend_list[0])
    for i in range(1, len(friend_list)):
        common_ids = common_ids & friend_list[i]

    print('Создаю список общих друзей...\n')
    for id in common_ids:
        params = dict(user_id=id, token=TOKEN, v=V)
        current_id = requests.get('https://api.vk.com/method/users.get', params)
        current_id = json.loads(current_id.text)
        user_name = '{} {}'.format(current_id['response'][0]['first_name'], current_id['response'][0]['last_name'])
        common_friends[id] = user_name

    return common_friends


user_input = input('Введите айди пользователей через пробел. По окончанию нажмите Enter.\n').split()
common_friends = get_common_friends(get_friends_list(user_input))

for id, name in common_friends.items():
    print('{}: {}'.format(name, ''.join((URL, str(id)))))