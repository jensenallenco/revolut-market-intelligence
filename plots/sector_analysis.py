import matplotlib.pyplot as plt

def render_sector_chart(df_sector, selected_sectors):
    """Generates a line chart tracking consumer spending indices by category."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Modern dark minimalist layout matching your established dashboard style
    fig.patch.set_facecolor('#0f121d')  
    ax.set_facecolor('#181c2a')         
    ax.tick_params(colors='#848e9c', labelsize=10) 
    ax.xaxis.label.set_color('#848e9c')
    ax.yaxis.label.set_color('#848e9c')
    ax.grid(True, color='#222838', linestyle='-', linewidth=0.8) 
    
    # Simple, high-contrast palette
    colors_list = ['#ffffff', '#0075ff', '#00f0b5', '#ff467e', '#ffb020', '#9053ff']
    
    for i, sector in enumerate(selected_sectors):
        color = colors_list[i % len(colors_list)]
        ax.plot(df_sector['Date'], df_sector[sector], label=sector, linewidth=1.8, color=color)
        
    ax.set_ylabel("Spending Index (Base 100 = 2023 Average)", fontsize=10, color='#848e9c')
    ax.legend(frameon=True, facecolor='#0f121d', edgecolor='none', labelcolor='white', loc='upper left', fontsize=9)
    
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.tight_layout()
    return fig

def get_sector_insights(df_sector, selected_sectors):
    """Generates a direct, clean observation of category trends using standard statistical terms."""
    if not selected_sectors:
        return "No categories selected for statistical evaluation."
        
    df_recent = df_sector.sort_values('Date').tail(365) # Trailing 12 months
    
    # Calculate the max-min range of the index over the past year
    recent_maxs = df_recent[selected_sectors].max()
    recent_mins = df_recent[selected_sectors].min()
    max_range = (recent_maxs - recent_mins).max()
    
    movement_type = "notable seasonal movement" if max_range > 40 else "stable baseline movement"
            
    return f"The selected categories show a {max_range:.1f}-point range in the spending index over the past 12 months, suggesting {movement_type} in UK debit card spending."
