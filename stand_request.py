import config
import requests
import data

# Создаем заказ
def create_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDERS,
                         json=body,
                         headers=data.headers
                         )
response = create_new_order(data.order_body)
# Сохраняем номер заказа

track = response.json()["track"]



# Получить заказ по номеру
def get_order_by_number(track):
    return requests.get(config.URL_SERVICE + config.GET_ORDERS,
                        params={'t': track})
response = get_order_by_number(track)
