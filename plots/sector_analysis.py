import matplotlib.pyplot as plt

def render_sector_chart(df_sector, selected_sectors):
    """Generates an executive line chart using Revolut's dark interface colorway."""
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Revolut Dark Palette Map
    fig.patch.set_facecolor('#0f121d')  # Deep Revolut Slate Core
    ax.set_facecolor('#181c2a')         # Lighter Component Card Surface
    ax.tick_params(colors='#848e9c', labelsize=10) # Minimalist muted gray text
    ax.xaxis.label.set_color('#848e9c')
    ax.yaxis.label.set_color('#848e9c')
    ax.grid(True, color='#222838', linestyle='-', linewidth=0.8) # Subtle gridlines
    
    # Clean minimalist color rotation for various sectors
    brand_colors = ['#ffffff', '#0075ff', '#00f0b5', '#ff467e', '#ffb020', '#9053ff']
    
    for i, sector in enumerate(selected_sectors):
        color = brand_colors[i % len(brand_colors)]
        ax.plot(df_sector['Date'], df_sector[sector], label=sector, linewidth=1.8, color=color)
        
    ax.set_ylabel("Index Score (Base 100 = 2023 Average)", fontsize=10, fontweight='bold', color='#848e9c')
    ax.legend(frameon=True, facecolor='#0f121d', edgecolor='none', labelcolor='white', loc='upper left', fontsize=9)
    
    # Remove chart borders for a cleaner look
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.tight_layout()
    return fig