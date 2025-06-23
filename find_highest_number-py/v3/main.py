from app.highest_number_finder import HighestNumberFinder

def main():
    finder = HighestNumberFinder()
    numbers = [3, 'a', 17, 9.5]
    result = finder.find_highest_number(numbers)
    print(f"V3: The highest valid number is: {result}")

if __name__ == "__main__":
    main()
