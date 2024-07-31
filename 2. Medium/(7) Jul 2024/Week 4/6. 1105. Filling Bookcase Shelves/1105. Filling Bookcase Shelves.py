def minHeightShelves(books: list[list[int]], shelfWidth: int) -> int:

    def rec(available_width: int, book_index: int, curr_height):
        if available_width < 0:
            return float('inf')
        if book_index == len(books):
            return curr_height
        
        book_width, book_height = books[book_index]

        # Put the book on current shelf
        same_shelf = rec(available_width - book_width, book_index + 1, max(curr_height, book_height))
        # Put the book on a new shelf
        new_shelf = curr_height + rec(shelfWidth - book_width, book_index + 1, book_height)

        return min(same_shelf, new_shelf)

    return rec(shelfWidth, 0, 0)

# W, H
print(minHeightShelves(books = [[1,1],[2,3], [1,1]], shelfWidth = 4))
