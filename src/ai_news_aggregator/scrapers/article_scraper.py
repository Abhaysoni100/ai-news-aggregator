import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def scrape_article_content(url: str) -> str | None:
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/120 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Remove unnecessary elements
        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "aside"
        ]):
            tag.decompose()

        # Try to find article content
        article = soup.find("article")

        if article:
            content = md(str(article))
        else:
            content = md(str(soup.body))

        return content.strip()

    except Exception as e:
        print(f"Error scraping article: {url}")
        print(e)

        return None