from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.getLogger("matplotlib").setLevel(logging.ERROR)

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
absences = np.full(5, np.nan)


def add_absence(event):
    selected_day = document.getElementById("day").value
    absence_input = document.getElementById("absence").value

    if absence_input.strip() == "":
        document.getElementById("message").innerText = "Please enter the number of absences."
        return

    index = np.where(days == selected_day)[0][0]
    absences[index] = int(absence_input)

    document.getElementById("message").innerText = f"Absences recorded for {selected_day}."
    document.getElementById("absence").value = ""


def show_graph(event):

    if np.all(np.isnan(absences)):
        document.getElementById("message").innerText = "Please enter at least one absence before generating the graph."
        return

    # Clear old graph to prevent spam
    document.getElementById("graph-output").innerHTML = ""
    plt.clf()

    # Replace empty days with 0 so full 5-day graph always shows
    graph_data = np.nan_to_num(absences, nan=0)

    plt.plot(days, graph_data, marker="o")
    plt.title("Section Attendance Tracker")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Absences")
    plt.grid(True)

    display(plt, target="graph-output")

    document.getElementById("message").innerText = "Graph updated successfully."
