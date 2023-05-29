from colorDetectionData import ColorDetectionData

class Ball:
    def __init__(self):
        self._radius = 0
        self._center = (0, 0)
        self._color_data = ColorDetectionData()
        self._angle = 0
        self._velocity = 0

    @property
    def center(self):
        return self._center

    @property
    def mask(self):
        return self._color_data.color_mask

    @property
    def color_bounds(self):
        return (self._color_data.rgb__upper_color, self._color_data.rgb__lower_color, self._color_data.rgb__picked_color)

    @property
    def color(self):
        return self._color_data.rgb__picked_color

    @color.setter
    def color(self, rgb__color):
        self._color_data.handle_color_pick(rgb__color)

    def tick(self):
        self._color_data.update_mask()
        self._center = self._color_data.get_center_and_update_bbox()

    def to_json(self):
        return {
            "x": self._center[0],
            "y": self._center[1],
        }
