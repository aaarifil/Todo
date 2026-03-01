from fastapi.testclient import TestClient
import traceback

import main

client = TestClient(main.app)

def run():
    try:
        resp = client.post('/api/v1/todos', json={'title':'Debug test','description':'from debug'})
        print('STATUS', resp.status_code)
        print(resp.text)
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    run()
