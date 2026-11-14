
from pathlib import Path


def write_reports(registrations, error_records, output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    # 1. Write the clean master registration list
    master_file = output_folder / "master_list.txt"

    with open(master_file, "w", encoding="utf-8") as file:
        file.write("COLLEGE FEST MASTER REGISTRATION LIST\n")
        file.write("=" * 45 + "\n")

        for record in registrations:
            file.write(
                f"{record['register_number']} | "
                f"{record['name']} | "
                f"{record['department']} | "
                f"{record['email']} | "
                f"Events: {', '.join(record['events'])}\n"
            )

    # 2. Group students by event
    event_participants = {}

    for record in registrations:
        for event in record["events"]:
            event_participants.setdefault(event, []).append(record)

    # 3. Write a separate participant file for each event
    event_folder = output_folder / "event_participants"
    event_folder.mkdir(parents=True, exist_ok=True)

    for event, participants in event_participants.items():
        safe_name = "".join(
            character.lower() if character.isalnum() else "_"
            for character in event
        ).strip("_")

        event_file = event_folder / f"{safe_name}.txt"

        with open(event_file, "w", encoding="utf-8") as file:
            file.write(f"PARTICIPANTS - {event}\n")
            file.write("=" * 35 + "\n")

            for student in participants:
                file.write(
                    f"{student['register_number']} | "
                    f"{student['name']} | "
                    f"{student['department']}\n"
                )

    # 4. Write summary report
    summary_file = output_folder / "summary_report.txt"

    with open(summary_file, "w", encoding="utf-8") as file:
        file.write("COLLEGE FEST SUMMARY REPORT\n")
        file.write("=" * 35 + "\n")
        file.write(f"Total valid registrations: {len(registrations)}\n")
        file.write(f"Total events: {len(event_participants)}\n")

        file.write("\nEVENT-WISE PARTICIPANT COUNT\n")

        for event, participants in sorted(event_participants.items()):
            file.write(f"{event}: {len(participants)}\n")

        file.write(f"\nTotal error records: {len(error_records)}\n")

    # 5. Write error log
    error_file = output_folder / "error_log.txt"

    with open(error_file, "w", encoding="utf-8") as file:
        file.write("COLLEGE FEST ERROR LOG\n")
        file.write("=" * 35 + "\n")

        if error_records:
            for error in error_records:
                file.write(error + "\n")
        else:
            file.write("No errors found.\n")

    print("College fest reports generated successfully!")
    print(f"Master list: {master_file}")
    print(f"Summary report: {summary_file}")
    print(f"Error log: {error_file}")
    print(f"Event participant files: {event_folder}")
