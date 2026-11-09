# Lab 10: OOP for Agents
## My Assistant: Stacy, the Library Book Finder

Stacy is a library assistant that tells visitors whether a book is on the shelf and how many copies are available.She uses a separate `BookLookup` tool. It's a mock: Stacy's replies come from simple keyword rules instead of an AI model, and the book list is a small hard coded dictionary instead of an actual library catalog. Any message about fees, fines, payments, or library cards is passed to a librarian, because those involve money and visitor's personal account, which a bot should not handle. If Stacy used real visitor data it could expose private information to someone who is not that visitor.


## Week 11: Adding a local model
When I asked "What time do you open on Saturday?", the model answered "The library opens at 9 am on Saturday," which is correct. When I asked "Do you have study rooms?", the model refused and said it did not know, because I didn't include that information in the instructions. The refusal was correct, but it said it would "pass the patron to a librarian," copying the wording of the instructions instead of speaking to me directly. I kept book availability in code, using the BookLookup tool. I also kept the handoff for fees, fines, payments, and library cards in code, because anything involving money or an account should always go to a librarian.