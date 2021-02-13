"""Тесты для множеств"""
import pytest


@pytest.mark.sets
def test_set_join(setup_set_veggies):
    """Проверка строки после присоединения к ней другой"""
    assert ('banana' in setup_set_veggies) == 0


@pytest.mark.sets
def test_set_del_element():
    """Проверка что set() удаляет повторения элементов множества"""
    test_set_unique = set('hetczchetczbhetczc')
    assert test_set_unique == {'c', 'z', 'e', 'h', 't'}


@pytest.mark.sets
def test_empty_set():
    """Проверка, что после создания множества и очистки осталось пустое множество"""
    test_set = {'foo', 'bar'}
    test_set.clear()
    assert test_set == set()


@pytest.mark.sets
def test_set_len(setup_set_veggies):
    """Проверка, что множество включает элементы"""
    assert len(setup_set_veggies) != 0


@pytest.mark.sets
def test_set_append():
    """Проверка на пересекающиеся элементы"""
    first_set = set('lexus')
    second_set = set('rolex')
    assert (first_set & second_set) == {'l', 'e', 'x'}


TESTDATA = [
    ({'foo', 'bar'}, None),
    ({'trelolo'}, None),
]


@pytest.mark.sets
@pytest.mark.parametrize("set_example, expected", TESTDATA)
def test_count_string(set_example, expected):
    """Очистка множеств элементов"""
    assert set_example.clear() == expected