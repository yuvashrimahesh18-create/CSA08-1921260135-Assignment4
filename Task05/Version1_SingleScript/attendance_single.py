
from pathlib import Path


# Locate the shared input files
BASE_FOLDER = Path(__file__).parent
INPUT_FOLDER = BASE_FOLDER.parent / "input_files"


def read_attendance():
    attendance = {}
    damaged_records = []

    files = sorted(INPUT_FOLDER.glob("day*.txt"))

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register = parts[0].strip()
                    date = parts[1].strip()
                    status = parts[2].strip()

                    if not register or not date:
                        raise ValueError("Missing student details")

                    if status not in ("P", "A"):
                        raise ValueError("Invalid attendance status")

                    if register not in attendance:
                        attendance[register] = {
                            "present": 0,
                            "absent": 0
                        }

                    if status == "P":
                        attendance[register]["present"] += 1
                    else:
                        attendance[register]["absent"] += 1

                except ValueError as error:
                    damaged_records.append(
                        f"{file_path.name}, Line {line_number}: {error}"
                    )

    return attendance, damaged_records


def find_three_day_absentees():
    files = sorted(INPUT_FOLDER.glob("day*.txt"))
    absent_sets = []

    for file_path in files:
        absent_students = set()

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) == 3 and parts[2].strip() == "A":
                    absent_students.add(parts[0].strip())

        absent_sets.append(absent_students)

    consecutive_absentees = set()

    for i in range(len(absent_sets) - 2):
        common = (
            absent_sets[i]
            & absent_sets[i + 1]
            & absent_sets[i + 2]
        )
        consecutive_absentees.update(common)

    return sorted(consecutive_absentees)


def write_reports(attendance, damaged_records):
    report_path = BASE_FOLDER / "attendance_report.txt"
    absence_path = BASE_FOLDER / "three_day_absentees.txt"
    error_path = BASE_FOLDER / "damaged_records.txt"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("ATTENDANCE REPORT\n")
        report.write("=" * 40 + "\n")

        for register, counts in sorted(attendance.items()):
            total = counts["present"] + counts["absent"]
            percentage = (
                counts["present"] / total * 100 if total else 0
            )

            report.write(
                f"{register} | Present: {counts['present']} | "
                f"Absent: {counts['absent']} | "
                f"Percentage: {percentage:.2f}%\n"
            )

    absentees = find_three_day_absentees()

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


if __name__ == "__main__":
    attendance, damaged_records = read_attendance()
    write_reports(attendance, damaged_records)
