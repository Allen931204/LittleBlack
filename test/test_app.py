import sys
import os
# 添加 devops-test 目錄到 sys.path，這樣可以讓 Python 正確找到 app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello():
    assert 1 == 1

def test_home_page(client):
    """測試首頁是否成功回傳 200 且包含預期中文字"""
    response = client.get('/')
    assert response.status_code == 200

    # 解碼 HTML 並進行中文內容驗證
    html = response.data.decode('utf-8')
    assert "歡迎來到 測試 DevOps" in html
    assert "Gitea" in html
    assert "Jenkins" in html
    assert "Docker" in html
