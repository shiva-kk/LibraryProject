from library.library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, run_time):
        super().__init__(title, director, item_id)
        self.run_time = run_time
