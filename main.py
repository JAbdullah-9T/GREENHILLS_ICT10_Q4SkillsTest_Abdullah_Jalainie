from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.getLogger("matplotlib").setLevel(logging.ERROR)

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
absences = np.full(5, np.nan)   # Start with empty values (not zero)


def add_absence(event):
    selected_day = document.getElementById("day").value
    absence_input = document.getElementById("absence").value

    # Check if input is empty
    if absence_input.strip() == "":
        document.getElementById("message").innerText = "Please enter the number of absences."
        return

    absence_number = int(absence_input)

    index = np.where(days == selected_day)[0][0]
    absences[index] = absence_number

    document.getElementById("message").innerText = f"Absences recorded for {selected_day}."
    document.getElementById("absence").value = ""


def show_graph(event):
    # Check if all values are empty
    if np.all(np.isnan(absences)):
        document.getElementById("message").innerText = "Please enter at least one absence before generating the graph."
        return

    plt.clf()

    plt.plot(days, absences, marker="o")
    plt.title("Section Attendance Tracker")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Absences")
    plt.grid(True)

    display(plt, target="graph-output")
    document.getElementById("message").innerText = ""