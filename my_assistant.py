# my_assistant.py
# Author: Syan Patel

HANDOFF_WORDS = ["fee", "fine", "pay", "card"]
BOOK_WORDS = ["available", "book", "copies"]


class LibraryAssistant:
    """A mock library assistant. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, book_tool):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.book_tool = book_tool
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a librarian."
        if self.is_book_question(text):
            return self.book_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me if a book is available."
        return "I'm not sure how to help with that. I can check if a book is available."

    def needs_human(self, text):
        """Return True if the message is about money or a library account."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def is_book_question(self, text):
        """Return True if the message asks about a book."""
        for word in BOOK_WORDS:
            if word in text:
                return True
        return False

    def book_reply(self, user_message):
        """Use the book tool to answer a question about a book."""
        title = self.book_tool.find_title(user_message)
        if title is None:
            return "Which book? Please tell me the title you want me to check."
        copies = self.book_tool.copies_for(title)
        if copies == 0:
            return f"All copies of {title.title()} are checked out right now."
        return f"Yes! We have {copies} copies of {title.title()} on the shelf."
