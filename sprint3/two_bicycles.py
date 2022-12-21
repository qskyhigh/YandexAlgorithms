"""
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.
У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.
Ваша задача — по заданной стоимости велосипеда определить первый день, в которой Вася смог бы купить один велосипед, и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).
Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.
В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.
В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.
Формат вывода
Нужно вывести два числа — номера дней по условию задачи.
Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.
"""

from typing import List
import unittest
from dataclasses import dataclass


class Solution:

    def func(self, money: List[int], price: int) -> List[int]:
        result = []

        def binary_search(nums: List[int], target: int, low: int, high: int) -> int:
            if high <= low != 0:
                return -1
            mid = (low + high) // 2
            if nums[mid] >= target and (nums[mid - 1] < target or mid == 0):
                return mid + 1
            elif target <= nums[mid]:
                return binary_search(nums, target, low, mid)
            else:
                return binary_search(nums, target, mid + 1, high)

        result.append(binary_search(money, price, 0, len(money)))
        result.append(binary_search(money, price * 2, 0, len(money)))
        return result


@dataclass
class TestCase:
    numbers: List[int]
    target: int
    expectation: List[int]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 4, 4, 6, 8], 3, [3, 5]),
            TestCase([1, 2, 4, 4, 4, 4], 3, [3, -1]),
            TestCase([1, 2, 4, 4, 4, 4], 10, [-1, -1])

        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.func(t.numbers, t.target), t.expectation)
