
from datetime import datetime, timedelta


def calculate_statistics(records):
    attendance = {}

    for register, date, status in records:
        if register not in attendance:
            attendance[register] = {
                "present": 0,
                "absent": 0
            }

        if status == "P":
            attendance[register]["present"] += 1
        else:
            attendance[register]["absent"] += 1

    return attendance


def find_three_day_absentees(records):
    absent_dates = {}

    for register, date, status in records:
        if status == "A":
            if register not in absent_dates:
                absent_dates[register] = set()

            absent_dates[register].add(
                datetime.strptime(date, "%Y-%m-%d").date()
            )

    consecutive_absentees = []

    for register, dates in absent_dates.items():
        for date in dates:
            if (
                date + timedelta(days=1) in dates
                and date + timedelta(days=2) in dates
            ):
                consecutive_absentees.append(register)
                break

    return sorted(consecutive_absentees)
