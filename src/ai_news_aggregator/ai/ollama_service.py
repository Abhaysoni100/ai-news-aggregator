import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_summary(content: str) -> str:

    # Limit content size
    content = content[:6000]

    prompt = f"""
Summarize the following AI news article.

Rules:
- Write a concise summary.
- Focus on the important information.
- Use simple language.
- Maximum 4 sentences.

Article:

{content}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "Summary could not be generated."
        ).strip()

    except Exception as e:

        print(f"Error generating AI summary: {e}")

        return "Summary could not be generated."