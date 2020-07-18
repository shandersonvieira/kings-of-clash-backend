from fastapi import APIRouter
from fastapi_utils.inferring_router import InferringRouter

from services.war_service import WarService
from war_store import WarLogStore
from models import ResponseModel

router = InferringRouter()


class WarListApiView:

    @router.get('/wars', status_code=200, response_model=ResponseModel)
    async def get():
        context = {
            'data': WarLogStore().get()
        }

        return context