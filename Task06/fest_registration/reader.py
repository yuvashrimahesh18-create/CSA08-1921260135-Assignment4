
from pathlib import Path


def read_department_files(input_folder):
    input_folder = Path(input_folder)

    registrations = []
    error_records = []

    for number in range(1, 6):
        file_path = input_folder / f"department{number}.txt"

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split(",", 4)

                    if len(parts) != 5:
                        error_records.append(
                            f"{file_path.name}, Line {line_number}: "
                            "Damaged record - expected 5 fields"
                        )
                        continue

                    registration = {
                        "register_number": parts[0].strip(),
                        "name": parts[1].strip(),
                        "department": parts[2].strip(),
                        "email": parts[3].strip(),
                        "events": [
                            event.strip()
                            for event in parts[4].split(";")
                            if event.strip()
                        ]
                    }

                    registrations.append(registration)

        except FileNotFoundError:
            error_records.append(
                f"{file_path.name}: Department file is missing"
            )

    return registrations, error_records
