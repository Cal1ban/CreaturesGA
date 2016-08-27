#!/usr/bin/python
import websocket
import time

def on_message(ws, message):
    print (message.decode("utf-8"))

def on_error(ws, error):
    print("here")
    print(error.decode("utf-8"))

def on_close(ws):
    print("Closed")

def on_open(ws):
    for i in range(30000):
        time.sleep(1)
        ws.send("Hello %d" % i)
    time.sleep(1)
    ws.close()
    print("thread terminating...")
    print("open")


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:5000",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()