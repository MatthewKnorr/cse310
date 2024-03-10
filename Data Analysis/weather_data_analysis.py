import pandas as pd
import matplotlib.pyplot as plt
import mplcursors  

def display_analysis_info(ax):
    min_temp_avg = weather_data['MinTemp'].mean() * 9/5 + 32
    max_temp_avg = weather_data['MaxTemp'].mean() * 9/5 + 32
    daily_temp_avg = ((weather_data['MinTemp'] * 9/5) + 32 + (weather_data['MaxTemp'] * 9/5) + 32) / 2
    rainfall_avg = weather_data['Rainfall'].mean()
    wind_gust_avg = weather_data['WindGustSpeed'].mean() * 0.621371
    humidity_avg = weather_data['Humidity3pm'].mean()
    pressure_avg = weather_data['Pressure3pm'].mean() * 0.0145038

    analysis_info = [
        f'Average Min Temperature: {min_temp_avg:.2f}°F',
        f'Average Max Temperature: {max_temp_avg:.2f}°F',
        f'Average Daily Temperature: {daily_temp_avg.median():.2f}°F',
        f'Average Rainfall: {rainfall_avg:.2f} mm',
        f'Average Wind Gust: {wind_gust_avg:.2f} mph',
        f'Average Humidity: {humidity_avg:.2f}%',
        f'Average Pressure: {pressure_avg:.2f} psi'
    ]

    for i, info in enumerate(analysis_info):
        ax.text(1.05, 0.95 - i * 0.05, info, fontsize=10, verticalalignment='top', transform=ax.transAxes)

weather_data = pd.read_csv('weather.csv')
total_days_recorded = len(weather_data)

variables_to_plot = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'Humidity3pm']

fig, ax = plt.subplots(figsize=(15, 9))  

for variable in variables_to_plot:
    ax.plot(weather_data.index, weather_data[variable], marker='o', linestyle='solid', label=variable, markersize=5)

ax.set_title('Weather Variables Over Time')
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Value', fontsize=12)

ax.set_xticks(range(0, total_days_recorded, 50))
ax.set_yticks(range(-15, 105, 15))

ax.grid(True)
ax.legend()

mplcursors.cursor(hover=True)

display_analysis_info(ax)

plt.tight_layout()
plt.show()
