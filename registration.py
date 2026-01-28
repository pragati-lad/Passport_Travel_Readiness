import tkinter as tk
from tkinter import messagebox, ttk
import csv, os

FILE = "travel_data.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            "Full_Name","Passport_Number","Date_of_Birth","Destination_Country",
            "Travel_Purpose","Group_Size","Number_of_Bags",
            "Children_Count","Elderly_Count",
            "Accessibility_Needs","Medical_Conditions","Dietary_Requirements",
            "Language_Preference","First_Time_Traveler","Emergency_Contact",
            "Travel_Insurance","Vaccination_Status","Travel_Feedback"
        ])

def submit():
    row = [
        name.get(), passport.get(), dob.get(), dest.get(), purpose.get(),
        group.get(), bags.get(), children.get(), elderly.get(),
        accessibility.get(), medical.get(), dietary.get(),
        language.get(), first_time.get(), emergency.get(),
        insurance.get(), vaccination.get(),
        feedback.get("1.0", tk.END).strip()
    ]
    if not row[0] or not row[1]:
        messagebox.showerror("Error", "Name & Passport required")
        return

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(row)

    messagebox.showinfo("Saved", "Data saved successfully")
    
    # Clear fields
    name.delete(0, tk.END)
    passport.delete(0, tk.END)
    dob.delete(0, tk.END)
    dest.delete(0, tk.END)
    group.delete(0, tk.END)
    bags.delete(0, tk.END)
    children.delete(0, tk.END)
    elderly.delete(0, tk.END)
    medical.delete(0, tk.END)
    dietary.delete(0, tk.END)
    emergency.delete(0, tk.END)
    feedback.delete("1.0", tk.END)

root = tk.Tk()
root.title("Passport Travel Readiness - Inclusive Entry Form")
root.geometry("600x850")

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollframe = tk.Frame(canvas)

scrollframe.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollframe, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tk.Label(scrollframe, text="Passport Travel Readiness System", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(scrollframe, text="Inclusive Travel Information", font=("Arial", 10, "italic"), fg="gray").pack()

def lbl(t): tk.Label(scrollframe, text=t, anchor="w").pack(fill="x", padx=10)
def ent():
    e = tk.Entry(scrollframe, width=40)
    e.pack(padx=10, pady=3)
    return e

# Personal Information
tk.Label(scrollframe, text="━━ PERSONAL INFORMATION ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)
lbl("Full Name *"); name = ent()
lbl("Passport Number *"); passport = ent()
lbl("Date of Birth"); dob = ent()

# Destination
tk.Label(scrollframe, text="━━ TRAVEL DETAILS ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)
lbl("Destination Country"); dest = ent()

lbl("Travel Purpose")
purpose = tk.StringVar(value="Tourism")
ttk.Combobox(scrollframe, textvariable=purpose,
             values=["Tourism","Business","Education","Work","Visit Family"],
             width=37).pack(padx=10, pady=3)

lbl("Group Size"); group = ent()
lbl("Number of Bags"); bags = ent()

# Family Info
tk.Label(scrollframe, text="━━ GROUP COMPOSITION ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)
lbl("Children Count"); children = ent()
lbl("Elderly Count"); elderly = ent()

# Inclusive & Accessibility
tk.Label(scrollframe, text="━━ ACCESSIBILITY & HEALTH ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)

lbl("Accessibility Needs (Wheelchair, Mobility Aid, Visual/Hearing Impairment, etc.)")
accessibility = ent()

lbl("Medical Conditions (if any)")
medical = ent()

lbl("Dietary Requirements (Vegetarian, Vegan, Halal, Kosher, Allergies, etc.)")
dietary = ent()

lbl("Language Preference")
language = tk.StringVar(value="English")
ttk.Combobox(scrollframe, textvariable=language,
             values=["English","Spanish","French","Mandarin","Hindi","Arabic","Other"],
             width=37).pack(padx=10, pady=3)

# Travel Experience
tk.Label(scrollframe, text="━━ TRAVEL EXPERIENCE ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)

lbl("First Time Traveler?")
first_time = tk.StringVar(value="No")
ttk.Combobox(scrollframe, textvariable=first_time,
             values=["Yes","No"],
             width=37).pack(padx=10, pady=3)

# Important Info
tk.Label(scrollframe, text="━━ IMPORTANT INFO ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)

lbl("Emergency Contact (Name & Phone)")
emergency = ent()

lbl("Travel Insurance?")
insurance = tk.StringVar(value="No")
ttk.Combobox(scrollframe, textvariable=insurance,
             values=["Yes","No"],
             width=37).pack(padx=10, pady=3)

lbl("Vaccination Status")
vaccination = tk.StringVar(value="Complete")
ttk.Combobox(scrollframe, textvariable=vaccination,
             values=["Complete","Partial","Not Vaccinated","Prefer Not to Say"],
             width=37).pack(padx=10, pady=3)

# Feedback
tk.Label(scrollframe, text="━━ ADDITIONAL FEEDBACK ━━", font=("Arial", 11, "bold"), fg="#2c3e50").pack(fill="x", padx=10, pady=8)
lbl("Travel Feedback/Comments")
feedback = tk.Text(scrollframe, height=4, width=40)
feedback.pack(padx=10, pady=3)

# Submit Button
tk.Button(scrollframe, text="Submit", bg="#27ae60", fg="white",
          width=40, font=("Arial", 12, "bold"), command=submit).pack(pady=15)

root.mainloop()
