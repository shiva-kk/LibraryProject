from library.library_item import LibraryItem
from library.book import Book
from library.dvd import DVD
from library.magazine import Magazine
from library.audio_cd import AudioCD 

def main(): # Create library items of different types
    book = Book("The Catcher in the Rye", "J.D. Salinger", 101, 234)
    dvd = DVD("Inception", "Christopher Nolan", 201, 148)
    magazine = Magazine("National Geographic", "National Geographic",301, 5)
    audio_cd = AudioCD("Abbey Road", "The Beatles", 401, 44)

    # Demonstrate checking in and out library items
    print(book.check_out())  # Check out the book
    print(dvd.check_out())   # Check out the DVD
    print(magazine.check_in())  # Check in the magazine
    print(audio_cd.check_out())  # Check out the audio CD

    # Display information about the items
    print(f"Book Title: {book.title}, Page Count: {book.page_count}")
    print(f"DVD Title: {dvd.title}, Run Time: {dvd.run_time} minutes")
    print(f"Magazine Title: {magazine.title}, Issue Number: {magazine.issue_number}")
    print(f"Audio CD Title: {audio_cd.title}, Duration: {audio_cd.duration} minutes")

if __name__ == "__main__":
    main()




