from highest_number_finder import HighestNumberFinder

def main():
    finder = HighestNumberFinder()
    numbers = [5, 12, 7, 20]
    result = finder.find_highest_number(numbers)
    print(f"V4: The highest number using sort is: {result}")

if __name__ == "__main__":
    main()
