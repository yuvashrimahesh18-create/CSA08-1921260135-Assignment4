
def validate_registration(registration):
    register = registration["register_number"]
    name = registration["name"]
    department = registration["department"]
    email = registration["email"]
    events = registration["events"]

    if not register or not name or not department:
        return False, "Missing required student details"

    if "@" not in email:
        return False, "Invalid email address: missing @"

    username, separator, domain = email.partition("@")

    if (
        not username
        or not domain
        or "." not in domain
        or domain.startswith(".")
        or domain.endswith(".")
    ):
        return False, "Invalid email address"

    if not events:
        return False, "No events selected"

    return True, "Valid registration"
