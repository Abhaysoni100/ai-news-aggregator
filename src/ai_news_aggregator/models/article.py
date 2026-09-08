from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from ai_news_aggregator.database.connection import Base


class Article(Base):

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(500), nullable=False)

    url = Column(String(1000), unique=True, nullable=False)

    source = Column(String(200), nullable=False)

    summary = Column(Text, nullable=True)

    content = Column(Text, nullable=True)

    published_at = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    def __repr__(self):
        return f"<Article(title='{self.title}', source='{self.source}')>"