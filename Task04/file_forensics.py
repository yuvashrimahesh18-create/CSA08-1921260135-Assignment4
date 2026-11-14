
from pathlib import Path

folder = Path(__file__).parent


def save_returns(books):
    log_path = folder / "returns.log"

    try:
        with open(log_path, "a", encoding="utf-8") as log:
            for book in books:
                if book.strip():
                    log.write(book.strip() + "\n")

    except OSError as error:
        error_path = folder / "error.log"

        with open(error_path, "a", encoding="utf-8") as error_file:
            error_file.write(f"Write failed: {error}\n")

        print("Error while writing:", error)


def process(day_file):
    try:
        with open(folder / day_file, "r", encoding="utf-8") as file:
            books = file.readlines()

        save_returns(books)

    except FileNotFoundError:
        print(f"Missing file: {day_file}")

    except OSError as error:
        print(f"File processing error: {error}")


# Clear the previous log for a fresh test
try:
    (folder / "returns.log").write_text("", encoding="utf-8")
except OSError as error:
    print("Could not clear log:", error)

# Process all three days
process("day1.txt")
process("day2.txt")
process("day3.txt")

# Display the corrected log
print("\n--- CORRECTED RETURN LOG ---")

try:
    with open(folder / "returns.log", "r", encoding="utf-8") as log:
        print(log.read())
except OSError as error:
    print("Could not read log:", error)
