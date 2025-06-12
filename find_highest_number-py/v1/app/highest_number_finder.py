class HighestNumberFinder:
    def find_highest_number(self, numbers):
        if not numbers:
            return None
        highest = numbers[0]
        for num in numbers:
            if num > highest:
                highest = num
        return highest
