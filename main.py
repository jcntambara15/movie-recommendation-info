import requests

url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

querystring = {"term":"bojack","country":"uk"}

headers = {
	"X-RapidAPI-Key": "810b9b6234msh366e8e207f34b19p1d8783jsn241cbe87fe8e",
	"X-RapidAPI-Host": "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)