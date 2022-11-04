#How to Make GET Requests to Web APIs using Python as a Client
import requests #library to make http requests
import json #libraryy is used to working with Jsoon  objects
movie = input("Enter your moviename: ")

url='https://itunes.apple.com/search?term='+movie+'&media=movie'

response=requests.get(url);

#check the response of status code
print("statuscode: ",response.status_code)

if response.status_code==200:
  #succes grab the JSON object from body
  #print("ok")
  json_object=json.loads(response.text)
  #print(json_object)

  result_array=json_object['results']
  for result in result_array:
    name=result['trackName']
    releaseDate=result['releaseDate']
    print(name,releaseDate)
