class HighestNumberFinder:
    def find_highest_number(self, numbers):
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list")
        clean_numbers = [n for n in numbers if isinstance(n, (int, float))]
        return max(clean_numbers) if clean_numbers else None
