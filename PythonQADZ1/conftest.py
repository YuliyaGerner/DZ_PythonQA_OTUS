"""setup-методы для тестов"""
import pytest


@pytest.fixture(scope='module')
def setup_companies_list():
    """Список с компаниями"""
    return ['microsoft', 'google', 'oracle', 'apple', 'google']


@pytest.fixture(scope='module')
def setup_figures_list():
    """Список с цифрами"""
    return [1, 2, 3, 4, 5]


@pytest.fixture(scope='module')
def setup_motobikes_dictionary():
    """Список со словарем мотоциклов"""
    return {'honda': 1, 'yamaha': 3, 'suzuki': 2}


@pytest.fixture(scope='module')
def setup_programming_dict():
    """Список со словарем языков программирования"""
    return {1: 'julia', 2: 'matlab', 3: 'python', 4: 'haskel', 5: 'javascript'}


@pytest.fixture(scope='module')
def setup_set_veggies():
    """Список со словарем овощей"""
    return {'cucumber', 'potato', 'carrot', 'eggplant', 'broccoli', 'corn'}


@pytest.fixture(scope='module')
def setup_string_example():
    """Список со словарем знаков"""
    return 'cuburiduburis'
