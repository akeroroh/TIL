from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import base64
from collections import Counter


file_path = r"C:\Users\SSAFY\Desktop\austin_weather.csv"

# Create your views here.
def problem1(request):
    df = pd.read_csv(file_path)
    context = {
        'df': df.to_html
    }
    return render(request, 'problem1.html', context)

def problem2(request):
    plt.clf()
    df = pd.read_csv(file_path, usecols=range(0, 4))
    df['Date'] = pd.to_datetime(df['Date'])

    plt.plot(df['Date'], df['TempHighF'], label="High Temperature")
    plt.plot(df['Date'], df['TempAvgF'], label="Average Temperature")
    plt.plot(df['Date'], df['TempLowF'], label="Low Temperature")
    plt.legend()
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }

    return render(request, 'problem2.html', context)

def problem3(request):
    plt.clf()
    df = pd.read_csv(file_path, usecols=range(0, 4))
    df['Date'] = pd.to_datetime(df['Date'])
    df['TempHighF'] = pd.to_numeric(df['TempHighF'])
    df['TempAvgF'] = pd.to_numeric(df['TempAvgF'])
    df['TempLowF'] = pd.to_numeric(df['TempLowF'])

    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df1 = df.groupby(['year', 'month']).mean().reset_index()

    plt.plot(df1['Date'], df1['TempHighF'], label="High Temperature")
    plt.plot(df1['Date'], df1['TempAvgF'], label="Average Temperature")
    plt.plot(df1['Date'], df1['TempLowF'], label="Low Temperature")
    plt.legend()
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }

    return render(request, 'problem3.html', context)


def problem4(request):
    plt.clf()
    df = pd.read_csv(file_path)

    events_counts = Counter()
    for events in df['Events']:
        for event in events.split(','):
            events_counts[event.strip()] += 1

    sorted_events_counts = dict(sorted(events_counts.items(), key=lambda x: x[1], reverse=True))

    x_labels = list(sorted_events_counts.keys())
    x_labels[0] = 'No Events'

    plt.bar(x_labels, sorted_events_counts.values())
    plt.title('Event counts')
    plt.xlabel('Event')
    plt.ylabel('Count')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'image': f'data:image/png;base64, {img_base64}',
    }

    return render(request, 'problem4.html', context)