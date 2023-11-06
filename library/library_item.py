class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been checked in."
        else:
            return f"{self.title} is already checked in."
