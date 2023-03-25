from sqlalchemy import Column, Integer, String, DateTime

from . import Base


class Sitemap(Base):
    __tablename__ = "sitemaps"

    id = Column(Integer, primary_key=True)
    site = Column(String(255), nullable=False)
    loc = Column(String(2550), nullable=False)
    lastmod = Column(DateTime, nullable=False)
