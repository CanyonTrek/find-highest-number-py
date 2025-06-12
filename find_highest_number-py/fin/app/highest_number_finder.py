class HighestNumberFinder:
    def find_highest_number(self, numbers):
        if not isinstance(numbers, list) or not numbers:
            return None
        return max(n for n in numbers if isinstance(n, (int, float)))
