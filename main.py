from fastapi import FastAPI
import requests
from datetime import datetime

endpoint = 'https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus'

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/orders/")
async def get_order_by_id(order_data: dict):
    order_id = order_data['queryResult']['parameters']['orderID']
    # print(order_id)
    data = {
        'orderId': f'{order_id}'
    }
    r = requests.post(url=endpoint, data=data)
    date = r.json()['shipmentDate']
    iso_date = datetime.fromisoformat(date)
    ret_date = iso_date.strftime('%A, %d %b %Y')
    print(ret_date)
    return {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        f'Your order {order_id} will be shipped on {ret_date}'
                    ]
                }
            }
        ]
    }
