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
    """Generates direct text observations based on the active sector filters."""
    if not selected_sectors:
        return "No categories selected for statistical evaluation."
        
    df_recent = df_sector.sort_values('Date').tail(365) # Look at the trailing year
    insights = []
    
    for sector in selected_sectors:
        latest_val = df_recent[sector].iloc[-1]
        min_val = df_recent[sector].min()
        max_val = df_recent[sector].max()
        
        # Calculate volatility (Spread between max and min index points)
        volatility = max_val - min_val
        
        if volatility > 40:
            status = "high seasonal volatility"
        else:
            status = "stable baseline consumer demand"
            
    return f"The selected categories track a variance span of {volatility:.1f} index points over the trailing 12 months, indicating a pattern of {status} across the UK market grid."
