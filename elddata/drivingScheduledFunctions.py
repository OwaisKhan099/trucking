from datetime import datetime,timedelta
def plan_driving_schedule(pickup_time_str, dropoff_time_str, total_drive_hours):
    # Parse the pickup and dropoff times
    pickup_time = datetime.strptime(pickup_time_str, "%Y-%m-%dT%H:%M:%SZ")
    dropoff_time = datetime.strptime(dropoff_time_str, "%Y-%m-%dT%H:%M:%SZ")

    # Initialize variables
    drive_hours_remaining = total_drive_hours
    current_time = pickup_time
    schedule = []

    # Helper function to add time blocks to the schedule
    def add_time_block(start_time, end_time, activity):
        schedule.append({
            'start_time': start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            'end_time': end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            'activity': activity
        })

    # Calculate schedule
    while drive_hours_remaining > 0 and current_time < dropoff_time:
        # Drive for a maximum of 8 hours or the remaining drive hours, whichever is less
        drive_hours = min(drive_hours_remaining, 8)
        end_drive_time = current_time + timedelta(hours=drive_hours)

        # Check if the end drive time exceeds the dropoff time
        if end_drive_time > dropoff_time:
            end_drive_time = dropoff_time

        add_time_block(current_time, end_drive_time, 'Driving')
        current_time = end_drive_time
        drive_hours_remaining -= drive_hours

        # Take a 30-minute break if there's more driving to do
        if drive_hours_remaining > 0:
            break_time = current_time + timedelta(minutes=30)
            add_time_block(current_time, break_time, 'Break')
            current_time = break_time

    # Return the planned schedule
    return schedule


# Example usage
pickup_time = "2024-07-01T08:00:00Z"
dropoff_time = "2024-07-01T20:00:00Z"
total_drive_hours = 10

schedule = plan_driving_schedule(pickup_time, dropoff_time, total_drive_hours)
for event in schedule:
    print(f"From {event['start_time']} to {event['end_time']}: {event['activity']}")

