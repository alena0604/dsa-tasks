# You are given two arrays of strings that represent two inclusive events that happened on the same day,
# event1 and event2, where:
#
# event1 = [startTime1, endTime1] and
# event2 = [startTime2, endTime2].
# Event times are valid 24 hours format in the form of HH:MM.
#
# A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
#
# Return true if there is a conflict between two events. Otherwise, return false.


from typing import List


def time_to_min(time_event: str) -> int:
    hours, minutes = map(int, time_event.split(":"))
    return hours * 60 + minutes


def have_conflict(event1: List[str], event2: List[str]) -> bool:
    start1, end1 = map(time_to_min, event1)
    start2, end2 = map(time_to_min, event2)

    return not (end1 < start2 or end2 < start1)


print(have_conflict(["01:15", "02:00"], ["02:00", "03:00"]))
