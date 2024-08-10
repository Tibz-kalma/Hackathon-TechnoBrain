def get_unique_sorted_integers():
    """Using a function"""
    try:
        integers = list(map(int, input("Enter numbers ").split()))

        # Remove duplicates and sort in descending
        unique_sorted_integers = sorted(set(integers), reverse=True)

        return unique_sorted_integers

    except ValueError:
        print("Invalid input.")
        return []

def main():
    unique_sorted_integers = get_unique_sorted_integers()

    if unique_sorted_integers:
        print("Sorted list = ", unique_sorted_integers)

if __name__ == "__main__":
    main()
