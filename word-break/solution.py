class Solution:
    def wordBreak(
        self,
        s: str,
        wordDict: list[str],
    ) -> bool:
        word_set = set(wordDict)
        memo_set = {}

        def can_break(i: int) -> bool:
            for word in word_set:
                if s.startswith(word, i) and can_break(i + len(word)):
                    memo_set[i] = True
                    return True

            memo_set[i] = False
            return False

        return can_break(0)
