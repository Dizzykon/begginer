# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: FleetCare
import unittest


def _sum_range(n):
    return sum(range(1, n + 1))


class TestFleetCare(unittest.TestCase):
    def test_sum_range(self):
        self.assertEqual(_sum_range(10), 55)
        self.assertEqual(_sum_range(1), 1)
        self.assertEqual(_sum_range(0), 0)

    def test_add(self):
        self.assertEqual(2 + 3, 5)
        self.assertEqual(-1 + 1, 0)

    def test_string_lower(self):
        self.assertEqual("Hello".lower(), "hello")
        self.assertEqual("already".lower(), "already")

    def test_dict_count(self):
        d = {"a": 1, "b": 2, "a": 3}
        self.assertEqual(d["a"], 3)
        self.assertEqual(len(d), 2)


if __name__ == "__main__":
    unittest.main()
