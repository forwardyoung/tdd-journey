import redis
import pytest
from fastapi.testclient import TestClient
from main import app

# Redis 클라이언트 임의 설정
r = redis.Redis(host='localhost', port=6379, db=2)

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # 테스트 실행 전에 Redis에 데이터 설정
    r.flushdb()  # 테스트용 Redis 데이터베이스 초기화
    r.set("user_location:1", "40.7128,-74.0060")

    yield

    # 테스트 종료 후 Redis 데이터베이스 초기화
    r.flushdb()


def test_get_location():
    response = client.get("/get-location/1")
    assert response.status_code == 200
    assert response.json() == {
        "user_id": "1",
        "latitude": 40.7128,
        "logitude": -74.0060
    }