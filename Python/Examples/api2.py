import requests


def search_books(query):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query}
    headers = {
        'Authorization': 'Bearer <token>',
        'Content-Type': 'application/json'  # Depending on the API requirements
    }

    try:
        response = requests.get(base_url, params=params) #headers=headers)
        data = response.json()

        if "items" in data:
            for item in data["items"]:
                volume_info = item["volumeInfo"]
                title = volume_info["title"]
                authors = volume_info.get("authors", ["Unknown"])
                publisher = volume_info.get("publisher", "Unknown")
                published_date = volume_info.get("publishedDate", "Unknown")
                print(f"Title: {title}")
                print(f"Authors: {', '.join(authors)}")
                print(f"Publisher: {publisher}")
                print(f"Published Date: {published_date}")
                print("-------------------------")
        else:
            print("No books found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
search_books("Python programming")
