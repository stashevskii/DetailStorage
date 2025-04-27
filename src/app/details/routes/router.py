from fastapi import APIRouter, FastAPI
from src.app.details.config.config import router_config
from .funcs import *

router = APIRouter(prefix=router_config.prefix, tags=router_config.tags)

router.get("/",
           summary=router_config.docs[1]["summary"],
           description=router_config.docs[1]["description"])(get_detail)
router.post("/",
            summary=router_config.docs[2]["summary"],
            description=router_config.docs[2]["description"])(add_detail)
router.delete("/{id}",
              summary=router_config.docs[3]["summary"],
              description=router_config.docs[3]["description"])(delete_detail)
router.put("/{id}",summary=router_config.docs[4]["summary"],
           description=router_config.docs[4]["description"])(full_update_detail)
router.patch("/{id}",
             summary=router_config.docs[5]["summary"],
             description=router_config.docs[5]["description"])(part_update_detail)


def add_detail_router(app: FastAPI):
    app.include_router(router)
