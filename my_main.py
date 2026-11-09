# my_main.py
# Author: Syan Patel

from my_assistant import LibraryAssistant
from my_tool import BookLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Stacy, a helpful assistant for the Bayside Public Library.
Answer in one short sentence.
The library is open 9 am to 8 pm Monday through Saturday and is closed on Sunday.
The library is located at 120 Main Street.
Members can borrow up to 5 items at a time for 3 weeks.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the patron to a librarian."""

BOOKS = {
    "dune": 3,
    "the hobbit": 0,
    "1984": 2,
}

book_tool = BookLookup(BOOKS)
model = OllamaModel(MODEL_NAME)
stacy = LibraryAssistant("Stacy", INSTRUCTIONS, book_tool, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{stacy.name}: {stacy.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(stacy.history)}")
