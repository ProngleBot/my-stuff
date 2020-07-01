import requests

imagelink = input("paste link: ")

url = "https://google-reverse-image-search.p.rapidapi.com/imgSearch"
querystring = {"url":imagelink}

headers = {
    'x-rapidapi-host': "google-reverse-image-search.p.rapidapi.com",
    'x-rapidapi-key': "3ab0d95ae7msh987302756243bcfp1544e1jsne709d54e402f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)