# my_assistant.py
# Author: Syan Patel

HANDOFF_WORDS = ["fee", "fine", "pay", "card"]
BOOK_WORDS = ["available", "book", "copies"]


class LibraryAssistant:
    """A library assistant. Rules handle what must be right. A model handles the rest."""

    def __init__(self, name, instructions, book_tool, model):
        """Set up one assistant with its own name, instructions, tool, model, and history."""
        self.name = name
        self.instructions = instructions
        self.book_tool = book_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Use a rule when one applies. Otherwise ask the model."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a librarian."
        if self.is_book_question(text):
            return self.book_reply(user_message)
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply

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
