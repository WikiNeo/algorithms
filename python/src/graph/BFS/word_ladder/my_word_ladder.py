from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        # special case
        if endWord not in word_set:
            return 0

        # bidirectional frontiers
        forward_frontier = {beginWord}
        backward_frontier = {endWord}

        # wordSet update
        word_set.discard(beginWord)
        word_set.discard(endWord)

        # result
        distance = 1

        # search from both frontiers
        while forward_frontier and backward_frontier:
            # always expand smaller frontier
            if len(forward_frontier) > len(backward_frontier):
                forward_frontier, backward_frontier = (
                    backward_frontier,
                    forward_frontier,
                )

            # initialize next frontier
            next_frontier = set()

            # expand forward frontier
            for word in forward_frontier:
                for i in range(len(word)):
                    for j in range(26):
                        c = chr(ord('a') + j)
                        next_word = word[:i] + c + word[i + 1 :]

                        # early termination
                        if next_word in backward_frontier:
                            return distance + 1

                        if next_word in word_set:
                            next_frontier.add(next_word)
                            word_set.remove(next_word)

            forward_frontier = next_frontier
            distance += 1

        return 0
