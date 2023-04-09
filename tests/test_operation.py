import pytest

from utils.operation import Operation


@pytest.fixture
def class_example_fixture():
    return Operation('441945886', 'EXECUTED', '2019-08-26T10:50:58.294041',
                     {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, 'Перевод организации',
                     'Maestro 1596837868705199', 'Счет 64686473678894779589')

@pytest.fixture
def class_example_fixture_2():
    return Operation('441945886', 'EXECUTED', '2019-08-26T10:50:58.294041',
                     {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, 'Перевод организации',
                     'нет данных', 'Счет 64686473678894779589')
@pytest.fixture
def class_example_fixture_3():
    return Operation('441945886', 'EXECUTED', '2019-08-26T10:50:58.294041',
                     {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, 'Перевод организации',
                     'Счет 75106830613657916952', 'Счет 64686473678894779589')


def test_is_executed(class_example_fixture):
    assert class_example_fixture.is_executed() == True


def test_correct_date_format(class_example_fixture):
    assert class_example_fixture.correct_date_format() == '26.08.2019'


def test_date_as_timestamp(class_example_fixture):
    assert class_example_fixture.date_as_timestamp() == 1566805858.294041


def test_hide_card_number(class_example_fixture, class_example_fixture_2, class_example_fixture_3):
    assert class_example_fixture.hide_card_number() == 'Maestro 1596 83** **** 5199'
    assert class_example_fixture_2.hide_card_number() == 'нет данных'
    assert class_example_fixture_3.hide_card_number() == 'Счет **6952'


def test_hide_account_to(class_example_fixture):
    assert class_example_fixture.hide_account_to() == 'Счет **9589'

def test_repr(class_example_fixture):
    assert repr(class_example_fixture) == '441945886'
