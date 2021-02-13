"""Тест для списков"""
import pytest


@pytest.mark.list
def test_list_count(setup_companies_list):
    """Проверка сколько раз был добавлен элемент в списке"""
    assert setup_companies_list.count('google') == 2


@pytest.mark.list
def test_list_append(setup_figures_list):
    """Добавление в список элементов и сравнивание добавились элементы ли в конце списка"""
    setup_figures_list.append(6)
    setup_figures_list.append(7)
    setup_figures_list.append(8)
    assert setup_figures_list == [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.list
def test_list_index(setup_companies_list):
    """Проверка индекса элемента"""
    assert setup_companies_list.index('microsoft') == 0


@pytest.mark.list
def test_list_clear(setup_figures_list):
    """Заполнение списка, очищение списка, проверка, что список пустой"""
    setup_figures_list.clear()
    assert setup_figures_list == []


@pytest.mark.list
def test_list_remove(setup_companies_list):
    """Проверка списка после удаления элемента"""
    setup_companies_list.remove('google')
    assert setup_companies_list == ['microsoft', 'oracle', 'apple', 'google']


TESTDATA = [
    (['microsoft', 'oracle', 'apple', 'google'], 'google', 3),
    (['microsoft', 'oracle', 'apple', 'google'], 'microsoft', 0),
    (['microsoft', 'oracle', 'apple', 'google'], 'apple', 2),
]


@pytest.mark.list
@pytest.mark.parametrize("first_list,second_list,expected", TESTDATA)
def test_count_with_params(first_list, second_list, expected):
    """Проверка индекса элемента в списке"""
    assert first_list.index(second_list) == expected