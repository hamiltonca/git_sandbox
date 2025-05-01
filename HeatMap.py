# copy/pasted from a Gemini session I had 
# 2025-04-30 16:00 ET

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data (replace with the actual table)
data = {'Word': ['Controversial', 'Outspoken', 'Divisive', 'Unpredictable', 'Strong', 'Nationalist', 'Populist', 'Narcissistic', 'Inflammatory', 'Authoritarian', 'Businessman', 'Polarizing', 'Egotistical', 'Charismatic', 'False', 'Negative', 'Simple', 'Violent'],
        'Simulated Count': [78900000, 15800000, 25900000, 18000000, 22000000, 9000000, 11000000, 14000000, 12500000, 7500000, 28000000, 20000000, 10000000, 6000000, 5000000, 35000000, 4000000, 2500000]}
df = pd.DataFrame(data)
df_pivot = df.pivot_table(index='Word', values='Simulated Count')

sns.heatmap(df_pivot, annot=True, fmt=".1e", cmap="viridis") # annot=True shows values, fmt formats them, cmap sets the color scheme
plt.title('Heat Map of Words Describing a politician (Simulated Data)')
plt.show()
