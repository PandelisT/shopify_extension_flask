from main import db


customers_tags = db.Table("customers_tags", db.Model.metadata,
                          db.Column("customer_id", db.Integer,
                                    db.ForeignKey("customers.id")),
                          db.Column("tag_id", db.Integer,
                                    db.ForeignKey("tags.id")))
