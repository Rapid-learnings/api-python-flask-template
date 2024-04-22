from datetime import datetime, timedelta, timezone


def convert_to_unix_timestamp(iso_str):
    """Convert ISO 8601 format string to UNIX timestamp, handling fractional seconds and timezone."""
    if iso_str is None:
        return None

    # Split the string into the main part and the timezone offset
    parts = iso_str.split("+")
    main_part = parts[0]
    tz_offset = parts[1] if len(parts) > 1 else "00:00"

    # Handle fractional seconds by splitting further
    datetime_part, _, fractional = main_part.partition(".")
    datetime_obj = datetime.strptime(datetime_part, "%Y-%m-%dT%H:%M:%S")

    # Add fractional seconds back to the datetime object, if present
    if fractional:
        fractional_seconds = float("0." + fractional.rstrip("Z"))
        datetime_obj += timedelta(seconds=fractional_seconds)

    # Parse timezone offset
    if tz_offset != "00:00":
        hours, minutes = map(int, tz_offset.split(":"))
        tz_delta = timedelta(hours=hours, minutes=minutes)
        datetime_obj = datetime_obj.replace(tzinfo=timezone.utc) - tz_delta
    else:
        datetime_obj = datetime_obj.replace(tzinfo=timezone.utc)

    return int(datetime_obj.timestamp())
