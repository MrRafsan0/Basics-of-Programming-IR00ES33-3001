# Time Travel Safety System

def time_travel_safety_check(user_device_charge, user_age, has_time_training, has_companion):
    # Safety check messages
    print("🔍 Analyzing temporal jump safety...")

    # Safety flags
    charge_ok = user_device_charge > 75
    age_ok = user_age >= 16
    training_ok = has_time_training.lower() == "yes"
    companion_ok = has_companion.lower() == "yes"

    # List of failure messages
    failure_messages = []

    if not charge_ok:
        failure_messages.append("🚫 Device charge too low! You need at least 75% power.")
    if not age_ok:
        failure_messages.append(f"🚫 Time travel minimum age not met. Return in {16 - user_age} year(s)!")
    if not (training_ok or companion_ok):
        failure_messages.append("🚫 No training or companion? That's like trying to pilot a rocket after watching a 5-minute YouTube tutorial!")

    # Output messages based on checks
    if failure_messages:
        for message in failure_messages:
            print(message)
        print("\n❌ TIME JUMP DENIED!\n   Please address all safety concerns before attempting temporal displacement.")
    else:
        print("✅ TIME JUMP APPROVED!\n   Try not to step on any butterflies!")

# Example test calls
time_travel_safety_check(50, 15, "no", "no")
time_travel_safety_check(80, 18, "yes", "no")
