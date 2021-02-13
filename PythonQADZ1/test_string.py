"""Тесты для строк"""
import pytest


@pytest.mark.string
def test_string_uppercase(setup_string_example):
    """Проверка что строка была переведена в верхний регистр"""
    assert setup_string_example.upper() == 'CUBURIDUBURIS'


@pytest.mark.string
def test_string_replace(setup_string_example):
    """Проверка что в строке заменяются буквы"""
    assert setup_string_example.replace("u", "e") == 'ceberideberis'


@pytest.mark.string
def test_string_len(setup_string_example):
    """Проверка длины строки"""
    assert len(setup_string_example) == 13


@pytest.mark.string
def test_string_concatenation(setup_string_example):
    """Проверка что  получилась новая строка"""
    second_string = "blablabla"
    assert setup_string_example + second_string == "cuburiduburisblablabla"


@pytest.mark.string
def test_string_count(setup_string_example):
    """Проверка количества вхождений в получаемой строке"""
    assert setup_string_example.count("bur") == 2


TESTDATA = [
    ('ololo', 'lalala', 11),
    ('привет', 'Boris', 12),
    ('привет', '1111', 10),
]


@pytest.mark.string
@pytest.mark.parametrize("f_str, sec_str, expected", TESTDATA)
def test_count_string(f_str, sec_str, expected):
    """Проверка длины строки после сложения"""
    addition = len(f_str + sec_str)
    assert addition == expected
