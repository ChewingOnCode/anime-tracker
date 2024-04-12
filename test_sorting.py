def multi_column_sort(data, sort_criteria):
    """
    Sorts the data based on multiple columns.

    :param data: The data to sort, a list of lists.
    :param sort_criteria: A list of tuples specifying the sorting criteria.
                          Each tuple is (column_index, sort_order),
                          where sort_order is 'asc' for ascending or 'desc' for descending.
    """
    for column_index, sort_order in reversed(sort_criteria):
        data.sort(key=lambda row: row[column_index], reverse=(sort_order == "desc"))


def test_sorting():
    # Sample data: [Title, Genre, Rating]
    data = [
        ["Naruto", "Action", 8],
        ["Bleach", "Action", 7],
        ["One Piece", "Adventure", 9],
        ["Naruto Shippuden", "Action", 9],
        ["Dragon Ball", "Action", 7],
    ]

    # Define the sort criteria:
    # First by Genre in ascending order, then by Rating in descending order
    sort_criteria = [(1, "asc"), (2, "desc")]

    print("Original Data:")
    for item in data:
        print(item)

    multi_column_sort(data, sort_criteria)

    print("\nSorted Data:")
    for item in data:
        print(item)


# Run the test function
test_sorting()
