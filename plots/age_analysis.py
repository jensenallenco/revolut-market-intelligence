import matplotlib.pyplot as plt

def render_age_chart(df_age, selected_ages):
    """Generates a line chart tracking consumer spending indices by age demographic."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    fig.patch.set_facecolor('#0f121d')
    ax.set_facecolor('#181c2a')
    ax.tick_params(colors='#848e9c', labelsize=10)
    ax.xaxis.label.set_color('#848e9c')
    ax.yaxis.label.set_color('#848e9c')
    ax.grid(True, color='#222838', linestyle='-', linewidth=0.8)
    
    age_colors = {
        "18-34": "#00d4ff",  
        "35-54": "#ff007f",  
        "55+": "#7b2cbf"     
    }
    
    for age in selected_ages:
        if age in df_age.columns:
            ax.plot(df_age['Date'], df_age[age], label=f"Age {age}", color=age_colors.get(age, '#ffffff'), linewidth=1.8)
        
    ax.set_ylabel("Spending Index (Base 100 = 2023 Average)", fontsize=10, color='#848e9c')
    ax.legend(frameon=True, facecolor='#0f121d', edgecolor='none', labelcolor='white', loc='upper left', fontsize=9)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.tight_layout()
    return fig


def get_age_insights(df_age, selected_ages):
    """Generates a direct observation of age demographic trends without artificial tech jargon."""
    if not selected_ages:
        return "No age groups selected for statistical evaluation."
        
    df_sorted = df_age.sort_values('Date')
    latest_entries = df_sorted.iloc[-1]
    
    active_scores = {age: latest_entries[age] for age in selected_ages if age in latest_entries}
    
    if not active_scores:
        return "Insufficient data for active age groups."
        
    leading_age = max(active_scores, key=active_scores.get)
    leading_val = active_scores[leading_age]
    
    return f"Among the selected age groups, the {leading_age} group has the highest latest spending index, reaching {leading_val:.1f} in the most recent period."
