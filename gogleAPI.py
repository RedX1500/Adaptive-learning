import requests
search={
    'q':'linked list',
    'key':'AIzaSyCcFFRRX1tG4T0m4D3ch9-RKDzi0YS0Ecw',
    'cx':'c53e63989d3584fc4',
    'searchType': 'video'
}
response = requests.get('https://www.googleapis.com/customsearch/v1',params=search)
back = response.json()
for i in range(0,10):
  print(back['items'][i]['link'])