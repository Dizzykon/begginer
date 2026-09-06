# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: FleetCare
def test_edge_cases():
    assert is_valid_date("2024-13-01") == False
    assert is_valid_date("2024-00-01") == False
    assert is_valid_date("0000-01-01") == False
    assert is_valid_date("2024-02-30") == False
    assert is_valid_date("2024-04-31") == False
    assert is_valid_date("2024-06-30") == True
    assert is_valid_date("2024-01-31") == True
    assert is_valid_date("2024-02-29") == False
    assert is_valid_date("2024-02-28") == True
    assert is_valid_date("2024-02-29") == True
    assert is_valid_date("2024-02-29") == True
    assert is_valid_date("2024-02-29") == True
    assert is_valid_date("2024-02-29") == True
