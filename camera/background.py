from colorDetectionData import ColorDetectionData

class Background:
    def __init__(self):
        self._color_data = ColorDetectionData()

    @property
    def pos(self):
        return self._color_data.bounding_box

    @property
    def color(self):
        return self._color_data.rgb__picked_color

    @color.setter
    def color(self, rgb__color):
        self._color_data.handle_color_pick(rgb__color)

    @property
    def color_bounds(self):
        return (self._color_data.rgb__upper_color, self._color_data.rgb__lower_color, self._color_data.rgb__picked_color)

    @property
    def mask(self):
        return self._color_data._hsv__color_mask

    def tick(self):
        self._color_data.update_mask()
        self._color_data.get_center_and_update_bbox()

