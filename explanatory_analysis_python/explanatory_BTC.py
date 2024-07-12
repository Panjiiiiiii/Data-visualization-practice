import matplotlib.pyplot as plt
import seaborn as sns
import  pandas as pd
import os

download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, "BTC-USD.csv")
df = pd.read_csv(file_path, delimiter=",")
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Close'], label='Close', color='Red')
plt.plot(df['Date'], df['Open'], label='Open', color='Blue')
plt.title('BTC-USD price', size=20)
plt.xlabel('Date', size=15)
plt.ylabel('Price (USD)', size=15)
plt.legend()
plt.show()