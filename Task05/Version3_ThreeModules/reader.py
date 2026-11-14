
from pathlib import Path


def read_attendance(input_folder):
    records = []
    damaged_records = []

    files = sorted(Path(input_folder).glob("day*.txt"))

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register, date, status = [
                        part.strip() for part in parts
                    ]

                    if not register or not date:
                        raise ValueError("Missing student details")

                    if status not in ("P", "A"):
                        raise ValueError("Invalid attendance status")

                    records.append((register, date, status))

                except ValueError as error:
                    damaged_records.append(
                        f"{file_path.name}, Line {line_number}: {error}"
                    )

    return records, damaged_records
