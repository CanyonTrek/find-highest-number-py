from app.highest_number_finder import HighestNumberFinder

def main():
    finder = HighestNumberFinder()
    numbers = [10, 'oops', 45.3, -5]
    result = finder.find_highest_number(numbers)
    print(f"FIN: The highest valid number is: {result}")

if __name__ == "__main__":
    main()
