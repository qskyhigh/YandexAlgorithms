from typing import List
import unittest
from dataclasses import dataclass

class Solution:

    def func(self, numbers: List[int]) -> int:
        return numbers[0] * numbers[1] * numbers[1] + numbers[2] * numbers[1] + numbers[3]

@dataclass
class TestCase:
    numbers: List[int]
    expectation: int

class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([-8, -5, -2, 7], -183),
            TestCase([8, 2, 9, -10], 40)
        ]

        for t in tests:
            with self.subTest(t):
                self.assertEqual(solution.func(t.numbers), t.expectation)
