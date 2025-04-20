from fastapi import HTTPException

not_found_detail_exception = HTTPException(status_code=422, detail="Detail not found")
