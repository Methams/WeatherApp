import requests
def Magic(city):
    Coord = CityToCoord(city)
    Lat, Lon = Coord
    Temp = CoordToTemp(Lat, Lon)
    print("Done!")
    return Temp


def CityToCoord(City):
    Url = f"https://geocoding-api.open-meteo.com/v1/search?name={City}&count=10&language=en&format=json"
    Feedback = requests.get(Url).json()

    if "results" in Feedback:
        Result = Feedback["results"][0] # Get the first result
        return Result["latitude"], Result["longitude"]
    return None, None

def CoordToTemp(Lat, Lon):
    if Lat is None:
        return 1
    
    Url = f"https://api.open-meteo.com/v1/forecast?latitude={Lat}&longitude={Lon}&current=temperature_2m"
    Feedback = requests.get(Url).json()

    Temperature = Feedback["current"]["temperature_2m"]
    return f"{Temperature}°C"
    