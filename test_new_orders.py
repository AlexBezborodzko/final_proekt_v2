# Алексей Безбородько, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import stand_request


# Проверка ответа 200
def positive_200(track):
    response = stand_request.get_order_by_number(track)
    assert response.status_code == 200


# Запрос на созданный номер заказа
def test_successful_response():
    positive_200(stand_request.track)
