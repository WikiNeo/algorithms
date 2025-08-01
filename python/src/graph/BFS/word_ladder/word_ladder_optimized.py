from typing import List


class WordLadderOptimized:
    """
    Highly optimized Word Ladder solution using Bidirectional BFS

    Key Optimizations:
    1. Bidirectional search: O(b^(d/2)) instead of O(b^d)
    2. Always expand smaller frontier
    3. Early termination when frontiers meet
    4. Set-based operations for O(1) lookups
    5. In-place string generation to avoid overhead
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Find shortest transformation sequence length

        Time: O(M² × N) where M = word length, N = dictionary size
        Space: O(N) for word set and frontiers
        """
        # Convert to set for O(1) membership testing
        word_set = set(wordList)

        # Early exit: target not reachable
        if endWord not in word_set:
            return 0

        # Special case: already at target
        if beginWord == endWord:
            return 1

        # Initialize bidirectional frontiers
        forward_frontier = {beginWord}
        backward_frontier = {endWord}

        # Remove from word_set to avoid revisiting
        word_set.discard(beginWord)
        word_set.discard(endWord)

        distance = 1

        while forward_frontier and backward_frontier:
            # 🎯 KEY OPTIMIZATION: Always expand the smaller frontier
            # This keeps the search balanced and minimizes total work
            if len(forward_frontier) > len(backward_frontier):
                forward_frontier, backward_frontier = (
                    backward_frontier,
                    forward_frontier,
                )

            next_frontier = set()

            # Expand current frontier
            for word in forward_frontier:
                # Try all possible single-character transformations
                word_list = list(word)  # Convert to list for efficient modification

                for i in range(len(word_list)):
                    original_char = word_list[i]

                    # Try all 26 possible characters
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original_char:
                            continue

                        word_list[i] = c
                        candidate = "".join(word_list)

                        # 🎯 TERMINATION: Frontiers meet!
                        if candidate in backward_frontier:
                            return distance + 1

                        # Add valid transformations to next frontier
                        if candidate in word_set:
                            next_frontier.add(candidate)
                            word_set.remove(candidate)  # Mark as visited

                    # Restore original character
                    word_list[i] = original_char

            # Move to next level
            forward_frontier = next_frontier
            distance += 1

        return 0  # No path exists

    def ladderLength_with_optimizations_explained(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        """
        Same algorithm with detailed optimization explanations
        """
        print(f"🎯 Starting bidirectional search: {beginWord} -> {endWord}")

        word_set = set(wordList)
        if endWord not in word_set:
            print("❌ Early exit: endWord not in dictionary")
            return 0

        forward_frontier = {beginWord}
        backward_frontier = {endWord}
        word_set.discard(beginWord)
        word_set.discard(endWord)

        distance = 1

        while forward_frontier and backward_frontier:
            print(f"\n📊 Level {distance}:")
            print(f"   Forward frontier size: {len(forward_frontier)}")
            print(f"   Backward frontier size: {len(backward_frontier)}")

            # Choose smaller frontier
            if len(forward_frontier) > len(backward_frontier):
                forward_frontier, backward_frontier = (
                    backward_frontier,
                    forward_frontier,
                )
                print("   🔄 Swapped frontiers (expanding smaller one)")

            print(f"   🔍 Expanding: {forward_frontier}")

            next_frontier = set()

            for word in forward_frontier:
                word_list = list(word)
                for i in range(len(word_list)):
                    original_char = word_list[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original_char:
                            continue

                        word_list[i] = c
                        candidate = "".join(word_list)

                        if candidate in backward_frontier:
                            print(f"   🎉 FRONTIERS MEET at '{candidate}'!")
                            return distance + 1

                        if candidate in word_set:
                            next_frontier.add(candidate)
                            word_set.remove(candidate)

                    word_list[i] = original_char

            print(f"   ➡️ Next frontier: {next_frontier}")
            forward_frontier = next_frontier
            distance += 1

        print("❌ No path found")
        return 0


def demonstrate_optimizations():
    """Show the optimized algorithm in action"""
    solver = WordLadderOptimized()

    print("🚀 OPTIMIZED WORD LADDER WITH BIDIRECTIONAL BFS")
    print("=" * 60)

    # Test case
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print("📝 Test Case:")
    print(f"   Begin: {beginWord}")
    print(f"   End: {endWord}")
    print(f"   Dictionary: {wordList}")

    # Show detailed execution
    result = solver.ladderLength_with_optimizations_explained(
        beginWord, endWord, wordList
    )
    print(f"\n🏆 Final Result: {result}")

    print("\n💡 KEY OPTIMIZATIONS USED:")
    print("✅ Bidirectional search reduces from O(b^d) to O(b^(d/2))")
    print("✅ Always expand smaller frontier keeps search balanced")
    print("✅ Set operations provide O(1) membership testing")
    print("✅ Early termination when frontiers meet")
    print("✅ Remove visited words to prevent cycles")


if __name__ == "__main__":
    demonstrate_optimizations()
