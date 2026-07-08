from math import floor

class StrikeSelector:
    def __init__(self,itm_distance:int=500):
        self.itm_distance=itm_distance

    def get_strike(self,spot_close:float)->int:
        return floor(spot_close/500)*500-self.itm_distance
