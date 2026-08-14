import threading
import time
from datetime import datetime


class Alarm:
    def __init__(self, alarm_id, alarm_time, label="Alarm"):
        self.id = alarm_id
        self.alarm_time = alarm_time
        self.label = label
        self.triggered = False


class AlarmClock:
    def __init__(self):
        self.alarms = []
        self.next_id = 1
        self.running = True

    def add_alarm(self, alarm_time, label="Alarm"):
        alarm = Alarm(self.next_id, alarm_time, label)
        self.alarms.append(alarm)
        self.next_id += 1

        print(
            f"✅ Alarm #{alarm.id} set for {alarm.alarm_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def list_alarms(self):
        if not self.alarms:
            print("No alarms scheduled.")
            return

        print("\nScheduled Alarms:")
        print("-" * 50)

        for alarm in self.alarms:
            status = "Triggered" if alarm.triggered else "Pending"

            print(
                f"[{alarm.id}] "
                f"{alarm.alarm_time.strftime('%Y-%m-%d %H:%M:%S')} "
                f"| {alarm.label} "
                f"| {status}"
            )

    def remove_alarm(self, alarm_id):
        for alarm in self.alarms:
            if alarm.id == alarm_id:
                self.alarms.remove(alarm)
                print(f"✅ Alarm {alarm_id} removed.")
                return

        print("❌ Alarm not found.")

    def check_alarms(self):
        while self.running:
            now = datetime.now()

            for alarm in self.alarms:
                if not alarm.triggered and now >= alarm.alarm_time:
                    alarm.triggered = True

                    print("\n")
                    print("=" * 50)
                    print("⏰ ALARM TRIGGERED!")
                    print(f"ID    : {alarm.id}")
                    print(f"Label : {alarm.label}")
                    print(
                        f"Time  : {alarm.alarm_time.strftime('%Y-%m-%d %H:%M:%S')}"
                    )
                    print("=" * 50)
                    print("\n")

            time.sleep(1)

    def shutdown(self):
        self.running = False


def print_help():
    print(
        """
Available Commands:

1. add
   Add a new alarm

2. list
   View scheduled alarms

3. remove
   Remove an alarm by ID

4. help
   Show available commands

5. exit
   Exit application
"""
    )


def get_alarm_datetime():
    while True:
        date_input = input(
            "Enter datetime (YYYY-MM-DD HH:MM:SS): "
        ).strip()

        try:
            alarm_time = datetime.strptime(
                date_input,
                "%Y-%m-%d %H:%M:%S"
            )

            if alarm_time <= datetime.now():
                print("❌ Please enter a future date/time.")
                continue

            return alarm_time

        except ValueError:
            print("❌ Invalid format.")


def main():
    print("=" * 60)
    print("CLI Alarm Clock")
    print("=" * 60)

    clock = AlarmClock()

    monitor_thread = threading.Thread(
        target=clock.check_alarms,
        daemon=True
    )

    monitor_thread.start()

    print_help()

    while True:
        try:
            command = input("\n> ").strip().lower()

            if command == "add":
                alarm_time = get_alarm_datetime()

                label = input(
                    "Alarm label (optional): "
                ).strip()

                if not label:
                    label = "Alarm"

                clock.add_alarm(alarm_time, label)

            elif command == "list":
                clock.list_alarms()

            elif command == "remove":
                alarm_id = int(
                    input("Alarm ID: ")
                )

                clock.remove_alarm(alarm_id)

            elif command == "help":
                print_help()

            elif command == "exit":
                clock.shutdown()
                print("Goodbye!")
                break

            else:
                print(
                    "Unknown command. Type 'help' for options."
                )

        except KeyboardInterrupt:
            clock.shutdown()
            print("\nGoodbye!")
            break

        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    main()