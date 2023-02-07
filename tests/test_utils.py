import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formatted_data

def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data("https://wrong.url.ru/")[0] is None
    assert get_data("https://github.com/npozdeeva/proj_kursovaya")[0] is None
    assert get_data("https://github.com/npozdeeva/proj_kursovaya33")[0] is None


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert data[0]["date"] == '2019-08-26T10:50:58.294041'
    assert len(data) == 4


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ["26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 {'code': 'RUB', 'name': 'руб.'}", "03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 {'code': 'USD', 'name': 'USD'}", "30.06.2018 Перевод организации\n  -> Счет **6702\n9824.07 {'code': 'USD', 'name': 'USD'}", "23.03.2018 Открытие вклада\n  -> Счет **2431\n48223.05 {'code': 'RUB', 'name': 'руб.'}", "04.04.2019 Перевод со счета на счет\nСчет 1970 86** **** 8542 -> Счет **4188\n79114.93 {'code': 'USD', 'name': 'USD'}"]


