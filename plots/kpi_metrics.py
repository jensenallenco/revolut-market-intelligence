import pandas as pd

def calculate_top_metrics(df_sector, df_age):
    """Computes internal platform aggregates and periodic adjustments."""
    df_sector = df_sector.sort_values('Date').reset_index(drop=True)
    df_age = df_age.sort_values('Date').reset_index(drop=True)
    
    latest_total = df_sector['Total'].iloc[-1]
    prev_total = df_sector['Total'].iloc[-8] 
    total_delta = ((latest_total - prev_total) / prev_total) * 100
    
    sector_cols = [col for col in df_sector.columns if col not in ['Date', 'Total']]
    recent_sector_means = df_sector[sector_cols].tail(30).mean()
    peak_sector = recent_sector_means.idxmax()
    
    latest_senior = df_age['55+'].iloc[-1]
    latest_young = df_age['18-34'].iloc[-1]
    ratio = latest_senior / latest_young if latest_young != 0 else 0
    
    return {
        "latest_total": f"{latest_total:.1f}",
        "total_delta": f"{total_delta:+.1f}% WoW",
        "peak_sector": str(peak_sector),
        "demographic_ratio": f"{ratio:.2f}x"
    }