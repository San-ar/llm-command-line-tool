from datahandling import add_to_json
from google import genai
from pydantic import BaseModel, Field

class Book(BaseModel):
    name: str = Field(description="Name of the book")
    genre: str = Field(description="Genres the book belongs to")
    year: int = Field(description="Year of book publication")
    synopsis: str = Field(description="What the book is about")

def ask_llm(book_name, author_name):
    client = genai.Client()

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=f"Provide the synopsis, genre and year of the {book_name} by the author {author_name}",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": Book.model_json_schema()
        }
        
    )
    book = interaction.output_text
    add_to_json(book)