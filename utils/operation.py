from datetime import datetime


class Operation:
    def __init__(self, code_id, state, date, operation_amount, description, account_from, account_to):
        self.code_id = code_id
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.account_from = account_from
        self.account_to = account_to

    def is_executed(self):
        '''возвращает True, если операция выполнена'''
        return self.state == "EXECUTED"

    def correct_date_format(self):
        '''приводит дату к нужному для вывода формату'''
        thedate = datetime.fromisoformat(self.date)
        return thedate.strftime('%d.%m.%Y')

    def date_as_timestamp(self):
        '''переводит дату в милисекунды'''
        thedate = datetime.fromisoformat(self.date)
        return thedate.timestamp()

    def hide_card_number(self):

        ''' зашифровывает номер карты'''

        if self.account_from == 'нет данных':
            return 'нет данных'
        elif 'Счет' in self.account_from:
            return self.hide_account_to()
        else:
            list_account_from = list(self.account_from)

            for i in range(5, 11):
                list_account_from[-i] = '*'

            for i in [-4, -9, -14]:
                list_account_from.insert(i, ' ')
            return ''.join(list_account_from)

    def hide_account_to(self):

        '''зашифровывает номер счета'''

        list_account_to = list(self.account_to)
        list_account_to[-5:-4] = ['*', '*']
        return ''.join(list_account_to[0:5] + list_account_to[-6:])

    def __repr__(self):
        return str(self.code_id)
