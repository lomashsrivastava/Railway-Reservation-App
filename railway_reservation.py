import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
from PIL import Image, ImageTk
import qrcode
from ttkbootstrap import Style

# Main Application Class
class RailwayReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Indian Railway Reservation System")
        self.root.geometry("1200x800")
        self.style = Style(theme="cosmo")  # Default theme

        # Store booked tickets for PNR checking
        self.booked_tickets = {}

        # Store ticket details temporarily
        self.ticket_details = {}

        # Main Screen
        self.main_screen()

    def main_screen(self):
        self.clear_screen()
        label = ttk.Label(
            self.root,
            text="Indian Railway Reservation System",
            font=("Helvetica", 28, "bold"),
        )
        label.pack(pady=50)

        register_button = ttk.Button(
            self.root,
            text="Register / Login",
            style="primary.TButton",
            command=self.register_screen,
        )
        register_button.pack(pady=20)

        theme_button = ttk.Button(
            self.root,
            text="Change Theme",
            style="info.TButton",
            command=self.change_theme,
        )
        theme_button.pack(pady=10)

    def register_screen(self):
        self.clear_screen()
        label = ttk.Label(
            self.root,
            text="Register",
            font=("Helvetica", 24, "bold"),
        )
        label.pack(pady=20)

        self.full_name = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.full_name.insert(0, "Enter Your Full Name")
        self.full_name.pack(pady=10)

        self.mobile_number = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.mobile_number.insert(0, "Mobile Number (10 Digits)")
        self.mobile_number.pack(pady=10)

        self.aadhaar_number = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.aadhaar_number.insert(0, "Aadhaar Card Number (12 Digits)")
        self.aadhaar_number.pack(pady=10)

        self.age = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.age.insert(0, "Enter Your Age")
        self.age.pack(pady=10)

        self.address = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.address.insert(0, "Enter Your Address")
        self.address.pack(pady=10)

        self.pincode = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.pincode.insert(0, "Enter Your Pincode")
        self.pincode.pack(pady=10)

        self.user_id = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.user_id.insert(0, "Enter Your ID")
        self.user_id.pack(pady=10)

        self.password = ttk.Entry(self.root, font=("Helvetica", 14), width=30, show="*")
        self.password.insert(0, "Enter Your Password")
        self.password.pack(pady=10)

        submit_button = ttk.Button(
            self.root,
            text="Submit",
            style="success.TButton",
            command=self.register_user,
        )
        submit_button.pack(pady=20)

        login_button = ttk.Button(
            self.root,
            text="Login",
            style="primary.TButton",
            command=self.login_screen,
        )
        login_button.pack(pady=10)

    def login_screen(self):
        self.clear_screen()
        label = ttk.Label(
            self.root,
            text="Login",
            font=("Helvetica", 24, "bold"),
        )
        label.pack(pady=20)

        self.login_id = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.login_id.insert(0, "Enter Your ID")
        self.login_id.pack(pady=10)

        self.login_password = ttk.Entry(self.root, font=("Helvetica", 14), width=30, show="*")
        self.login_password.insert(0, "Enter Your Password")
        self.login_password.pack(pady=10)

        login_button = ttk.Button(
            self.root,
            text="Login",
            style="success.TButton",
            command=self.login_user,
        )
        login_button.pack(pady=20)

        register_button = ttk.Button(
            self.root,
            text="Register",
            style="primary.TButton",
            command=self.register_screen,
        )
        register_button.pack(pady=10)

    def book_ticket_screen(self):
        self.clear_screen()
        label = ttk.Label(
            self.root,
            text="Book Train Ticket",
            font=("Helvetica", 24, "bold"),
        )
        label.pack(pady=20)

        self.passenger_name = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.passenger_name.insert(0, "Enter Full Name")
        self.passenger_name.pack(pady=10)

        self.passenger_age = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.passenger_age.insert(0, "Enter Your Age")
        self.passenger_age.pack(pady=10)

        self.train_name = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.train_name.insert(0, "Enter Train Name")
        self.train_name.pack(pady=10)

        self.train_number = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.train_number.insert(0, "Enter Train Number")
        self.train_number.pack(pady=10)

        self.departure_station = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.departure_station.insert(0, "Departure Station Name")
        self.departure_station.pack(pady=10)

        self.destination_station = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.destination_station.insert(0, "Destination Station Name")
        self.destination_station.pack(pady=10)

        self.journey_class = ttk.Combobox(
            self.root,
            values=["Sleeper", "AC Tier 3", "AC Tier 2", "AC Tier 1", "EC", "CC", "Executive", "Compartment"],
            font=("Helvetica", 14),
            width=28,
        )
        self.journey_class.set("Choose Journey Class")
        self.journey_class.pack(pady=10)

        self.journey_date = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.journey_date.insert(0, "Journey Date (YYYY-MM-DD)")
        self.journey_date.pack(pady=10)

        submit_button = ttk.Button(
            self.root,
            text="Proceed to Payment",
            style="success.TButton",
            command=self.store_ticket_details,
        )
        submit_button.pack(pady=20)

        pnr_button = ttk.Button(
            self.root,
            text="Check PNR Status",
            style="info.TButton",
            command=self.pnr_status_screen,
        )
        pnr_button.pack(pady=10)

    def store_ticket_details(self):
        # Store ticket details temporarily before switching screens
        self.ticket_details = {
            "Passenger Name": self.passenger_name.get(),
            "Age": self.passenger_age.get(),
            "Train Name": self.train_name.get(),
            "Train Number": self.train_number.get(),
            "Departure Station": self.departure_station.get(),
            "Destination Station": self.destination_station.get(),
            "Class": self.journey_class.get(),
            "Journey Date": self.journey_date.get(),
        }
        self.payment_screen()

    def payment_screen(self):
        self.clear_screen()
        label = ttk.Label(
            self.root,
            text="Payment Options",
            font=("Helvetica", 24, "bold"),
        )
        label.pack(pady=20)

        upi_button = ttk.Button(
            self.root,
            text="Pay via UPI",
            style="primary.TButton",
            command=self.upi_payment,
        )
        upi_button.pack(pady=20)

        barcode_button = ttk.Button(
            self.root,
            text="Generate Barcode",
            style="secondary.TButton",
            command=self.generate_barcode,
        )
        barcode_button.pack(pady=20)

        back_button = ttk.Button(
            self.root,
            text="Back",
            style="danger.TButton",
            command=self.book_ticket_screen,
        )
        back_button.pack(pady=10)

    def upi_payment(self):
        messagebox.showinfo("UPI Payment", "Redirecting to UPI payment gateway...")
        time.sleep(2)
        self.book_ticket()

    def generate_barcode(self):
        # Generate a random 10-digit PNR number
        pnr = random.randint(1000000000, 9999999999)

        # Store ticket details with the PNR number
        self.book_ticket(pnr)

        # Generate QR code for the PNR number
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f"PNR: {pnr}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("barcode.png")

        # Display the QR code in a new window
        barcode_window = tk.Toplevel(self.root)
        barcode_window.title("Barcode")
        barcode_label = ttk.Label(barcode_window, text="Scan the Barcode for Payment")
        barcode_label.pack(pady=10)

        barcode_image = ImageTk.PhotoImage(Image.open("barcode.png"))
        barcode_image_label = ttk.Label(barcode_window, image=barcode_image)
        barcode_image_label.image = barcode_image
        barcode_image_label.pack(pady=10)

        close_button = ttk.Button(
            barcode_window,
            text="Close",
            style="danger.TButton",
            command=barcode_window.destroy,
        )
        close_button.pack(pady=10)

        # Schedule the payment success message after 30 seconds
        self.root.after(30000, self.show_payment_success, pnr)

    def show_payment_success(self, pnr):
        messagebox.showinfo("Payment Successful", f"Payment Successful! Your PNR Number is: {pnr}")

    def book_ticket(self, pnr=None):
        if pnr is None:
            pnr = random.randint(1000000000, 9999999999)
        self.booked_tickets[pnr] = self.ticket_details
        messagebox.showinfo("Success", f"Ticket Booked Successfully! Your PNR Number is: {pnr}")

    def pnr_status_screen(self):
        self.clear_screen()
        label = ttk.Label(
            self.root,
            text="Check PNR Status",
            font=("Helvetica", 24, "bold"),
        )
        label.pack(pady=20)

        self.pnr_entry = ttk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.pnr_entry.insert(0, "Enter PNR Number")
        self.pnr_entry.pack(pady=10)

        check_button = ttk.Button(
            self.root,
            text="Check Status",
            style="info.TButton",
            command=self.check_pnr_status,
        )
        check_button.pack(pady=20)

        back_button = ttk.Button(
            self.root,
            text="Back",
            style="danger.TButton",
            command=self.book_ticket_screen,
        )
        back_button.pack(pady=10)

    def check_pnr_status(self):
        try:
            pnr = int(self.pnr_entry.get())
            if pnr in self.booked_tickets:
                ticket_details = self.booked_tickets[pnr]
                details = "\n".join([f"{key}: {value}" for key, value in ticket_details.items()])
                messagebox.showinfo("PNR Status", f"PNR Status: Confirmed\n\n{details}")
            else:
                messagebox.showerror("Error", "Invalid PNR Number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid 10-digit PNR number.")

    def register_user(self):
        messagebox.showinfo("Success", "Registration Successful! Please login.")
        self.login_screen()

    def login_user(self):
        messagebox.showinfo("Success", "Login Successful!")
        self.book_ticket_screen()

    def change_theme(self):
        themes = ["cosmo", "flatly", "journal", "lumen", "minty", "pulse", "sandstone", "yeti"]
        current_theme = self.style.theme_use()
        next_theme = themes[(themes.index(current_theme) + 1) % len(themes)]  # Fixed parenthesis
        self.style.theme_use(next_theme)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = RailwayReservationSystem(root)
    root.mainloop()