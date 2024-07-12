import matplotlib.pyplot as plt
import seaborn as sns
import  pandas as pd
import os

human_height = [170.3, 168.7, 186.5, 190.5]
human_weight = [68.5, 63.4, 78.8, 85.3]

plt.plot(human_height, human_weight)
plt.show()

#BTC-USD price
download_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(download_folder, "BTC-USD.csv")
df = pd.read_csv(file_path, delimiter=",")
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Close'], color='red')
plt.title("BTC-USD")
plt.xlabel('Date', size=15)
plt.ylabel('Price', size=15)
plt.show()