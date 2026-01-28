import tkinter as tk
import subprocess
import sys

def run(file):
    subprocess.Popen([sys.executable, file])

root = tk.Tk()
root.title("Passport Travel Readiness System")
root.geometry("500x520")
root.resizable(False, False)

tk.Label(
    root,
    text="Passport Travel Readiness\nData Science Case Study",
    font=("Arial", 18, "bold"),
    pady=20
).pack()

btn = {"font": ("Arial", 12), "width": 30, "height": 2}

tk.Button(root, text="Passenger Entry",
          command=lambda: run("registration.py"), **btn).pack(pady=6)

tk.Button(root, text="Feedback Insights",
          command=lambda: run("feedback_gui.py"), **btn).pack(pady=6)

tk.Button(root, text="Text Summarization",
          command=lambda: run("summary_gui.py"), **btn).pack(pady=6)

tk.Button(root, text="Entity Extraction (NER)",
          command=lambda: run("ner_gui.py"), **btn).pack(pady=6)

tk.Button(root, text="Visual Insights",
          command=lambda: run("plot_gui.py"), **btn).pack(pady=6)

tk.Button(root, text="Exit", bg="red", fg="white",
          command=root.destroy, **btn).pack(pady=20)

root.mainloop()
