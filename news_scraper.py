
import requests
from bs4 import BeautifulSoup

# News website URL
URL = "https://www.bbc.com/news"

# Send request to website
headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_headlines():
    try:
        response = requests.get(
            URL,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find headline tags
        headline_tags = soup.find_all(["h2", "h3"])

        headlines = []
        seen = set()

        for tag in headline_tags:
            headline = tag.get_text(" ", strip=True)

            if headline and headline not in seen:
                headlines.append(headline)
                seen.add(headline)

        if not headlines:
            print("No headlines found. The website structure may have changed.")
            return

        # Display headlines
        print("\n====== TOP NEWS HEADLINES ======\n")

        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline}")

        # Save headlines to text file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            file.write("TOP NEWS HEADLINES\n")
            file.write("===================\n\n")

            for index, headline in enumerate(headlines, start=1):
                file.write(f"{index}. {headline}\n")

        print("\nHeadlines saved successfully in headlines.txt")

    except requests.exceptions.RequestException as error:
        print("Error fetching website:", error)

    except Exception as error:
        print("An unexpected error occurred:", error)


# Run the scraper
if __name__ == "__main__":
    scrape_headlines()
