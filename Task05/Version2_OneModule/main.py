
from attendance_module import read_attendance, write_reports


if __name__ == "__main__":
    attendance, damaged_records = read_attendance()
    write_reports(attendance, damaged_records)

    print("Reports generated successfully!")
    print("Attendance report created.")
    print("Three-day absence report created.")
    print("Damaged records report created.")
