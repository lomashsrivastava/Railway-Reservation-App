# Indian Railway Reservation System

## Overview
The **Indian Railway Reservation System** is a GUI-based application built using Python and Tkinter. It allows users to register, log in, book train tickets, generate barcodes for payments, and check PNR statuses. The system provides a user-friendly interface with modern themes using the `ttkbootstrap` library.

## Features
- User Registration and Login System
- Ticket Booking with Passenger Details
- Journey Class Selection
- Payment Gateway Simulation (UPI & Barcode Generation)
- QR Code Barcode Generation for Payments
- PNR Status Check
- Dynamic Theme Switching
- Ticket Storage with PNR Mapping
- Modern GUI Design

## Technologies Used
- Python
- Tkinter
- ttkbootstrap (Themed Widgets)
- Pillow (Image Processing)
- qrcode (QR Code Generation)
- Random Library
- Time Library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/railway-reservation-system.git
   cd railway-reservation-system
   ```

2. Install the required dependencies:
   ```bash
   pip install pillow qrcode ttkbootstrap
   ```

3. Run the application:
   ```bash
   python railway_reservation.py
   ```

## How to Use
### Registration
1. Launch the application.
2. Click on **Register / Login**.
3. Enter your personal details like Full Name, Mobile Number, Aadhaar Number, Age, Address, Pincode, User ID, and Password.
4. Click on **Submit** to register.

### Login
1. Go to the Login Screen.
2. Enter your User ID and Password.
3. Click **Login** to proceed to the ticket booking section.

### Ticket Booking
1. Enter passenger details including Name, Age, Train Name, Train Number, Departure, and Destination Stations.
2. Select the Journey Class from the dropdown.
3. Choose the Journey Date.
4. Click **Proceed to Payment**.

### Payment
1. Choose either **UPI Payment** or **Generate Barcode**.
2. For Barcode Payment, scan the generated QR code.
3. Payment will be confirmed automatically after 30 seconds.

### PNR Status
1. Go to the PNR Status Check screen.
2. Enter your PNR number.
3. Click **Check Status** to view your booking details.

## Themes Available
- Cosmo
- Flatly
- Journal
- Lumen
- Minty
- Pulse
- Sandstone
- Yeti

## Folder Structure
```plaintext
📂 railway-reservation-system
├─ railway_reservation.py  # Main Application File
├─ barcode.png            # QR Code Image
└─ README.md             # Project Documentation
```

## Dependencies
- Python 3.x
- Pillow
- qrcode
- ttkbootstrap

## License
This project is licensed under the **MIT License**.

## Author
Lomash Srivastava

## Contact
- Email: lomashgroups@gmail.com
- GitHub: [Lomash Srivastava](https://github.com/lomashsrivastava)

## Acknowledgements
- Tkinter Documentation
- ttkbootstrap Library
- Indian Railway Official Website (Design Reference)
