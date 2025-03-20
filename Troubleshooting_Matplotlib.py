import matplotlib
matplotlib.use("QtAgg")  # Alternative: "MacOSX" for native mac backend
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
tips = sns.load_dataset("tips")

# Create a Seaborn plot
sns.histplot(tips["total_bill"], kde=True)

# Show the plot
plt.show()
