class Common:
    def __init__(self, bounds, curr_window, img_name):
        self.x_min, self.y_min, self.x_max, self.y_max = bounds
        self.curr_window = curr_window
        self.size = (int(self.x_max - self.x_min), int(self.y_max - self.y_min))
        self.image_name = img_name
