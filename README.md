# Packet Sniffer
          $$ $$$$$ $$
              $$ $$$$$ $$
             .$$ $$$$$ $$.
             :$$ $$$$$ $$:
             $$$ $$$$$ $$$
             $$$ $$$$$ $$$
            ,$$$ $$$$$ $$$.
           ,$$$$ $$$$$ $$$$.
          ,$$$$; $$$$$ :$$$$.
         ,$$$$$  $$$$$  $$$$$.
       ,$$$$$$'  $$$$$  `$$$$$$.
     ,$$$$$$$'   $$$$$   `$$$$$$$.
  ,s$$$$$$$'     $$$$$     `$$$$$$$s.
$$$$$$$$$'       $$$$$       `$$$$$$$$$
$$$$$Y'          $$$$$          `Y$$$$$

## Overview

This project is a packet sniffer tool designed to capture and analyze network packets on a selected network interface. It uses the `scapy` library to sniff packets and display them in a user-friendly format. The tool provides basic functionalities such as starting, pausing, and resuming packet sniffing.

**Note**: This project is currently under development. Some features may be subject to changes or improvements in future versions.

## Features

- Capture packets on a selected network interface.
- Filter packets based on protocol (e.g., TCP, UDP, IP).
- Pause and resume sniffing as needed.
- Display packet summaries and details.
- Start and stop sniffing with a clean user interface built using `Tkinter`.

## Requirements

- Python 3.x
- `scapy` library
- `psutil` library
- `tkinter` library (included with Python standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/packet-sniffer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd packet-sniffer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Select a network interface from the dropdown list.
3. Enter a packet filter (e.g., `tcp`, `udp`, `ip`).
4. Click **Start Sniffing** to begin capturing packets.
5. Use the **Pause** button to pause sniffing and the **Resume** button to continue.
6. Click **Stop Sniffing** to stop the packet sniffing process.

## Example

Upon starting the sniffing process, the application will display captured packet details:

```
Starting sniffing...
Sniffing on interface Wi-Fi with filter: tcp
Packet captured: <Packet Summary>
<Packet Details>
----------------------------------------
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

