from fastapi import APIRouter
from fastapi.responses import JSONResponse


# make router with file name
user_router = APIRouter()


@user_router.post("/user_data_test")
async def vendorScores():

    data = {
        'name': 'test',
        'email': 'test@gmail.com',
        'contact': '123455567'
    }

    return JSONResponse(content={"success": True, "message": "User fetched Successful", "status": 200, "data": data})
