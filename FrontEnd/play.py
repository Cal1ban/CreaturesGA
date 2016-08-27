from websocket import create_connection

while True:
    ws = create_connection("ws://localhost:5000")
    ws.send("hello world")
    result = ws.recv()
    print(result)
    ws.close()