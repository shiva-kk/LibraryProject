from library.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, item_id, page_count):
        super().__init__(title, author, item_id)
        self.page_count = page_count
