from typing import List, Dict
from collections import defaultdict, deque


class WordLadderVisualizer:
    """
    Visualize how Bidirectional BFS explores fewer nodes than Regular BFS
    """

    def __init__(self):
        self.regular_explored = []
        self.bidirectional_explored = []

    def can_transform(self, word1: str, word2: str) -> bool:
        """Check if two words differ by exactly one character"""
        if len(word1) != len(word2):
            return False
        diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
        return diff_count == 1

    def build_graph(self, words: List[str]) -> Dict[str, List[str]]:
        """Build adjacency graph of word transformations"""
        graph = defaultdict(list)
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i != j and self.can_transform(word1, word2):
                    graph[word1].append(word2)
        return dict(graph)

    def regular_bfs_with_tracking(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        """Regular BFS that tracks exploration order"""
        self.regular_explored = []

        if endWord not in wordList:
            return 0

        graph = self.build_graph([beginWord] + wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()
            self.regular_explored.append((word, level))

            if word == endWord:
                return level

            for neighbor in graph.get(word, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

        return 0

    def bidirectional_bfs_with_tracking(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        """Bidirectional BFS that tracks exploration order"""
        self.bidirectional_explored = []

        if endWord not in wordList:
            return 0

        if beginWord == endWord:
            return 1

        graph = self.build_graph([beginWord] + wordList)

        begin_queue = deque([(beginWord, 1, "forward")])
        end_queue = deque([(endWord, 1, "backward")])

        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}

        while begin_queue or end_queue:
            # Process forward direction
            if begin_queue:
                word, level, direction = begin_queue.popleft()
                self.bidirectional_explored.append((word, level, direction))

                for neighbor in graph.get(word, []):
                    if neighbor in end_visited:
                        total_distance = level + end_visited[neighbor]
                        return total_distance

                    if neighbor not in begin_visited:
                        begin_visited[neighbor] = level + 1
                        begin_queue.append((neighbor, level + 1, "forward"))

            # Process backward direction
            if end_queue:
                word, level, direction = end_queue.popleft()
                self.bidirectional_explored.append((word, level, direction))

                for neighbor in graph.get(word, []):
                    if neighbor in begin_visited:
                        total_distance = level + begin_visited[neighbor]
                        return total_distance

                    if neighbor not in end_visited:
                        end_visited[neighbor] = level + 1
                        end_queue.append((neighbor, level + 1, "backward"))

        return 0

    def print_exploration_comparison(
        self, beginWord: str, endWord: str, wordList: List[str]
    ):
        """Print detailed comparison of exploration patterns"""
        print(f"🎯 WORD LADDER EXPLORATION: {beginWord} -> {endWord}")
        print("=" * 70)

        # Run both algorithms
        regular_distance = self.regular_bfs_with_tracking(beginWord, endWord, wordList)
        bidirectional_distance = self.bidirectional_bfs_with_tracking(
            beginWord, endWord, wordList
        )

        print(f"📈 REGULAR BFS (explored {len(self.regular_explored)} nodes):")
        print("   Level | Words Explored")
        print("   ------|---------------")

        current_level = 1
        level_words = []
        for word, level in self.regular_explored:
            if level != current_level:
                if level_words:
                    print(f"   {current_level:4d}  | {' -> '.join(level_words)}")
                level_words = [word]
                current_level = level
            else:
                level_words.append(word)
        if level_words:
            print(f"   {current_level:4d}  | {' -> '.join(level_words)}")

        print(
            f"\n📉 BIDIRECTIONAL BFS (explored {len(self.bidirectional_explored)} nodes):"
        )
        print("   Level | Direction | Words Explored")
        print("   ------|-----------|---------------")

        for word, level, direction in self.bidirectional_explored:
            direction_arrow = "→" if direction == "forward" else "←"
            print(f"   {level:4d}  | {direction:9s} {direction_arrow} | {word}")

        print("\n🏆 RESULTS:")
        print(
            f"   Regular BFS:      Distance = {regular_distance}, Nodes = {len(self.regular_explored)}"
        )
        print(
            f"   Bidirectional BFS: Distance = {bidirectional_distance}, Nodes = {len(self.bidirectional_explored)}"
        )

        if len(self.regular_explored) > 0:
            efficiency = (
                (len(self.regular_explored) - len(self.bidirectional_explored))
                / len(self.regular_explored)
                * 100
            )
            print(f"   Efficiency gain: {efficiency:.1f}% fewer nodes explored")


def create_comprehensive_test():
    """Create a test case that better demonstrates the difference"""
    # Create a more complex word list with clear transformation paths
    words = [
        "cat",
        "bat",
        "bet",
        "bot",
        "bit",
        "sit",
        "set",
        "get",
        "got",
        "hot",
        "hit",
        "hat",
        "rat",
        "mat",
        "met",
        "net",
        "not",
        "nit",
        "nut",
        "but",
        "cut",
        "cot",
        "dot",
        "dog",
        "dig",
        "big",
        "bag",
        "bad",
        "bed",
        "red",
        "rod",
        "nod",
        "mod",
        "mad",
        "pad",
        "pan",
        "can",
        "man",
        "men",
        "den",
        "pen",
        "pet",
        "pit",
        "pot",
        "pat",
        "fat",
        "fit",
        "fir",
        "far",
        "car",
    ]

    visualizer = WordLadderVisualizer()

    print("🧪 COMPREHENSIVE TEST CASE")
    print("Dictionary size:", len(words))
    print("Sample words:", words[:10], "...")
    print()

    # Test case that shows clear difference
    visualizer.print_exploration_comparison("cat", "dog", words)


def explain_bidirectional_concept():
    """Explain the mathematical advantage of bidirectional search"""
    print("\n" + "=" * 70)
    print("🧠 WHY BIDIRECTIONAL BFS IS MORE EFFICIENT")
    print("=" * 70)
    print()
    print("🔍 REGULAR BFS:")
    print("   • Explores nodes level by level from start")
    print("   • At depth d, explores up to b^d nodes (b = branching factor)")
    print("   • Total nodes explored: 1 + b + b² + ... + b^d = O(b^d)")
    print()
    print("🔍 BIDIRECTIONAL BFS:")
    print("   • Searches from both start and end simultaneously")
    print("   • Each search goes to depth d/2")
    print("   • Total nodes explored: 2 × (1 + b + ... + b^(d/2)) = O(b^(d/2))")
    print()
    print("📊 COMPARISON:")
    print("   If b=10 and d=6:")
    print("   • Regular BFS: ~1,000,000 nodes")
    print("   • Bidirectional BFS: ~2,000 nodes")
    print("   • Speedup: 500x faster!")
    print()
    print("🎯 KEY OPTIMIZATIONS:")
    print("   1. Always expand the smaller frontier")
    print("   2. Use sets for O(1) intersection checking")
    print("   3. Remove visited nodes to prevent cycles")
    print("   4. Early termination when frontiers meet")


def main():
    create_comprehensive_test()
    explain_bidirectional_concept()


if __name__ == "__main__":
    main()
