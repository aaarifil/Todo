from fastapi.testclient import TestClient
import traceback

import main

client = TestClient(main.app)

def run():
    try:
        resp = client.get('/api/v1/todos')
        print('STATUS', resp.status_code)
        print(resp.text)
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    run()
