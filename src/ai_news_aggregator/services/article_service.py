from sqlalchemy.orm import Session

from ai_news_aggregator.models.article import Article


def save_article(db: Session, article_data: dict):
    existing_article = (
        db.query(Article)
        .filter(Article.url == article_data["url"])
        .first()
    )

    if existing_article:
        print(f"Skipping duplicate: {article_data['title']}")
        return existing_article

    article = Article(
        title=article_data["title"],
        url=article_data["url"],
        source=article_data["source"],
        summary=article_data.get("summary"),
    )

    db.add(article)
    db.commit()
    db.refresh(article)

    print(f"Saved: {article.title}")

    return article