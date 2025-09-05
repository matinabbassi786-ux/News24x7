
import requests
import pandas

api_url = "http://127.0.0.1:8000/api/User%20Info/"  # Example API endpoint

rowf = pandas.read_csv('E:/projects/news24x7/API/MOCK_DATA.csv')

for x in range(22,976):
    email = rowf["email"]
    q = email.loc[x]
    data1 ={
  "email": [
    q
  ]
}
    adqa = requests.post(api_url,data=data1)
    # print(adqa.json)





