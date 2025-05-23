import os

FILENAME = "reservations.txt"
ADULT_RATE = 500
CHILD_RATE = 300

class Reservation:
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children

    def subtotal(self):
        return self.adults * ADULT_RATE + self.children * CHILD_RATE

    def to_line(self):
        return f"{self.date}|{self.time}|{self.name}|{self.adults}|{self.children}\n"

    @staticmethod
    def from_line(line):
        date, time, name, adults, children = line.strip().split("|")
        return Reservation(name, date, time, int(adults), int(children))

class ReservationSystem:
    def __init__(self):
        self.reservations = []
        self.load_reservations()

    def load_reservations(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                self.reservations = [Reservation.from_line(line) for line in file]

    def save_reservations(self):
        with open(FILENAME, "w") as file:
            for res in self.reservations:
                file.write(res.to_line())

    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.")
            return
        print("# Date       Time     Name              Adults Children")
        for i, res in enumerate(self.reservations, 1):
            print(f"{i} {res.date:10} {res.time:8} {res.name:17} {res.adults:6} {res.children:8}")

    def make_reservation(self):
        try:
            name = input("Enter name: ")
            date = input("Enter date (e.g. Nov 10, 2020): ")
            time = input("Enter time (e.g. 10:00 am): ")
            adults = int(input("Enter number of adults: "))
            children = int(input("Enter number of children: "))
            if adults < 1 and children < 1:
                raise ValueError("At least one guest must be reserved.")
            self.reservations.append(Reservation(name, date, time, adults, children))
            self.save_reservations()
            print("Reservation added successfully!")
        except ValueError as ve:
            print("Invalid input:", ve)

    def delete_reservation(self):
        try:
            self.view_reservations()
            idx = int(input("Enter reservation number to delete: ")) - 1
            if idx < 0 or idx >= len(self.reservations):
                raise IndexError("Reservation number out of range.")
            del self.reservations[idx]
            self.save_reservations()
            print("Reservation deleted successfully!")
        except (ValueError, IndexError) as e:
            print("Error:", e)

    def generate_report(self):
        if not self.reservations:
            print("No reservations to report.")
            return
        total_adults = total_kids = grand_total = 0
        print("# Date       Time     Name              Adults Children Subtotal")
        for i, res in enumerate(self.reservations, 1):
            subtotal = res.subtotal()
            print(f"{i} {res.date:10} {res.time:8} {res.name:17} {res.adults:6} {res.children:8} {subtotal:8.2f}")
            total_adults += res.adults
            total_kids += res.children
            grand_total += subtotal
        print(f"\nTotal number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_kids}")
        print(f"Grand Total: PHP {grand_total:.2f}")

def main():
    system = ReservationSystem()
    while True:
        print("\n--- WELCOME TO JAMES N JAMERO{} RESTAURANT DINING RESERVATION SYSTEM ---")
        print("1. VIEW RESERVATIONS")
        print("2. MAKE RESERVATION")
        print("3. DELETE RESERVATION")
        print("4. GENERATE REPORT")
        print("5. EXIT")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            system.view_reservations()
        elif choice == '2':
            system.make_reservation()
        elif choice == '3':
            system.delete_reservation()
        elif choice == '4':
            system.generate_report()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid selection. Please choose between 1 to 5.")

if __name__ == "__main__":
    main()
