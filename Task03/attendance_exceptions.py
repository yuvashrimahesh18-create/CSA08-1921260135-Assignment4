
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when an attendance record is invalid."""


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    register_number = parts[0].strip()
    date = parts[1].strip()
    status = parts[2].strip()

    if not register_number or not date:
        raise InvalidRecord("missing student details")

    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")

    return register_number, date, status


def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    register, date, status = parse_line(line)

                    if status == "P":
                        present += 1
                    else:
                        absent += 1

                except InvalidRecord as error:
                    errors.append((line_number, str(error)))

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Attendance file not found: {path}"
        ) from error

    return present, absent, errors


data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

with tempfile.NamedTemporaryFile(
    "w", suffix=".csv", delete=False, encoding="utf-8"
) as tmp:
    tmp.write(data)
    file_path = tmp.name

try:
    result = summarise(file_path)

except FileNotFoundError as error:
    print("ERROR:", error)

else:
    print(result)

finally:
    print("Attendance processing attempt finished.")
    if os.path.exists(file_path):
        os.remove(file_path)
print("\n--- MISSING FILE TEST ---")

try:
    summarise("missing_attendance.csv")

except FileNotFoundError as error:
    print("Handled error:", error)
    print("\n--- BROAD EXCEPTION TEST ---")

try:
    result = 10 / 0
    print(result)

except Exception:
    pass

print("Program continued without displaying the error.")