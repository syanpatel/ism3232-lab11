from mock_model import MockModel
from my_assistant import LibraryAssistant
from my_tool import BookLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_assistant():
    """Build a fresh assistant with its own tool and a mock model for each test."""
    books = {"dune": 3, "the hobbit": 0}
    return LibraryAssistant("Stacy", "Be helpful.", BookLookup(books), MockModel())


def make_assistant_with_silent_model():
    """Build an assistant whose model never answers."""
    books = {"dune": 3, "the hobbit": 0}
    return LibraryAssistant("Stacy", "Be helpful.", BookLookup(books), SilentModel())


def test_tool_finds_copies_for_known_book():
    tool = BookLookup({"dune": 3})
    assert tool.copies_for("dune") == 3


def test_tool_returns_none_for_unknown_book():
    tool = BookLookup({"dune": 3})
    assert tool.copies_for("harry potter") is None


def test_available_book_uses_the_tool():
    stacy = make_assistant()
    assert (
        stacy.respond("Is Dune available?")
        == "Yes! We have 3 copies of Dune on the shelf."
    )


def test_book_with_no_copies_says_checked_out():
    stacy = make_assistant()
    assert "checked out" in stacy.respond("Is The Hobbit available?")


def test_fee_question_goes_to_a_librarian():
    stacy = make_assistant()
    assert "librarian" in stacy.respond("I need to pay a late fee")


def test_unknown_request_gets_a_safe_reply():
    stacy = make_assistant()
    stacy.respond("Do you have wifi?")
    assert len(stacy.history) == 2
    assert "not sure" in stacy.history[1]["content"]


def test_other_messages_go_to_the_model():
    stacy = make_assistant()
    assert stacy.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer():
    stacy = make_assistant_with_silent_model()
    assert "try again" in stacy.respond("hello")


def test_book_rule_does_not_need_the_model():
    stacy = make_assistant_with_silent_model()
    assert (
        stacy.respond("Is Dune available?")
        == "Yes! We have 3 copies of Dune on the shelf."
    )


def test_handoff_rule_does_not_need_the_model():
    stacy = make_assistant_with_silent_model()
    assert "librarian" in stacy.respond("I need to pay a late fee")
