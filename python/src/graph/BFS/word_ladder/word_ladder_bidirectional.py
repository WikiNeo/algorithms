from typing import List


class WordLadderBidirectional:
    """
    Word Ladder problem solved using Bidirectional BFS

    Time Complexity: O(M^2 * N) where M = word length, N = dictionary size
    Space Complexity: O(N)

    Bidirectional BFS reduces the search space from O(b^d) to O(b^(d/2))
    where b = branching factor, d = depth
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert to set for O(1) lookup
        word_set = set(wordList)

        # Early termination - endWord must be in dictionary
        if endWord not in word_set:
            return 0

        # Special case: beginWord and endWord are the same
        if beginWord == endWord:
            return 1

        # Initialize two frontiers
        begin_set = {beginWord}
        end_set = {endWord}

        # Track visited words from both directions
        word_set.discard(beginWord)  # Remove to avoid revisiting
        word_set.discard(endWord)

        # Start with distance 1 (beginWord -> firstTransformation)
        distance = 1

        while begin_set and end_set:
            # Key optimization: always expand the smaller frontier
            # This keeps the search balanced and reduces total work
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            # Get next level of current frontier
            next_begin_set = set()

            for word in begin_set:
                # Try all possible single-character changes
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:  # Skip same character
                            continue

                        next_word = word[:i] + c + word[i + 1 :]

                        # Check if we've met the other frontier
                        if next_word in end_set:
                            return distance + 1

                        # Add to next frontier if valid and unvisited
                        if next_word in word_set:
                            next_begin_set.add(next_word)
                            word_set.remove(next_word)

            # Move to next level
            begin_set = next_begin_set
            distance += 1

        return 0  # No path found

    def ladderLength_with_path(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> tuple:
        """
        Returns both the shortest distance and the actual path
        Useful for debugging and understanding the transformation sequence
        """
        word_set = set(wordList)

        if endWord not in word_set:
            return 0, []

        if beginWord == endWord:
            return 1, [beginWord]

        # Track parent relationships for path reconstruction
        begin_parents = {beginWord: None}
        end_parents = {endWord: None}

        begin_set = {beginWord}
        end_set = {endWord}

        word_set.discard(beginWord)
        word_set.discard(endWord)

        distance = 1
        meeting_word = None

        while begin_set and end_set and not meeting_word:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                begin_parents, end_parents = end_parents, begin_parents

            next_begin_set = set()

            for word in begin_set:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        next_word = word[:i] + c + word[i + 1 :]

                        if next_word in end_set:
                            meeting_word = next_word
                            begin_parents[next_word] = word
                            break

                        if next_word in word_set:
                            next_begin_set.add(next_word)
                            begin_parents[next_word] = word
                            word_set.remove(next_word)

                if meeting_word:
                    break

            begin_set = next_begin_set
            distance += 1

        if not meeting_word:
            return 0, []

        # Reconstruct path
        path = self._reconstruct_path(
            beginWord, endWord, meeting_word, begin_parents, end_parents
        )
        return distance, path

    def _reconstruct_path(
        self,
        beginWord: str,
        endWord: str,
        meeting_word: str,
        begin_parents: dict,
        end_parents: dict,
    ) -> List[str]:
        """Reconstruct the shortest path from parent tracking"""
        # Build path from begin to meeting point
        begin_path = []
        current = meeting_word
        while current is not None:
            begin_path.append(current)
            current = begin_parents[current]
        begin_path.reverse()

        # Build path from meeting point to end
        end_path = []
        current = end_parents[meeting_word]  # Skip meeting_word to avoid duplication
        while current is not None:
            end_path.append(current)
            current = end_parents[current]

        return begin_path + end_path


def demonstrate_bidirectional_bfs():
    """Demonstrate the bidirectional BFS with examples"""
    solver = WordLadderBidirectional()

    # Example 1: Classic case
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    distance = solver.ladderLength(beginWord, endWord, wordList)
    distance_with_path, path = solver.ladderLength_with_path(
        beginWord, endWord, wordList
    )

    print("Example 1:")
    print(f"Begin: {beginWord}, End: {endWord}")
    print(f"Dictionary: {wordList}")
    print(f"Shortest distance: {distance}")
    print(f"Path: {' -> '.join(path)}")
    print()

    # Example 2: No solution
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]  # Missing "cog"

    distance2 = solver.ladderLength(beginWord2, endWord2, wordList2)
    print("Example 2 (no solution):")
    print(f"Begin: {beginWord2}, End: {endWord2}")
    print(f"Dictionary: {wordList2}")
    print(f"Shortest distance: {distance2}")
    print()

    # Example 3: Longer transformation
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]

    distance3 = solver.ladderLength(beginWord3, endWord3, wordList3)
    distance_with_path3, path3 = solver.ladderLength_with_path(
        beginWord3, endWord3, wordList3
    )
    print("Example 3:")
    print(f"Begin: {beginWord3}, End: {endWord3}")
    print(f"Dictionary: {wordList3}")
    print(f"Shortest distance: {distance3}")
    print(f"Path: {' -> '.join(path3)}")


if __name__ == "__main__":
    demonstrate_bidirectional_bfs()
