import time

class Timer:
    def __init__(self):
        self.prev_time = int(round(time.time() * 1000))

    def get_millis(self):
	    return int(round(time.time() * 1000))

    def time_check(self, dif):
        if (self.get_millis() - self.prev_time) > dif:
            self.prev_time = self.get_millis()
            return True
        return False