import redis
from fastapi import FastAPI, HTTPException

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)
r.set("user_location:1", "40.7128,-74.0060")


@app.get("/get-location/{user_id}")
def get_location(user_id: str):
    location_data = r.get(f"user_location:{user_id}")

    if location_data:
        latitude, longitude = map(float, location_data.decode('utf-8').split(','))
        return {
            "user_id": "1",
            "latitude": 40.7128,
            "logitude": -74.0060
        }
    else:
        raise HTTPException(status_code=404, detail="Location data not found")
