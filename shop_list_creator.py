def read_items():
    with open('recipes.txt', 'r') as f:
        for line in f:
            print(line.strip())


def make_cookbook_from_recipes():
    cook_book = {}
    with open('recipes.txt', 'r') as f:
        current_line = 0
        for line in f:
            cur_line = line.strip().lower()
            cook_book[cur_line] = []
            ingridient_amount = int(f.readline().strip())
            for _ in range(ingridient_amount):
                current_list = f.readline().strip().split(' | ')
                new_dish = {'ingridient_name': current_list[0].lower(), \
                'quantity': int(current_list[1]), 'measure': current_list[2].lower()}
                cook_book[cur_line].append(new_dish)
            f.readline().strip()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item[
                    'ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += \
                  new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'],
                                shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
      .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list(make_cookbook_from_recipes())

