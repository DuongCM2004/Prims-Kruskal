import pandas as pd
import matplotlib.pyplot as plt
from worst_best_case_func import best_case_prims
numnode = 50
best_avg, index1 = best_case_prims(numnode)

df = pd.DataFrame({'index': index1,'best_avg_time': best_avg})
plt.plot(df['index'], df['best_avg_time'], marker='o', linestyle='-', label='best_case')
plt.title('Time complexity')
plt.xlabel('Vertice')
plt.ylabel('Time')
plt.legend()  # Add legend
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()