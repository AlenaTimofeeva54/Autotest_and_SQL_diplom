# Алена Тимофеева, 6-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def positiv_assert():
    order_response = sender_stand_request.get_order_by_track()
    assert order_response.status_code == 200


def test_status_code_order_by_track():
    positiv_assert()
