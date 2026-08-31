TEST_CASES = [ # type: ignore
    {
        "method": "wordBreak",
        "args": [
            "leetcode",
            ["leet", "code"],
        ],
        "expected": True,
    },
    {
        "method": "wordBreak",
        "args": [
            "applepenapple",
            ["apple", "pen"],
        ],
        "expected": True,
    },
    {
        "method": "wordBreak",
        "args": [
            "catsandog",
            ["cats", "dog", "sand", "and", "cat"],
        ],
        "expected": False,
    },
]