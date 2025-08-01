import time
from typing import List
from collections import deque


class WordLadderComparison:
    """
    Compare Regular BFS vs Bidirectional BFS for Word Ladder problem
    """

    def __init__(self):
        self.regular_bfs_nodes_explored = 0
        self.bidirectional_bfs_nodes_explored = 0

    def regular_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Traditional BFS approach"""
        self.regular_bfs_nodes_explored = 0
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()
            self.regular_bfs_nodes_explored += 1

            # Generate all possible next words
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    next_word = word[:i] + c + word[i + 1 :]

                    if next_word == endWord:
                        return level + 1

                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

        return 0

    def bidirectional_bfs(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        """Bidirectional BFS approach"""
        self.bidirectional_bfs_nodes_explored = 0
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        if beginWord == endWord:
            return 1

        begin_set = {beginWord}
        end_set = {endWord}

        word_set.discard(beginWord)
        word_set.discard(endWord)

        distance = 1

        while begin_set and end_set:
            # Always expand the smaller frontier (key optimization!)
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            self.bidirectional_bfs_nodes_explored += len(begin_set)
            next_begin_set = set()

            for word in begin_set:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        next_word = word[:i] + c + word[i + 1 :]

                        # Check if frontiers meet
                        if next_word in end_set:
                            return distance + 1

                        if next_word in word_set:
                            next_begin_set.add(next_word)
                            word_set.remove(next_word)

            begin_set = next_begin_set
            distance += 1

        return 0

    def compare_algorithms(self, beginWord: str, endWord: str, wordList: List[str]):
        """Compare both algorithms and show metrics"""
        print(f"🔍 Comparing algorithms for: {beginWord} -> {endWord}")
        print(f"Dictionary size: {len(wordList)}")
        print("-" * 60)

        # Test Regular BFS
        start_time = time.time()
        regular_result = self.regular_bfs(beginWord, endWord, wordList)
        regular_time = time.time() - start_time

        # Test Bidirectional BFS
        start_time = time.time()
        bidirectional_result = self.bidirectional_bfs(beginWord, endWord, wordList)
        bidirectional_time = time.time() - start_time

        # Results
        print("📊 RESULTS:")
        print("Regular BFS:")
        print(f"  ├─ Distance: {regular_result}")
        print(f"  ├─ Nodes explored: {self.regular_bfs_nodes_explored}")
        print(f"  └─ Time: {regular_time:.6f}s")
        print()
        print("Bidirectional BFS:")
        print(f"  ├─ Distance: {bidirectional_result}")
        print(f"  ├─ Nodes explored: {self.bidirectional_bfs_nodes_explored}")
        print(f"  └─ Time: {bidirectional_time:.6f}s")
        print()

        if self.regular_bfs_nodes_explored > 0:
            efficiency = (
                (
                    self.regular_bfs_nodes_explored
                    - self.bidirectional_bfs_nodes_explored
                )
                / self.regular_bfs_nodes_explored
                * 100
            )
            print("🚀 PERFORMANCE IMPROVEMENT:")
            print(f"  ├─ Nodes reduction: {efficiency:.1f}%")
            print(
                f"  ├─ Time speedup: {regular_time / bidirectional_time:.2f}x faster"
                if bidirectional_time > 0
                else ""
            )
            print(
                f"  └─ Space efficiency: {self.bidirectional_bfs_nodes_explored}/{self.regular_bfs_nodes_explored} nodes"
            )
        print("=" * 60)


def generate_large_test_case():
    """Generate a larger test case to see the performance difference more clearly"""

    # Generate some 3-letter words
    base_words = [
        "cat",
        "bat",
        "rat",
        "hat",
        "mat",
        "sat",
        "pat",
        "fat",
        "car",
        "bar",
        "far",
        "tar",
        "war",
        "can",
        "ban",
        "fan",
        "man",
        "pan",
        "ran",
        "tan",
        "van",
        "cap",
        "gap",
        "lap",
        "map",
        "nap",
        "rap",
        "sap",
        "tap",
        "bag",
        "dag",
        "gag",
        "hag",
        "jag",
        "lag",
        "nag",
        "rag",
        "sag",
        "tag",
        "wag",
    ]

    return base_words


def main():
    """Run comparisons with different test cases"""
    comparator = WordLadderComparison()

    print("🎯 WORD LADDER: Regular BFS vs Bidirectional BFS")
    print("=" * 60)

    # Test Case 1: Classic example
    print("TEST CASE 1: Classic Example")
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    comparator.compare_algorithms("hit", "cog", wordList1)

    # Test Case 2: Larger dictionary
    print("TEST CASE 2: Larger Dictionary")
    large_wordList = generate_large_test_case()
    comparator.compare_algorithms("cat", "dog", large_wordList)

    # Test Case 3: No solution
    print("TEST CASE 3: No Solution")
    no_solution_list = ["hot", "dot", "lot", "log"]  # Missing "cog"
    comparator.compare_algorithms("hit", "cog", no_solution_list)

    print("\n💡 KEY INSIGHTS:")
    print("• Bidirectional BFS shines with larger search spaces")
    print("• Both algorithms have same time complexity O(M²×N) but different constants")
    print("• Bidirectional BFS reduces nodes explored from O(b^d) to O(b^(d/2))")
    print("• The 'smaller frontier first' optimization keeps search balanced")


if __name__ == "__main__":
    main()
