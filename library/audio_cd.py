from library.library_item import LibraryItem

class AudioCD(LibraryItem):
    def __init__(self, title, artist, item_id, duration):
        super().__init__(title, artist, item_id)
        self.duration = duration
