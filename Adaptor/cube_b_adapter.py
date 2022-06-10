"an interface for cubeB so it can be used like CubeA"
from interface_cube_a import ICubeA
from cube_b import CubeB


class CubeBAdapter(ICubeA):
    "adapter for CubeB that implements ICubeA"
    def __init__(self):
        self.cube = CubeB
        self.width = self.height = self.depth = 0

    def manufacture(self: 'CubeBAdapter' = None, width: int = 0, height: int = 0, depth: int = 0) -> bool:
        self.width = width
        self.height = height
        self.depth = depth

        success = self.cube.create(
            self,
            top_left_front=(0-width/2, 0-height/2, 0-depth/2),
            bottom_right_back=(0+width/2, 0+height/2, 0+depth/2)
        )
        return success
