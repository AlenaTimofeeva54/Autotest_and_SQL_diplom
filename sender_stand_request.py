import configuration
import data
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)
response = post_new_order(data.body_order)
print(response.status_code)
print(response.json())

def get_new_order_track():
    order_response = post_new_order(data.body_order)
    track = order_response.json()["track"]
    return str(track)

track = get_new_order_track()
print(track)

def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_NUMBER + track)

response = get_order_by_track()
print(response.status_code)
print(response.json())



