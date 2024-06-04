import datetime


def calculate_weekly_total_hours(worksheet):
    weekly_total_hours = 0.0
    today = datetime.date.today()

    # Check if today is Monday (weekday() returns 0 for Monday)
    if today.weekday() == 0:
        # If it's Monday, only calculate hours for the current week
        for row in worksheet.iter_rows(
            min_row=2, max_row=worksheet.max_row, min_col=6, max_col=6, values_only=True
        ):
            if row[0] is not None:
                if isinstance(row[0], (int, float, str)):
                    weekly_total_hours += float(row[0])
    else:
        # For other days, calculate the total as before
        for row in worksheet.iter_rows(
            min_row=2, max_row=worksheet.max_row, min_col=6, max_col=6, values_only=True
        ):
            if row[0] is not None:
                if isinstance(row[0], (int, float, str)):
                    weekly_total_hours += float(row[0])

    return weekly_total_hours

