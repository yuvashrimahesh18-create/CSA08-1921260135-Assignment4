
from pathlib import Path


def write_reports(attendance, absentees, damaged_records, output_folder):
    output_folder = Path(output_folder)

    report_path = output_folder / "attendance_report.txt"
    absence_path = output_folder / "three_day_absentees.txt"
    error_path = output_folder / "damaged_records.txt"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("ATTENDANCE REPORT\n")
        report.write("=" * 40 + "\n")

        for register, counts in sorted(attendance.items()):
            total = counts["present"] + counts["absent"]
            percentage = counts["present"] / total * 100 if total else 0

            report.write(
                f"{register} | Present: {counts['present']} | "
                f"Absent: {counts['absent']} | "
                f"Percentage: {percentage:.2f}%\n"
            )

    with open(absence_path, "w", encoding="utf-8") as report:
        report.write("STUDENTS ABSENT FOR THREE CONSECUTIVE DAYS\n")
        for register in absentees:
            report.write(register + "\n")

    with open(error_path, "w", encoding="utf-8") as error_file:
        error_file.write("DAMAGED RECORDS\n")
        for record in damaged_records:
            error_file.write(record + "\n")

    print("Reports generated successfully!")
    print("Attendance report:", report_path)
    print("Three-day absence report:", absence_path)
    print("Damaged records:", error_path)
