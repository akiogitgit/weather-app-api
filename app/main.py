from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
import json
from starlette.middleware.cors import CORSMiddleware

# ------------------------------------------------------------------
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
	rvalue = {"morning": "おはよう","afternoon": "こんにちは"}
	return rvalue


@app.get("/weather")
async def weather():
	current = Path()
	file_path = current /  "weather.json"
	
	response = FileResponse(path=file_path) 
	 
	return response

@app.get("/weather/city_names")
async def city_names():

# json read
	current = Path()
	file_path = current /  "weather.json"
	with open(file_path, "r") as file:
		dict = json.load(file)

		result = []

		for r in range(0, 8):
			result.append(dict["data"][r]["name"])

		return result


@app.get("/weather/{city_name}")
async def weather(city_name: str):

# json read
	current = Path()
	file_path = current /  "weather.json"
	with open(file_path, "r") as file:
		dict = json.load(file)


	response = dict["data"][0]
	
	for r in range(0, 8):
	    if dict["data"][r]["name"].lower() == city_name.lower():
		    return dict["data"][r]
		


