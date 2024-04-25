from worst_best_case_func import worst_case_prims
from worst_best_case_func import best_case_prims
from worst_best_case_func import avg_case_prims
import pandas as pd
import matplotlib.pyplot as plt

numnode = 50
best_avg, index1 = best_case_prims(numnode)
worst_avg, index2 = worst_case_prims(numnode)
avg_avg, index3 = avg_case_prims(numnode)

df = pd.DataFrame({'index': index1,'best_avg_time': best_avg, 'worst_avg_time': worst_avg, 'avg_time': avg_avg})
plt.plot(df['index'], df['best_avg_time'], marker='o', linestyle='-', label='best_case')
plt.plot(df['index'], df['worst_avg_time'], marker='o', linestyle='-', label='worst_case')
plt.plot(df['index'], df['avg_time'], marker='o', linestyle='-', label='avg_case')
plt.title('Time complexity')
plt.xlabel('Vertice')
plt.ylabel('Time')
plt.legend()  # Add legend
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
