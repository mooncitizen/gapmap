from fastapi import FastAPI, HTTPException

from gapmap import (
    get_city_by_name,
    distance_between_cities,
    radius_around_coords,
    is_out_of_radius,
)

app = FastAPI()


@app.get("/city_by_name/{name}")
async def city_by_name(name: str):
    city = get_city_by_name(name, expanded=True)

    if city is None:
        raise HTTPException(status_code=404, detail=f"{name} not found")

    return city


@app.get("/distance_between_two_cities/{city1}/{city2}")
async def distance_between_two_cities(city1: str, city2: str):
    distance = distance_between_cities(city1, city2)
    return distance


@app.get("/radial_around_city/{city}/{range_in_miles}")
async def radial_around_city(city: str, range_in_miles: int):
    city = get_city_by_name(city)

    cities = city.get("cities", None)

    if cities is None:
        c = city
    else:
        if type(cities) == dict:
            c = cities
        else:
            c = cities[0]

    radius = radius_around_coords(c["latitude"], c["longitude"], range_in_miles)

    c["range"] = range_in_miles
    c["radius"] = radius

    return c


@app.get("/radial_from_lat_lng/{lat}/{lng}/{range_in_miles}")
async def radial_from_lat_lng(lat: float, lng: float, range_in_miles: int):
    radius = radius_around_coords(lat, lng, range_in_miles)

    return {"latitude": lat, "longitude": lng, "radius": radius}


@app.get("/is_out_of_radius/{cityA}/{cityB}/{range_in_miles}")
async def is_out_of_radius_by_city(cityA: str, cityB: str, range_in_miles: float):
    cityA = get_city_by_name(cityA)
    cityB = get_city_by_name(cityB)

    citiesA = cityA.get("cities", None)
    citiesB = cityB.get("cities", None)

    if citiesA:
        cityA = cityA["cities"]

    if citiesB:
        cityB = cityB["cities"]

    c = is_out_of_radius(
        cityA,
        cityB,
        range_in_miles,
    )

    return c
