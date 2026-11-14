
from pathlib import Path

from fest_registration.reader import read_department_files
from fest_registration.processor import process_registrations
from fest_registration.report import write_reports


def main():
    base_folder = Path(__file__).resolve().parent

    input_folder = base_folder / "input_files"
    output_folder = base_folder / "output_files"

    print("COLLEGE FEST REGISTRATION PROCESSOR")
    print("=" * 40)

    registrations, error_records = read_department_files(input_folder)

    clean_records, error_records = process_registrations(
        registrations, error_records
    )

    write_reports(clean_records, error_records, output_folder)


if __name__ == "__main__":
    main()
