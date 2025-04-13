from scapy.all import sniff
import threading
import time

class PacketSniffer:
    def __init__(self, interface, packet_callback, filter=''):
        # Extract the interface name without IP address part
        self.interface = self.extract_iface_name(interface)
        self.packet_callback = packet_callback
        self.filter = filter
        self.sniffing = False
        self.paused = False
        self.sniff_thread = None

    def extract_iface_name(self, display_name):
        # Remove the IP address and return only the interface name (e.g., "Wi-Fi")
        return display_name.split(' ')[0]

    def start_sniffing(self):
        # Start sniffing on a separate thread
        self.sniffing = True
        self.paused = False
        self.sniff_thread = threading.Thread(target=self._sniff)
        self.sniff_thread.daemon = True
        self.sniff_thread.start()

    def _sniff(self):
        print("Starting sniffing...")
        while self.sniffing:
            if self.paused:
                # Wait before checking for pause again to prevent high CPU usage
                time.sleep(1)
                continue

            # Sniff a limited number of packets to avoid blocking
            print(f"Sniffing on interface {self.interface} with filter {self.filter}")
            sniff(iface=self.interface, filter=self.filter, prn=self._packet_callback, store=0, timeout=1)

    def stop_sniffing(self):
        # Stop sniffing
        print("Stopping sniffing...")
        self.sniffing = False

    def pause_sniffing(self):
        # Pause sniffing
        print("Pausing sniffing...")
        self.paused = True

    def resume_sniffing(self):
        # Resume sniffing
        print("Resuming sniffing...")
        self.paused = False

    def _packet_callback(self, packet):
        # Process the packet
        print(f"Packet captured: {packet.summary()}")
        self.packet_callback(packet)
