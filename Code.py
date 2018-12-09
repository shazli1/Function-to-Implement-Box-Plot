import math
import statistics
import numpy as np
from numpy import percentile
import matplotlib.pyplot as plt

# Get the 1st half of data
def get_lower_half(lst):
    mid_idx = math.floor(len(lst) / 2)
    return(lst[0:mid_idx])

# Get the 2nd half of data
def get_upper_half(lst):
    mid_idx = math.ceil(len(lst) / 2)
    return(lst[mid_idx:])

#######################################
# Function to Calculate Quartiles
#######################################
# Can be used to calculate Q1 & Q3 as below:
# Use the input as the the 1st half of list >>> get Q1
# Use the input as the the 2nd half of list >>> get Q3
def est_quartile(lst):
    lst_cnt = len(lst)
    mid_idx = int(lst_cnt / 2)
    if lst_cnt % 2 != 0:
        return lst[mid_idx]
    return (lst[mid_idx-1] + lst[mid_idx]) / 2


#########################################
# Load data, Convert it to List & Sort it
#########################################
data = np.loadtxt(r'C:\Users\chtv2985\Desktop\Assig-2\Data\Data1.txt')
data_list = data.tolist()
data_sorted = sorted(data_list)


# Get Median using Python Function:
q2 = statistics.median(data_sorted)

q1 = est_quartile(get_lower_half(data_sorted))
q3 = est_quartile(get_upper_half(data_sorted))

iqr = q3 - q1     #inter-quartile range

whisker_b1 = q1 - (1.5 * iqr)
whisker_b2 = q3 + (1.5 * iqr)

extreme_b1 = q1 - (3 * iqr)
extreme_b2 = q3 + (3 * iqr)

outliers = []
extreme_outliers = []
for i in range(len(data_sorted)):
    if extreme_b1 < data_sorted[i] <= whisker_b1:
        outliers.append(data_sorted[i])
    if data_sorted[i] <= extreme_b1:
        extreme_outliers.append(data_sorted[i])
    if whisker_b2 <= data_sorted[i] < extreme_b2:
        outliers.append(data_sorted[i])
    if data_sorted[i] >= extreme_b2:
        extreme_outliers.append(data_sorted[i])

print("Q1: %s" % (q1))
print("Q2: %s" % (q2))
print("Q3: %s" % (q3))
print("Inter-quartile Range: %s" % (float(iqr)))
print("Whisker_1: %s" % (whisker_b1))
print("Whisker_2: %s" % (whisker_b2))
print("Extreme_1: %s" % (extreme_b1))
print("Extreme_2: %s" % (extreme_b2))
print("Outliers: ")
print(outliers)
print("Number of Outliers: %s" % len(outliers))
print("Extreme Outliers:")
print(extreme_outliers)

# box plot for data
plt.figure()
plt.boxplot(data, 0, 'gD', vert=False)
plt.show()

# Copy q1, q2, q3, inter-quartile range into output text file
results = []
labels = np.array(['Q1', 'Q2', 'Q3', 'Inter-quartile Range'])
results.append(q1)
results.append(q2)
results.append(q3)
results.append(iqr)

DAT =  np.column_stack((labels, np.array(results)))

np.savetxt(r'C:\Users\chtv2985\Desktop\Assig-2\Codes\Output-Prob1.txt', DAT, delimiter=" = ", fmt="%s")

# Append outlier points, and extreme outlier points into same output file
with open(r'C:\Users\chtv2985\Desktop\Assig-2\Codes\Output-Prob1.txt', "a") as myfile:
    myfile.write("Outliers = ")
    myfile.write(str(outliers))
    myfile.write("\n")
    myfile.write("Extreme Outliers = ")
    myfile.write(str(extreme_outliers))