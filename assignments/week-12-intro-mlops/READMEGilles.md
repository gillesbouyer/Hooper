# stock-predictor
special repo to do week12 of 4B:
https://github.com/gillesbouyer/stock-predictor
url of fast api
http://3.94.125.15:8000/docs#/default/get_prediction_predict_post

Command:

curl --header "Content-Type: application/json" --request POST --data '{"ticker":"MSFT", "days":7}' http://3.94.125.15:8000/predict

returned 
{"ticker":"MSFT","days":7,"forecast":{"03/06/2023":244.83054811717994,"03/07/2023":244.8113671133644,"03/08/2023":244.79218610954882,"03/09/2023":244.7730051057333,"03/10/2023":244.7538241019177,"03/11/2023":244.7346430981021,"03/12/2023":244.71546209428655}}%                

see semaine 12 for all details

curl -X 'POST' 'http://3.94.125.15:8000/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"ticker": "MSFT","days": 8}'
also works