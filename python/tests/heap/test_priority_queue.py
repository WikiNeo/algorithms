import unittest

from src.heap import priority_queue


class TestPriorityQueue(unittest.TestCase):
    def test_priority_queue(self):
        priority_queue.add_task("wake up", 0)
        priority_queue.add_task("brush teeth", 1)
        priority_queue.add_task("wash face", 1)
        priority_queue.add_task("eat breakfast", 2)

        task = priority_queue.pop_task()
        self.assertEqual(task, "wake up")

        task = priority_queue.pop_task()
        self.assertEqual(task, "brush teeth")

        priority_queue.remove_task("wash face")

        task = priority_queue.pop_task()
        self.assertEqual(task, "eat breakfast")
