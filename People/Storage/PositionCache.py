import redis
from People.Interface.move_pb2 import Movement, Direction, LEFT, RIGHT, UP, DOWN
from People.Interface.move_pb2 import UpdatedPosition

class PositionCache:

    def __init__(self, 
                 conn = redis.StrictRedis(host = 'localhost', port=6379)):
                 
        self.conn = conn

    def get_pos(self, p_id: int):
        x_key, y_key = "pos:{0}:x".format(p_id), "pos:{0}:y".format(p_id)
        x, y = self.conn.get(x_key), self.conn.get(y_key)
        if x is None:
            x = 0
        if y is None:
            y = 0
        return int(x), int(y)

    def set_pos(self, p_id, x, y):
        x_key, y_key = "pos:{0}:x".format(p_id), "pos:{0}:y".format(p_id)
        self.conn.set(x_key, x)
        self.conn.set(y_key, y)

    def update_position(self, move: Movement) -> UpdatedPosition:
        x, y = self.get_pos(move.p_id)
        print("In cache {0}".format(str(x)))
        print(move.direction)
        if move.direction == RIGHT:
            x += 1
            print("r")
        elif move.direction == LEFT:
            x -= 1
        elif move.direction == UP:
            y += 1
        else:
            y -= 1

        self.set_pos(move.p_id, x, y)

        update = UpdatedPosition()
        update.p_id = move.p_id
        update.x_pos = x
        update.y_pos = y
        print(x, y)
        print(update)
        return update