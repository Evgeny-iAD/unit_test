# решение задачи
class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def average(self, lst):
        """average"""
        return sum(lst) / len(lst) if lst else 0

    def compare_averages(self):
        """compare_averages"""
        avg_list1 = self.average(self.list1)
        avg_list2 = self.average(self.list2)

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        elif avg_list2 > avg_list1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

    comparator = ListComparator(l1, l2)
    result = comparator.compare_averages()
    print(result)
