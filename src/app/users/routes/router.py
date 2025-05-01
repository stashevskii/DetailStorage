from fastapi import APIRouter, FastAPI
from src.app.users.config.config import router_config
from .funcs import *

router = APIRouter(prefix=router_config.prefix, tags=router_config.tags)

router.get("/",
           summary=router_config.docs[1]["summary"],
           description=router_config.docs[1]["description"])(get_user)
router.post("/",
            summary=router_config.docs[2]["summary"],
            description=router_config.docs[2]["description"])(add_user)
router.delete("/{id}",
              summary=router_config.docs[3]["summary"],
              description=router_config.docs[3]["description"])(delete_user)
router.put("/{id}",summary=router_config.docs[4]["summary"],
           description=router_config.docs[4]["description"])(full_update_user)
router.patch("/{id}",
             summary=router_config.docs[5]["summary"],
             description=router_config.docs[5]["description"])(part_update_user)


def add_user_router(app: FastAPI):
    app.include_router(router)
