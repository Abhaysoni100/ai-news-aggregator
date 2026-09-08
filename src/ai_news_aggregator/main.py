from ai_news_aggregator.services.rss_service import fetch_all_news
from ai_news_aggregator.database.connection import Base, engine, SessionLocal
from ai_news_aggregator.models.article import Article
from ai_news_aggregator.ai.ollama_service import generate_summary


def main():
    print("Starting AI News Aggregator...")

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Fetch articles
    articles = fetch_all_news()

    print("\nSaving articles to database...\n")

    db = SessionLocal()

    saved_count = 0
    skipped_count = 0

    try:
        for article_data in articles:

            # Check if article already exists
            existing_article = (
                db.query(Article)
                .filter(Article.url == article_data["url"])
                .first()
            )

            if existing_article:
                print(f"\nSkipping duplicate:")
                print(article_data["title"])

                skipped_count += 1
                continue

            print("\nGenerating AI summary for:")
            print(article_data["title"])

            # Get article content safely
            content = article_data.get("content", "")

            # Generate summary only if content exists
            if content:
                summary = generate_summary(content)
            else:
                summary = "Summary could not be generated."

            # Create article
            article = Article(
                title=article_data["title"],
                url=article_data["url"],
                source=article_data["source"],
                content=content,
                summary=summary,
            )

            db.add(article)

            # Commit each article
            db.commit()

            saved_count += 1

            print("✓ Article saved successfully")

    except Exception as e:
        db.rollback()

        print(f"\nError saving articles: {e}")

    finally:
        db.close()

    print("\n-----------------------------")
    print(f"New articles saved: {saved_count}")
    print(f"Duplicate articles skipped: {skipped_count}")
    print("-----------------------------")

    print("\nAI News Aggregator finished successfully!")


if __name__ == "__main__":
    main()