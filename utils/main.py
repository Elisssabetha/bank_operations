from utils.functions import sort_dates, get_operations, check_executed, print_info

def main():

    # список с экземплярами класса
    operations = []
    get_operations(operations)

    #  список с экземлярами класса - только выполненные операции
    operations_executed = []
    check_executed(operations, operations_executed)

    # список последних 5 операций по возрастанию
    last_5_operations = sort_dates(operations_executed)

    while last_5_operations:
        for operation in operations_executed:
            if operation.date_as_timestamp() == last_5_operations[-1]:
                '''выводит инфо по последней операции в списке'''
                print_info(operation)
                '''удаляет последнюю операцию из списка'''
                last_5_operations.pop()
                break

if __name__ == '__main__':
    main()
