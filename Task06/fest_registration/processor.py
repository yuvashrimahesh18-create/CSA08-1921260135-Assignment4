
from .validator import validate_registration


def process_registrations(registrations, error_records):
    clean_records = []
    seen_register_numbers = set()

    for registration in registrations:
        register = registration["register_number"]

        if register in seen_register_numbers:
            error_records.append(
                f"{register}: Duplicate registration"
            )
            continue

        seen_register_numbers.add(register)

        is_valid, message = validate_registration(registration)

        if not is_valid:
            error_records.append(
                f"{register}: {message}"
            )
            continue

        clean_records.append(registration)

    return clean_records, error_records
