class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Code from Gemini, not mine at all.
        if not digits:
            return []
        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                combinations.append(combination)
                return

            letters = digit_to_letters[next_digits[0]]
            for letter in letters:
                backtrack(combination + letter, next_digits[1:])

        combinations = []
        backtrack("", digits)
        return combinations


if __name__ == "__main__":
    sol = Solution()
    # Expected result: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(sol.letterCombinations("23"))
    # Expected result: []
    print(sol.letterCombinations(""))
    # Expected result: ["a","b","c"]
    print(sol.letterCombinations("2"))
