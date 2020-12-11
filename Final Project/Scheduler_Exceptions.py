class Error(Exception):
    """Base"""
    pass

class day_range(Exception):
    """created when day range is outside normal month range"""
    pass
class time_range(Exception):
    """created when time range is invalid"""
    pass