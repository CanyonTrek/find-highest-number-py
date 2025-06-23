class HighestNumberFinder:
    def find_highest_number(self, numbers):
        """
        Returns the highest numeric value (int or float) from a list.
        Non-numeric values are ignored. If the input is not iterable or contains 
        no numeric values, returns None.
        Parameters:
            numbers (iterable): A list or iterable containing values.

        Returns:
            int or float or None: The highest numeric value, or None if invalid.
        """
        try:
            return max(n for n in numbers if isinstance(n, (int, float)))
        except (TypeError, ValueError):
            return None
