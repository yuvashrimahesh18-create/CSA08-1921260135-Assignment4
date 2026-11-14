
from decimal import Decimal, InvalidOperation
from pathlib import Path


def process_mess_file(filename):
    total = Decimal("0.00")
    report = []
    rejected_lines = []

    try:
        with open(filename, "r", encoding="utf-8") as f:

            for line_number, line in enumerate(f, start=1):
                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register_number = parts[0].strip()
                    name = parts[1].strip()
                    amount = Decimal(parts[2].strip())

                    if not register_number or not name:
                        raise ValueError("Missing student details")

                    report.append(f"{name} {amount:.2f}")
                    total += amount
                except InvalidOperation:
                  rejected_lines.append(
                   (line_number, line.strip(), "Invalid amount")
                )

                except InvalidOperation:
                   rejected_lines.append(
                       (line_number, line.strip(), "Invalid amount")
                )

                except ValueError as error:
                   rejected_lines.append(
                      (line_number, line.strip(), str(error))
                )

        print("MESS BILL REPORT")
        for record in report:
            print(record)

        print("Total:", f"{total:.2f}")

        print("\nRejected Records:")
        for record in rejected_lines:
            print(record)

    except FileNotFoundError:
        print("Error: File not found:", filename)

    except PermissionError:
        print("Error: Permission denied:", filename)


if __name__ == "__main__":
    input_file = Path(__file__).with_name("mess_oct.txt")
    process_mess_file(input_file)