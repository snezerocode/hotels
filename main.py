from fastapi import FastAPI, Body
import uvicorn
from fastapi.params import Query

app = FastAPI()

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Dubai", "name": "dubai"},
]

@app.put("/hotels/{hotel_id}")
def edit_hotel(
        id: int ,
        title: str = Body(),
        name: str = Body(),
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == id:
            hotel["title"] = title
            hotel["name"] = name

    return {"status": "ok"}

@app.patch("/hotels/{id}")
def edit_hotel_attr(
        id: int,
        title: str = Body(None),
        name: str = Body(None),
):
    global hotels
    for hotel in hotels:
       if hotel["id"] == id:
        if title:
            hotel["title"] = title
        if name:
            hotel["name"] = name
        return {"status": "ok"}
    return {"status": "not found"}


@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "ok"}


@app.post("/hotels")
def add_hotel(
        title: str = Body(embed=True),
):
    global hotels
    hotels.append(
        {
            "id": hotels[-1]["id"] + 1,
            "title": title,
        }
    )
    return {"status": "ok"}




@app.get("/hotels")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None= Query(None, description="Название отеля"),

):
    hotels_ = []
    for hotel in hotels:
        if hotel["id"] and id != id:
            continue
        if hotel["title"] and title != title:
            continue
        hotels_.append(hotel)
    return hotels_


@app.get("/")
def func():
    return "Hello world"




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)