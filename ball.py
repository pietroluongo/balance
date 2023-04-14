class Ball:
    def __init__(self):
        self._radius = 0
        self._center = (0, 0)
        self._angle = 0
        self._velocity = 0

    def update_position(self, x, y):
        self._center = (x, y)

    @property
    def center(self):
        return self._center