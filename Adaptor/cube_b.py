import time
from interface_cube_b import ICubeB


class CubeB(ICubeB):
    "A hypothetical Cube tool from Company B"
    # a static variable indicating the last time a cube was manufactured
    last_time = int(time.time())

    def create(self: 'CubeB' = None, top_left_front: tuple = 0, bottom_right_back: tuple = 0) -> bool:
        now = int(time.time())
        if now > int(CubeB.last_time + 2):
            CubeB.last_time = now
            return True
        else:
            return False  # busy

