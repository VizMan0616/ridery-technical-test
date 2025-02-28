import logging
from typing import List

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.models.vehicle import Vehicle

_logger = logging.getLogger("uvicorn")
app = FastAPI()


@app.post("/vehicles", status_code=201)
async def submit_and_print_vehicles(vehicles: List[Vehicle]) -> JSONResponse:
    data = {"message": "Vehicles registered sucessfully"}

    for vehicle in vehicles:
        if len(vehicle.plate_code) != 7:
            data["message"] = "Plate Code must be 7 characters long"
            return JSONResponse(content=data, status_code=400)

        _logger.info(vehicle.print_data())
    return JSONResponse(content=data, status_code=201)
