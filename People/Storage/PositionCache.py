import redis
from People.Interface.move import MovementRequest
from People.Interface.move import UpdatedPosition


class PositionCache:
    def __init__(self,
                 conn=redis.StrictRedis(host='localhost', port=6379)):

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

    def update_position(self, move: MovementRequest) -> UpdatedPosition:
        self.set_pos(move.p_id, move.destination.x_pos, move.destination.y_pos)

        update = UpdatedPosition()
        update.p_id = move.p_id
        update.x_pos = move.destination.x_pos
        update.y_pos = move.destination.y_pos
        print(update)
        return update
