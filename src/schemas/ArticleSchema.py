from main import ma
from models.Article import Article

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
    
    product_articles = ma.Nested("ProductSchema", many=True)


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)