from datetime import date, datetime
import ttkbootstrap

root = ttkbootstrap.Window(themename="darkly")
root.title("Age Calculator")
root.geometry("750x500")
root.minsize(380, 280)

header = ttkbootstrap.Label(
    root,
    text="Age Calculator",
    font=("Segoe UI", 20, "bold"),
    bootstyle="primary"
)
header.pack(pady=(20, 8))

clock_label = ttkbootstrap.Label(
    root,
    text="",
    font=("Segoe UI", 10, "bold"),
    bootstyle="secondary"
)
clock_label.pack(pady=(0, 10))

subtext = ttkbootstrap.Label(
    root,
    text="Select your birth date",
    font=("Segoe UI", 10),
    bootstyle="secondary"
)
subtext.pack(pady=(0, 10))

cal = ttkbootstrap.DateEntry(
    root,
    dateformat='%d-%m-%Y',
    bootstyle="info"
)
cal.configure(width=18)
cal.pack(pady=12, padx=40, fill="x")


cal.entry.configure(font=("Segoe UI", 13, "bold"))
cal.button.configure(width=3)

try:
    if hasattr(cal, "popup") and cal.popup is not None:
        cal.popup.geometry("330x330")
        cal.popup.configure(bg="#1f2937")
except Exception:
    pass

btn = ttkbootstrap.Button(
    root,
    text="Calculate Age",
    command=lambda: see_date(),
    bootstyle="success-outline"
)
btn.pack(pady=12, padx=40, fill="x")

result_frame = ttkbootstrap.LabelFrame(
    root,
    text="Result",
    padding=(20, 12),
    bootstyle="info"
)
result_frame.pack(padx=20, pady=(10, 20), fill="x")

date_label = ttkbootstrap.Label(
    result_frame,
    text="No date selected yet",
    font=("Segoe UI", 12, "bold"),
    bootstyle="light",
    wraplength=340
)
date_label.pack(anchor="center")

birthday_label = ttkbootstrap.Label(
    result_frame,
    text="HAPPY BIRTHDAY!",
    font=("Segoe UI", 18, "bold"),
    bootstyle="warning inverse",
    padding=(12, 8)
)


def update_clock():
    now = datetime.now()
    clock_label.config(text=now.strftime("Current time: %I:%M:%S %p"))
    root.after(1000, update_clock)


def calculate_age(born_date):
    today = date.today()

    if born_date > today:
        return "Future date selected"

    years = today.year - born_date.year
    months = today.month - born_date.month
    days = today.day - born_date.day

    if days < 0:
        days += 30
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days


def see_date():
    selected_date = cal.entry.get()

    try:
        birth_date = datetime.strptime(selected_date, "%d-%m-%Y").date()
        result = calculate_age(birth_date)

        if isinstance(result, str):
            date_label.config(text=result, bootstyle="danger")
        else:
            years, months, days = result
            current_time = datetime.now().strftime("%I:%M:%S %p")
            if months == 0 and days == 0:
                date_label.pack_forget()
                birthday_label.pack(anchor="center", pady=(4, 0))
            else:
                birthday_label.pack_forget()
                date_label.pack(anchor="center")
                date_label.config(
                    text=f"You are {years} years, {months} months, and {days} days old\nAs of {current_time}",
                    bootstyle="success"
                )
    except ValueError:
        date_label.config(text="Please select a valid date", bootstyle="danger")


update_clock()
root.mainloop()