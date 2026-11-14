
from pathlib import Path

def process_attendance(folder):
    attendance = {}
    damaged_records = []

    # Find all daily attendance files
    files = sorted(Path(folder).glob("day*.txt"))

    # Read each file one line at a time
    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    try:
                        parts = line.strip().split(",")

                        if len(parts) != 3:
                            raise ValueError("Expected 3 fields")

                        register_number = parts[0].strip()
                        date = parts[1].strip()
                        status = parts[2].strip()

                        if not register_number or not date:
                            raise ValueError("Missing student details")

                        if status not in ("P", "A"):
                            raise ValueError(f"Invalid status '{status}'")

                        if register_number not in attendance:
                            attendance[register_number] = {
                                "present": 0,
                                "absent": 0
                            }

                        if status == "P":
                            attendance[register_number]["present"] += 1
                        else:
                            attendance[register_number]["absent"] += 1

                    except ValueError as error:
                        damaged_records.append(
                            f"{file_path.name}, Line {line_number}: "
                            f"{line.strip()} - {error}"
                        )

        except FileNotFoundError:
            damaged_records.append(f"{file_path.name}: File not found")
        except PermissionError:
            damaged_records.append(f"{file_path.name}: Permission denied")
        except UnicodeDecodeError:
            damaged_records.append(f"{file_path.name}: Encoding error")

    # Generate monthly attendance report
    report_path = Path(folder) / "monthly_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("MONTHLY ATTENDANCE REPORT\n")
        report.write("=" * 50 + "\n")

        for register_number, counts in sorted(attendance.items()):
            present = counts["present"]
            absent = counts["absent"]
            total = present + absent
            percentage = (present / total) * 100 if total else 0

            report.write(
                f"{register_number} | Present: {present} | "
                f"Absent: {absent} | Attendance: {percentage:.2f}%\n"
            )

            if percentage < 75:
                report.write("WARNING: Attendance below 75%\n")

    # Generate damaged-record log
    error_path = Path(folder) / "damaged_records.txt"

    with open(error_path, "w", encoding="utf-8") as error_file:
        error_file.write("DAMAGED ATTENDANCE RECORDS\n")
        error_file.write("=" * 50 + "\n")

        if damaged_records:
            for record in damaged_records:
                error_file.write(record + "\n")
        else:
            error_file.write("No damaged records found.\n")

    print("Attendance processing completed!")
    print("Monthly report saved:", report_path)
    print("Damaged record log saved:", error_path)


if __name__ == "__main__":
    folder_path = Path(__file__).parent
    process_attendance(folder_path)
