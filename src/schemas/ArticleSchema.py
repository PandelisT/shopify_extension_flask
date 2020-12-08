from main import ma
from models.Article import Article

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
    
    # customer = ma.Nested("CustomerSchema", many=True)


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)