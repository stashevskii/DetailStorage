from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.db.db import get_db

DbDep = Annotated[Session, Depends(get_db)]
