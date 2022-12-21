"""
Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях (ПСП), состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке – алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.
Помогите Рите – напишите программу, которая по заданному n выведет все ПСП в нужном порядке.
Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. Таких всего две:

(())
()()

(()) идёт раньше ()(), так как первый символ у них одинаковый, а на второй позиции у первой ПСП стоит (, который идёт раньше ).

Формат ввода
На вход функция принимает n — целое число от 0 до 10.
Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной длины в алфавитном (лексикографическом) порядке.
https://neerc.ifmo.ru/wiki/index.php?title=%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8
"""

from typing import List
import unittest
from dataclasses import dataclass


class Solution:

    def main(self, n) -> List[str]:
        result = []
        def bracket_generator(n, counter_open, counter_close, ans):
            if counter_open + counter_close == 2 * n:
                result.append(ans)
            if counter_open < n:
                bracket_generator(n, counter_open + 1, counter_close, ans + "(")
            if counter_open > counter_close:
                bracket_generator(n, counter_open, counter_close + 1, ans + ")")

        bracket_generator(n, 0, 0, '')
        return result


@dataclass
class TestCase:
    number: int
    expectation: List[str]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase(2, ['(())', '()()']),
            TestCase(3, ['((()))', '(()())', '(())()', '()(())', '()()()'])
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.main(t.number), t.expectation)
