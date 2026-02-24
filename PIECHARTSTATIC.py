import matplotlib.pyplot as plt

# Data
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'Go']
usage = [30, 20, 15, 18, 10, 7]  # Example percentage values

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(usage, labels=languages, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Programming Language Usage')

# Show chart
plt.show()
