import json
import os.path

from utils.operation import Operation

os.path.join('utils', 'operations.json')


def get_list_operations():
    'создает список из операция(словари)'
    with open('operations.json', 'rt', encoding='utf-8') as f:
        return json.loads(f.read())


def get_operations(operations):
    '''создаем список эксземпляров класса'''
    for item in get_list_operations():
        code_id = item['id']
        st = item['state']
        dt = item['date']
        opAm = item['operationAmount']
        desc = item['description']
        if 'from' not in item.keys():
            '''обработка случая, когда нет информации по счету/карте списания'''
            fr = 'нет данных'
        else:
            fr = item['from']
        t = item['to']
        operations.append(Operation(code_id, st, dt, opAm, desc, fr, t))


def check_executed(operations, operations_executed):
    '''выделяет выполненные операции'''
    for operation in operations:
        if operation.is_executed():
            operations_executed.append(operation)


def sort_dates(list_operations):
    '''из экземпляров класса создает список из дат в милисекундах, сортирует их, выводит 5 последних'''
    list_of_dates = []

    for operation in list_operations:
        list_of_dates.append(operation.date_as_timestamp())

    sorted_list_of_dates = sorted(list_of_dates)

    return sorted_list_of_dates[-5:]


def print_info(operation):
    '''вывод инфо в нужном виде'''
    print(f'{operation.correct_date_format()} {operation.description}')
    print(f'{operation.hide_card_number()} → {operation.hide_account_to()}')
    print(f'{operation.operation_amount["amount"]} {operation.operation_amount["currency"]["name"]} ')
    print()
