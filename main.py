# It will ask for a book name, author name, then
# send to llm, and then return the book synopsis,
# genre, year and save record to json history file
from llm import ask_llm
from datahandling import add_to_json
def main():
    while True:
        print("Enter details to know book details, press enter if you'd like to exit")
        book_name = input("What book would you like to know about? \n")
        author_name = input("Do you happen to know the author too? \n")

        if not book_name and not author_name:
            break
        print("Thanks for the info, pls wait a moment!")
        ask_llm(book_name, author_name)

if __name__ == "__main__":
    main()