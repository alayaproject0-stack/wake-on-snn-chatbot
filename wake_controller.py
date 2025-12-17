class WakeController:
    def __init__(self, thr):
        self.thr = thr

    def should_wake(self, confidence):
        return confidence < self.thr
