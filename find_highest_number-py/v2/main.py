from highest_number_finder import HighestNumberFinder

def main():
    finder = HighestNumberFinder()
    numbers = [3, 17, 9, 5]
    result = finder.find_highest_number(numbers)
    print(f"V2: The highest number is: {result}")

if __name__ == "__main__":
    main()
