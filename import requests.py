import tkinter as tk
from tkinter import messagebox
import requests

def get_vendor_by_mac(mac_address):
    try:
        # Format the MAC address to remove any separators like ":" or "-"
        formatted_mac = mac_address.replace(":", "").replace("-", "").upper()

        # Use an online API to get the vendor information
        url = f"https://api.macvendors.com/{formatted_mac}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            return "Vendor not found or invalid MAC address."
    except Exception as e:
        return str(e)

def show_vendor():
    mac_address = entry.get()
    if mac_address:
        vendor = get_vendor_by_mac(mac_address)
        result_label.config(text=f"Result: {vendor}")
    else:
        messagebox.showwarning("Input Error", "Please enter a MAC address.")

# Set up the main application window
root = tk.Tk()
root.title("MAC Address Lookup")

# Create and place widgets
label = tk.Label(root, text="Enter MAC Address:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Lookup", command=show_vendor)
button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", wraplength=300)
result_label.pack(pady=20)

# Start the application
root.mainloop()
