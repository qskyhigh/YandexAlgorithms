from typing import List
import unittest
from dataclasses import dataclass

class Solution:

    def func(self, numbers: List[int]) -> str:
        i, count_a, count_b = 0, 0, 0
        while i < len(numbers):
            if numbers[i] % 2 == 0 or numbers[i] == 0:
                count_a += 1
            else:
                count_b += 1
            i += 1

        if count_a == len(numbers) or count_b == len(numbers):
            return 'WIN'
        else:
            return 'FAIL'

@dataclass
class TestCase:
    numbers: List[int]
    expectation: str

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, -3, 7], 'FAIL'),
            TestCase([7, 11, 7], 'WIN'),
            TestCase([6, -2, 0], 'WIN')

        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.func(t.numbers), t.expectation)
