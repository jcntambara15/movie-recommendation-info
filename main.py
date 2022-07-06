import requests
import pandas as pd
import sqlalchemy as db	
import json

session_id= 'c72032122d67260cc02034445c4206ba96a84f0e'
list_id = '8209394'

session_id= 'c72032122d67260cc02034445c4206ba96a84f0e'
list_id = '8209391'

# request token used in retriving sesion id 
mykey ={'request_token': '00b55b48576f0ad50239e00e35a9acd0c7091d2f'}
# api_key
api_key ='dd1c306527d8caa33b2acb40c88ce2ae'

#parts for the creating a list
list_body = {'name': 'Movie recommendation', 'description': 'List of movies to be recommended', 'language': 'en'}
header = {'Content-Type': 'application/json;charset=utf-8'}
query_string ={'session_id': 'c72032122d67260cc02034445c4206ba96a84f0e'}

#prints the list id used to add recommended movies
listUrl = 'https://api.themoviedb.org/3/list?api_key=dd1c306527d8caa33b2acb40c88ce2ae'
responseL = requests.post(listUrl, headers=header, json=list_body, params=query_string)
print(responseL.json())