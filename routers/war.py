from fastapi import APIRouter
from fastapi_utils.inferring_router import InferringRouter
from settings import settings

from services.war_service import WarService
from war_store import WarLogStore
from models import ResponseModel

router = InferringRouter()


class WarListApiView:

    @router.get('/wars', status_code=200, response_model=ResponseModel)
    async def get():
        war_date_gte = settings.WAR_START_DATE
        war_date_lte = settings.WAR_END_DATE
        context = {
            'data': WarLogStore().filter_by_date(
                war_date_gte,
                war_date_lte
            )
        }
        return context