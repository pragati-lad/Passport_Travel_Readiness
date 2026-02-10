import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    df = pd.read_csv("passenger_registration.csv")
    
    if len(df) == 0:
        print("No data found. Please enter travel data first!")
        exit()
    
    # Data preprocessing
    df['Group_Size'] = pd.to_numeric(df['Group_Size'], errors='coerce').fillna(1).astype(int)
    df['Children_Count'] = pd.to_numeric(df['Children_Count'], errors='coerce').fillna(0).astype(int)
    df['Elderly_Count'] = pd.to_numeric(df['Elderly_Count'], errors='coerce').fillna(0).astype(int)
    df['Number_of_Bags'] = pd.to_numeric(df['Number_of_Bags'], errors='coerce').fillna(0).astype(int)
    df['First_Time_Traveler'] = df['First_Time_Traveler'].fillna('No')
    df['Accessibility_Needs'] = df['Accessibility_Needs'].fillna('None')
    
    # Create 2x2 subplot grid
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("Visualization", fontsize=20, fontweight='bold', y=0.99)
    
    # PLOT 1: TRAVELER COMPOSITION
    solo = len(df[df["Group_Size"] == 1])
    family = len(df[df["Children_Count"] > 0])
    elderly = len(df[df["Elderly_Count"] > 0])
    
    colors1 = ["#3498db", "#e74c3c", "#f39c12"]
    ax1.pie(
        [solo, family, elderly],
        labels=["Solo Travelers", "Families with Children", "Groups with Elderly"],
        autopct="%1.1f%%",
        colors=colors1,
        startangle=90,
        textprops={'fontsize': 9, 'weight': 'bold'}
    )
    ax1.set_title("Traveler Composition", fontsize=12, fontweight='bold', pad=10)
    
    # PLOT 2: GROUP SIZE vs BAGS
    ax2.scatter(df["Group_Size"], df["Number_of_Bags"], s=80, alpha=0.6, color='#9b59b6', edgecolors='black', linewidth=1.5)
    ax2.set_xlabel("Group Size", fontsize=10, fontweight='bold')
    ax2.set_ylabel("Number of Bags", fontsize=10, fontweight='bold')
    ax2.set_title("Group Size vs Baggage Load", fontsize=12, fontweight='bold', pad=10)
    ax2.set_xticks(sorted(df["Group_Size"].unique()))
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # PLOT 3: FIRST-TIME vs EXPERIENCED TRAVELERS
    counts = df["First_Time_Traveler"].value_counts()
    colors3 = ['#3498db', '#e67e22'][:len(counts)]
    counts.plot(kind="bar", ax=ax3, color=colors3, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax3.set_xlabel("Traveler Type", fontsize=10, fontweight='bold')
    ax3.set_ylabel("Number of Passengers", fontsize=10, fontweight='bold')
    ax3.set_title("First-Time vs Experienced Travelers", fontsize=12, fontweight='bold', pad=10)
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=0, ha='center', fontsize=9)
    ax3.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # PLOT 4: ACCESSIBILITY NEEDS
    access = df["Accessibility_Needs"].value_counts().head(8)
    ax4.barh(range(len(access)), access.values, color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    ax4.set_yticks(range(len(access)))
    ax4.set_yticklabels(access.index, fontsize=9)
    ax4.set_xlabel("Number of Passengers", fontsize=10, fontweight='bold')
    ax4.set_title("Top Accessibility Needs", fontsize=12, fontweight='bold', pad=10)
    ax4.grid(True, alpha=0.3, axis='x', linestyle='--')
    
    # Adjust spacing to prevent label overlap
    plt.subplots_adjust(top=0.94, bottom=0.08, left=0.08, right=0.96, hspace=0.35, wspace=0.3)
    
    # Remove toolbar for cleaner look
    mng = plt.get_current_fig_manager()
    if hasattr(mng, 'toolbar'):
        mng.toolbar.pack_forget()
    
    plt.show()
        
except FileNotFoundError:
    print("Error: passenger_registration.csv not found!")
except Exception as e:
    print(f"Error: {str(e)}")
