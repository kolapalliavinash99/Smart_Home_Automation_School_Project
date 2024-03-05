import time

# Simulated state of smart devices
devices = {
    'light': {'state': False, 'start_time': None, 'duration': 0},
    'thermostat': {'state': False, 'start_time': None, 'duration': 0},
    'security_camera': {'state': 'inactive', 'start_time': None, 'duration': 0},
    'smart_lock': {'state': 'locked', 'start_time': None, 'duration': 0},
    'motion_sensor': {'state': 'inactive', 'start_time': None, 'duration': 0}
}

# Function to control device
def control_device(device_id, action):
    if device_id in devices:
        if action == 'on':
            if not devices[device_id]['state']:
                devices[device_id]['state'] = True
                devices[device_id]['start_time'] = time.time()
                print(f"{device_id} turned on")
            else:
                print(f"{device_id} is already on")
        elif action == 'off':
            if devices[device_id]['state']:
                devices[device_id]['state'] = False
                duration = time.time() - devices[device_id]['start_time']
                devices[device_id]['duration'] += duration
                print(f"{device_id} turned off")
                print(f"Total duration: {devices[device_id]['duration'] / 60:.2f} minutes")
            else:
                print(f"{device_id} is already off")
        else:
            print("Invalid action")
    else:
        print("Device not found")

# Function to handle user input for device selection
def select_device():
    print("Device list:")
    for idx, device_id in enumerate(devices.keys(), 1):
        print(f"{idx}. {device_id}")
    device_idx = int(input("Select device (enter number): ")) - 1
    return list(devices.keys())[device_idx]

# Function to handle user input for action selection
def select_action():
    while True:
        action = input("Enter action (on/off): ")
        if action in ['on', 'off']:
            return action
        else:
            print("Invalid action. Please enter 'on' or 'off'.")

# Function to handle user input for duration
def input_duration():
    duration = float(input("Enter duration in minutes: "))
    return duration * 60  # Convert minutes to seconds

# Function to handle user input for checking duration
def check_duration(device_id):
    print(f"{device_id} is currently running for {devices[device_id]['duration']:.2f} seconds")

# Function to handle user input
def handle_user_input():
    while True:
        device_id = select_device()
        action = select_action()
        duration = input_duration()
        control_device(device_id, action)
        time.sleep(duration)
        control_device(device_id, 'off')
        check_duration(device_id)
        more_input = input("Press Enter to control another device or 'q' to quit: ")
        if more_input.lower() == 'q':
            break

if __name__ == '__main__':
    # Prompt user for input to control devices
    handle_user_input()
