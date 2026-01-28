import tkinter as tk
from tkinter import scrolledtext
import pandas as pd

keywords = [
    "smooth","delay","security","baggage",
    "slow","quick","helpful","stressful","waiting"
]

def summarize(text):
    text = str(text).lower()
    found = [k for k in keywords if k in text]
    if not found:
        return "General travel experience."
    return "Key points: " + ", ".join(found)

def generate():
    df = pd.read_csv("travel_data.csv")
    df["Summary"] = df["Travel_Feedback"].fillna("").apply(summarize)
    df.to_csv("travel_summary.csv", index=False)

    out.delete(1.0, tk.END)
    for i, r in df.iterrows():
        out.insert(tk.END,
            f"Original:\n{r['Travel_Feedback']}\n"
            f"Summary:\n{r['Summary']}\n\n")

root = tk.Tk()
root.title("Text Summarization")
root.geometry("720x520")

tk.Button(root, text="Generate Summary", command=generate).pack(pady=10)
out = scrolledtext.ScrolledText(root, width=85, height=25)
out.pack()

root.mainloop()
