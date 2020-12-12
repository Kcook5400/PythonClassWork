"""
PEP: 8
Title: Scheduler exceptions
Author: Kevin Cook
Status: Active
Type: Process
Created: 12-12-2020
Post:12-12-2020
History:
"""

class Error(Exception):
    """Base"""
    pass

class day_range(Exception):
    """created when day range is outside normal month range"""
    pass
class time_range(Exception):
    """created when time range is invalid"""
    pass