class HighestNumberFinder:
    def find_highest_number(self, numbers):
        try:
            return sorted(numbers, reverse=True)[0]
        except Exception:
            return None
