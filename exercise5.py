import pandas as pd
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
irisDataset = genfromtxt('IrisNew.csv', delimiter=',', dtype=None, encoding=None)
x = pd.DataFrame(irisDataset[1:, :4])
y = pd.DataFrame(irisDataset[1:, 4]).values.flatten()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Initialize lists to store k values and corresponding accuracy scores
k_values = []
accuracy_scores = []

# Define a range of k values to test
k_range = range(1, 25)  # You can adjust the range as needed

# Loop through different values of k
for k in k_range:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    k_values.append(k)
    accuracy_scores.append(accuracy)

# Plot the accuracy versus k values
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_scores, marker='o', linestyle='-', color='b')
plt.title('Accuracy vs. k Value for k-NN')
plt.xlabel('k Value')
plt.ylabel('Accuracy')
plt.xticks(k_range)
plt.grid()
plt.show()