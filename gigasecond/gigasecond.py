def add(moment):
    from datetime import datetime, timedelta
    res = moment + timedelta(seconds=1000000000)
    return res