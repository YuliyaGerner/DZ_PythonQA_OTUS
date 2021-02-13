"""Тесты для словарей"""
import pytest


@pytest.mark.dictionary
def test_dictionary_sort(setup_motobikes_dictionary):
    """Проверка сортировки ключей в словаре"""
    assert (sorted(setup_motobikes_dictionary.keys())) == ['honda', 'yamaha', 'suzuki']


@pytest.mark.dictionary
def test_dictionary_del_key(setup_motobikes_dictionary):
    """Проверка удаления ключа"""
    del setup_motobikes_dictionary['honda']
    assert setup_motobikes_dictionary == {'suzuki': 3, 'yamaha': 2}


@pytest.mark.dictionary
def test_dictionary_contains_element(setup_motobikes_dictionary):
    """Проверка  наличие элемента"""
    setup_motobikes_dictionary['ducati'] = 4
    assert ('ducati' in setup_motobikes_dictionary) == 1


@pytest.mark.dictionary
def test_dictionary_pop(setup_programming_dict):
    """Заполнение списка, проверка списка"""
    setup_programming_dict.pop(1)
    assert setup_programming_dict == {2: 'matlab', 3: 'python', 4: 'haskel', 5: 'javascript'}


@pytest.mark.dictionary
def test_dictionary_clear(setup_programming_dict):
    """Проверка удаления всех элементов"""
    setup_programming_dict.clear()
    assert setup_programming_dict == {}


TESTDATA = [
    ({1: 'julia', 2: 'matlab', 3: 'python'}, 1, 'julia'),
    ({1: 'honda', 3: "yamaha", 2: 'suzuki'}, 3, 'yamaha'),
    ({1: 'julia', 2: 'matlab', 3: 'python'}, 2, 'matlab'),
]


@pytest.mark.parametrize("dict_example, number,  expected", TESTDATA)
@pytest.mark.dictionary
def test_pop_dictionary(dict_example, number, expected):
    """Проверка удаление всех элементов"""
    assert dict_example.pop(number) == expected