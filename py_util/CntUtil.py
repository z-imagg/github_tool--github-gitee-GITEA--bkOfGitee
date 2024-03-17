class Counter:
    def __init__(self) -> None:
        self._idx=0
    def inc(self)->int:
        self._idx+=1
        return self._idx