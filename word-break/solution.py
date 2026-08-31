class Solution:
    def wordBreak(
        self,
        s: str,
        wordDict: list[str],
    ) -> bool:
        cache_dict: dict[int, bool] = {}

        def can_break(i: int) -> bool:
            if i == len(s):
                return True

            if i in cache_dict:
                return cache_dict[i]

            for word in wordDict:
                if s.startswith(word, i) and can_break(i + len(word)):
                    cache_dict[i] = True
                    return True

            cache_dict[i] = False
            return False

        result = can_break(0)
        return result
