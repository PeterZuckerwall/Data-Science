import pandas as pd
import bar_chart_race as bcr

# Read CSV into a pandas DataFrame.
df = pd.read_csv('data.csv', index_col='Year')

# Format the index to ensure proper year display
df.index = df.index.map(lambda y: f"{y:04d}")  # Ensure years are 4 digits

# Create the bar chart race animation with adjusted period formatting.
bcr.bar_chart_race(
    df=df,
    filename='Bar_Chart_Race.mp4',
    orientation='h',
    sort='desc',       # highest numbers at the top
    n_bars=10,         # show top 10
    fixed_order=False, # bars can change order dynamically
    title='Animated TV Series in America by Viewership (1999-2024)',
    bar_size=.95,
    period_fmt='{x}',  # Use a placeholder for custom formatting
    steps_per_period=250,  # Increase for smoother transitions
    period_length=12000,   # 4 seconds per period
    figsize=(8, 4.5),
    dpi=144,
    cmap='tab10'       # different colors for each bar
)