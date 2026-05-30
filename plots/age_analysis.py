import matplotlib.pyplot as plt

def render_age_chart(df_age, selected_ages):
    """Generates a demographic line chart mapped to Revolut Tier colorways."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    fig.patch.set_facecolor('#0f121d')
    ax.set_facecolor('#181c2a')
    ax.tick_params(colors='#848e9c', labelsize=10)
    ax.xaxis.label.set_color('#848e9c')
    ax.yaxis.label.set_color('#848e9c')
    ax.grid(True, color='#222838', linestyle='-', linewidth=0.8)
    
    # Revolut Product Brand Architecture Colors
    tier_colors = {
        "18-34": "#00d4ff",  # Revolut Standard Electric Blue
        "35-54": "#ff007f",  # Revolut Premium Pink
        "55+": "#7b2cbf"     # Revolut Ultra Obsidian Purple
    }
    
    for age in selected_ages:
        if age in df_age.columns:
            ax.plot(df_age['Date'], df_age[age], label=f"Age {age}", color=tier_colors.get(age, '#ffffff'), linewidth=1.8)
        
    ax.set_ylabel("Index Score (Base 100 = 2023 Average)", fontsize=10, fontweight='bold', color='#848e9c')
    ax.legend(frameon=True, facecolor='#0f121d', edgecolor='none', labelcolor='white', loc='upper left', fontsize=9)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.tight_layout()
    return fig