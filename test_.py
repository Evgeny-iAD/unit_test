import pytest
from main import ListComparator
# Тесты для класса ListComparator
def test_list_comparator_equal():
    comparator = ListComparator([1, 2, 3], [1, 2, 3])
    assert comparator.compare_averages() == "Средние значения равны"

def test_list_comparator_first_higher():
    comparator = ListComparator([4, 5, 6], [1, 2, 3])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_list_comparator_second_higher():
    comparator = ListComparator([1, 2, 3], [4, 5, 6])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_list_comparator_empty_lists():
    comparator = ListComparator([], [])
    assert comparator.compare_averages() == "Средние значения равны"

def test_list_comparator_first_empty():
    comparator = ListComparator([], [1, 2, 3])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_list_comparator_second_empty():
    comparator = ListComparator([1, 2, 3], [])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"
