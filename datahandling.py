import json

def add_to_json(book):
    new_book_dict = json.loads(book)

    try:
        
        with open("history.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    history.append(new_book_dict)

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

    print("Book successfully added!")