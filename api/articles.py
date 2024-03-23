from ninja import Router
from .schemas import ArticleSchema
from content.models import Articles

articles_router = Router()

@articles_router.get("/articles")
def get_articles(request, category: int = None, tag: str = None, skip: int = 0, limit: int = 10):
    queryset = Articles.objects.all()

    if category:
        queryset = queryset.filter(category_id=category)
    
    if tag:
        queryset = queryset.filter(tags__name=tag)

    total = queryset.count()
    articles = queryset[skip:skip + limit]

    return {
        "total": total,
        "articles": [ArticleSchema.from_orm(article) for article in articles]
    }