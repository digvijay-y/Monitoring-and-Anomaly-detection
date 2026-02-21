import pandas as pd
import matplotlib.pyplot as plt

# Read datasets
df_original = pd.read_csv('prmon_normal.txt', sep=r'\s+')
df_modified = pd.read_csv('prmon_normal_2.txt', sep=r'\s+')

df_original['label'] = 'normal'
df_modified['label'] = 'anomaly'

# Combine 
df = pd.concat([df_original,df_modified], ignore_index=True)


# Calculate Z-Score
df['z_score'] = (df['nthreads'] - df['nthreads'].mean()) / df['nthreads'].std()


threshold = 0.5
df['anomaly'] = df['z_score'] > threshold

# Plot 
plt.plot(df.index, df['nthreads'], label='nthreads', color='blue')
plt.scatter(df[df['anomaly']].index, df[df['anomaly']]['nthreads'], 
            color='red', label='anomaly flagged', zorder=5)
plt.title("Anomaly Detection using Z-Score")
plt.xlabel("Time (index)")
plt.ylabel("nthreads")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#Anomaly comparision
print(df['anomaly'].sum())  # total flagged
print(df[df['anomaly']]['label'].value_counts())