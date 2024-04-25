from worst_best_case_func import worst_case_prims
import pandas as pd
import matplotlib.pyplot as plt

numnode = 50

worst_avg, index2 = worst_case_prims(numnode)

df = pd.DataFrame({'index': index2, 'worst_avg_time': worst_avg})
plt.plot(df['index'], df['worst_avg_time'], marker='o', linestyle='-', label='worst_case')
plt.title('Time complexity')
plt.xlabel('Vertice')
plt.ylabel('Time')
plt.legend()  # Add legend
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()

