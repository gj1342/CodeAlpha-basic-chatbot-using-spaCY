# Basic Chatbot with spaCy

## Description

This Python script (`basic_chatbot.py`) implements a simple conversational chatbot using the spaCy library for Natural Language Processing (NLP). The chatbot is designed to understand basic user inputs, recognize named entities, and generate appropriate responses. It handles multiple entity types and provides a friendly conversational experience.

## Features

-   **Named Entity Recognition (NER):** Uses spaCy to identify and extract various named entities from user input, such as persons, locations, organizations, dates, and more.
-   **Multiple Entity Type Handling:** Responds to a wide range of entity types with tailored responses.
-   **Basic Conversation Flow:** Includes greetings, farewells, and a fallback response for unrecognized inputs.
-   **Exit Functionality:** Allows users to exit the chat by typing "exit," "quit," or "bye."
-   **User Input Validation:** Skips empty user inputs.

## Prerequisites

-   Python 3.x
-   spaCy library (`pip install spacy`)
-   spaCy English language model (`python -m spacy download en_core_web_sm`)

## Installation

1.  **Clone the repository (or download the `basic_chatbot.py` file):**

    ```bash
    git clone <repository_url> # If you have a repository
    ```

2.  **Install spaCy and the English language model:**

    ```bash
    pip install spacy
    python -m spacy download en_core_web_sm
    ```

## Usage

1.  **Run the script:**

    ```bash
    python basic_chatbot.py
    ```

2.  **Interact with the chatbot:**

    -   Type your messages in the console.
    -   The chatbot will respond based on your input and recognized entities.
    -   Type "exit," "quit," or "bye" to end the conversation.

## Code Structure

-   `basic_chatbot.py`: Contains the chatbot implementation.
    -   `get_entities(text)`: Extracts named entities from the given text.
    -   `generate_response(user_input)`: Generates a response based on user input and recognized entities.
    -   `main()`: Runs the chatbot in a loop.

## Example Interactions

```bash
$ python basic_chatbot.py
Chatbot: Hello! I am your basic chatbot. Type 'exit' or 'quit' to stop.
You: Hello, my name is John and I live in London.
Chatbot: Hello there! How can I help you today? Oh, you're talking about John. Interesting! I see you're talking about London. I'd love to visit there someday!
You: What do you know about Microsoft?
Chatbot: Microsoft is definitely worth discussing!
You: Bye!
Chatbot: It was nice chatting with you! Goodbye!
$
