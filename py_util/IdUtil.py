
from datetime import datetime

import time

def __current_milli_seconds():
    return round(time.time() * 1000)

def basicUqIdF():
    return __current_milli_seconds()
