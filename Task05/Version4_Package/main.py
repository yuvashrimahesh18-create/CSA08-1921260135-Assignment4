
from pathlib import Path

from attendance.reader import read_attendance
from attendance.stats import calculate_statistics, find_three_day_absentees
from attendance.report import write_reports


if __name__ == "__main__":
    base_folder = Path(__file__).parent
    input_folder = base_folder.parent / "input_files"

    records, damaged_records = read_attendance(input_folder)

    attendance = calculate_statistics(records)

    absentees = find_three_day_absentees(records)

    write_reports(
        attendance,
        absentees,
        damaged_records,
        base_folder
    )
