from ninja import Router
from .schemas import BlockSchema
from modules.models import Block

blocks_router = Router()

@blocks_router.get("/blocks")
def get_blocks(request):
    blocks = Block.objects.all()
    return {"blocks": [BlockSchema.from_orm(block) for block in blocks]}