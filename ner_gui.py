import tkinter as tk
from tkinter import scrolledtext, messagebox
import pandas as pd
import re

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except ImportError:
    messagebox.showerror("Error", "Spacy not installed. Install with: pip install spacy")
    nlp = None

def run_ner():
    try:
        if nlp is None:
            messagebox.showerror("Error", "Spacy model not loaded. Restart the application.")
            return
        
        df = pd.read_csv("passenger_registration.csv")
        
        if len(df) == 0:
            messagebox.showwarning("No Data", "Please enter travel data first!")
            return
        
        rows = []

        for _, r in df.iterrows():
            text = f"{r.get('Full_Name', '')} travelled to {r.get('Destination_Country', '')}. {r.get('Travel_Feedback', '')}"
            doc = nlp(text)

            for e in doc.ents:
                rows.append([e.text, e.label_])

            if 'Passport_Number' in r and pd.notna(r['Passport_Number']):
                for p in re.findall(r"[A-Z0-9]{6,10}", str(r["Passport_Number"])):
                    rows.append([p, "PASSPORT_NUMBER"])

        if not rows:
            messagebox.showinfo("Info", "No entities found in the data")
            out.delete(1.0, tk.END)
            out.insert(tk.END, "No named entities detected in travel data.")
            return

        ner_df = pd.DataFrame(rows, columns=["Entity", "Type"])

        try:
            ner_df.to_csv("entity_extraction.csv", index=False)
        except:
            pass  # File might be locked, continue anyway

        label_map = {
            "GPE": "LOCATION",
            "PERSON": "PERSON",
            "ORG": "ORGANIZATION",
            "NORP": "NATIONALITY",
            "DATE": "DATE",
            "LOC": "LOCATION",
        }

        out.delete(1.0, tk.END)
        out.insert(tk.END, "━━ NAMED ENTITY RECOGNITION (NER) RESULTS ━━\n\n")
        for e, t in rows:
            display_t = label_map.get(t, t)
            out.insert(tk.END, f"{e} → {display_t}\n")

        messagebox.showinfo("Success", "NER + Regex completed")

    except FileNotFoundError:
        messagebox.showerror("Error", "passenger_registration.csv not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("NER + Regex")
root.geometry("700x500")

tk.Button(root, text="Run NER + Regex", command=run_ner).pack(pady=10)
out = scrolledtext.ScrolledText(root)
out.pack(fill="both", expand=True, padx=10, pady=(0, 10))

root.after(100, run_ner)
root.mainloop()
