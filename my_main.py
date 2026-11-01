# my_main.py
# Author: Syan Patel

from my_assistant import LibraryAssistant
from my_tool import BookLookup

BOOKS = {
    "dune": 3,
    "the hobbit": 0,
    "1984": 2,
}

book_tool = BookLookup(BOOKS)
stacy = LibraryAssistant(
    "Stacy",
    "You are a helpful assistant for the Bayside Public Library.",
    book_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{stacy.name}: {stacy.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(stacy.history)}")
