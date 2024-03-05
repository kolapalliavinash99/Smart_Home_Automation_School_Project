import tkinter as tk
from tkinter import messagebox

# Simulated state of smart devices
devices = {
    'light': False,
    'thermostat': False,
    'security_camera': False,
    'smart_lock': False,
    'motion_sensor': False
}

# Function to toggle device state
def toggle_device_state(device_id):
    devices[device_id] = not devices[device_id]
    if devices[device_id]:
        messagebox.showinfo("Device Control", f"{device_id.capitalize()} turned on")
    else:
        messagebox.showinfo("Device Control", f"{device_id.capitalize()} turned off")

# Create main window
root = tk.Tk()
root.title("Smart Home Dashboard")

# Create buttons for each device
for device_id in devices.keys():
    button = tk.Button(root, text=device_id.capitalize(), command=lambda dev=device_id: toggle_device_state(dev))
    button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
