import tkinter as tk
from tkinter import scrolledtext, messagebox
import pandas as pd
from textblob import TextBlob
import os
import time

def sentiment(text):
    p = TextBlob(str(text)).sentiment.polarity
    if p > 0: return "Positive"
    if p < 0: return "Negative"
    return "Neutral"

def analyze():
    try:
        df = pd.read_csv("passenger_registration.csv")
        
        if len(df) == 0:
            messagebox.showwarning("No Data", "Please enter travel data first!")
            return
        
        df["Sentiment"] = df["Travel_Feedback"].fillna("").apply(sentiment)
        
        # Try to save CSV with retry
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if os.path.exists("sentiment_analysis.csv"):
                    try:
                        os.remove("sentiment_analysis.csv")
                    except:
                        time.sleep(0.5)
                
                df.to_csv("sentiment_analysis.csv", index=False)
                break
            except PermissionError:
                if attempt < max_retries - 1:
                    time.sleep(0.5)
                else:
                    messagebox.showwarning("File Locked", "Could not save CSV (file locked), but analysis displayed below.")
        
        messagebox.showinfo("Success", "Feedback analysis complete!")

        out.delete(1.0, tk.END)
        out.insert(tk.END, "━━ FEEDBACK SENTIMENT ANALYSIS ━━\n\n")
        
        for idx, (_, r) in enumerate(df.iterrows(), 1):
            feedback = str(r['Travel_Feedback'])[:100] if pd.notna(r['Travel_Feedback']) else "No feedback"
            sentiment_val = r['Sentiment']
            out.insert(tk.END, f"{idx}. Feedback: {feedback}\n   → Sentiment: {sentiment_val}\n\n")
        
        # Summary
        sentiment_counts = df['Sentiment'].value_counts()
        out.insert(tk.END, "\n━━ SUMMARY ━━\n")
        for sentiment_type, count in sentiment_counts.items():
            out.insert(tk.END, f"{sentiment_type}: {count}\n")
            
    except FileNotFoundError:
        messagebox.showerror("Error", "passenger_registration.csv not found! Enter data first.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

root = tk.Tk()
root.title("Feedback Analysis")
root.geometry("700x500")

tk.Button(root, text="Analyze Feedback", command=analyze, font=("Arial", 12, "bold"),
          bg="#27ae60", fg="white", padx=10, pady=8).pack(pady=10)
out = scrolledtext.ScrolledText(root, font=("Arial", 10))
out.pack(fill="both", expand=True, padx=10, pady=(0, 10))

root.after(100, analyze)
root.mainloop()
