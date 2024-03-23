from ninja import Schema

class ArticleSchema(Schema):
    id: int
    title: str
    description: str
    # Define other fields as needed

class BlockSchema(Schema):
    visual: str
    block_position: str
    row: int