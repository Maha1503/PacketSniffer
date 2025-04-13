import tkinter as tk
from tkinter import ttk
from scapy.all import get_if_list
from sniffer import PacketSniffer
import threading
import psutil

def get_friendly_interfaces():
    interfaces = []
    for nic, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family.name == 'AF_INET':
                interfaces.append(f"{nic} ({addr.address})")
    return interfaces

def extract_iface_name(display_name):
    return display_name.split(' (')[0] if ' (' in display_name else display_name

class SnifferApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Packet Sniffer")
        self.root.geometry("1000x600")
        self.root.config(bg='#1a1a1a')

        # Set up font for a terminal look
        self.font = ('Courier New', 10)

        # Interface Dropdown
        tk.Label(self.root, text="Select Interface:", fg='#00FF00', font=self.font, bg='#1a1a1a').pack(anchor='w', padx=10, pady=5)
        self.friendly_interfaces = get_friendly_interfaces()
        self.interface_var = tk.StringVar()
        self.interface_dropdown = ttk.Combobox(self.root, textvariable=self.interface_var, values=self.friendly_interfaces, state="readonly", font=self.font)
        self.interface_dropdown.pack(fill='x', padx=10)

        # Try to auto-select Wi-Fi interface
        for iface in self.friendly_interfaces:
            if "Wi-Fi" in iface or "Wireless" in iface:
                self.interface_var.set(iface)
                break
        else:
            self.interface_var.set(self.friendly_interfaces[0] if self.friendly_interfaces else "")

        # Filter input
        tk.Label(self.root, text="Packet Filter (e.g. tcp, udp, ip):", fg='#00FF00', font=self.font, bg='#1a1a1a').pack(anchor='w', padx=10, pady=5)
        self.filter_entry = tk.Entry(self.root, font=self.font, bg='#333333', fg='#00FF00', insertbackground='white')
        self.filter_entry.pack(fill='x', padx=10)

        # Start Sniffing Button
        self.start_button = tk.Button(self.root, text="Start Sniffing", command=self.start_sniffing_thread, font=self.font, bg='#000000', fg='#00FF00', relief=tk.FLAT)
        self.start_button.pack(pady=10)

        # Pause Sniffing Button (Initially hidden)
        self.pause_button = tk.Button(self.root, text="Pause Sniffing", command=self.pause_sniffing, font=self.font, bg='#000000', fg='#FF8800', relief=tk.FLAT)
        self.pause_button.pack(pady=10)
        self.pause_button.pack_forget()  # Hide until sniffing starts

        # Packet display
        self.text_area = tk.Text(self.root, wrap=tk.NONE, font=self.font, bg='#1a1a1a', fg='#00FF00', insertbackground='white', borderwidth=2, relief=tk.SUNKEN)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        # Add scrollbar
        y_scroll = tk.Scrollbar(self.text_area, command=self.text_area.yview, bg='#00FF00')
        self.text_area.configure(yscrollcommand=y_scroll.set)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.sniffer = None

    def start_sniffing_thread(self):
        self.start_button.config(state=tk.DISABLED, bg='#808080')
        self.sniffer = PacketSniffer(
            interface=self.interface_var.get(),
            packet_callback=self.packet_callback,
            filter=self.filter_entry.get()
        )
        self.sniffer.start_sniffing()
        self.pause_button.pack()  # Show the pause button

    def packet_callback(self, packet):
        summary = packet.summary()
        headers = packet.show(dump=True)
        self.text_area.insert(tk.END, f"{summary}\n{headers}\n{'-'*80}\n")
        self.text_area.see(tk.END)

    def pause_sniffing(self):
        if self.sniffer:
            self.sniffer.pause_sniffing()
        self.pause_button.config(state=tk.DISABLED, bg='#808080')  # Disable pause button while paused
        threading.Thread(target=self.resume_sniffing_after_delay).start()

    def resume_sniffing_after_delay(self):
        threading.Event().wait(3)  # Wait for 3 seconds
        if self.sniffer:
            self.sniffer.resume_sniffing()
        self.pause_button.config(state=tk.NORMAL, bg='#FF8800')  # Re-enable pause button

    def run(self):
        self.root.mainloop()
