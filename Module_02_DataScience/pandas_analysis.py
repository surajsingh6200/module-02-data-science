import pandas as pd

data = {
    "name": [
        "John", "Bob", "Alice", "David", "Emma",
        "Michael", "Sophia", "Daniel", "Olivia", "James"
    ],
    "age": [25, 30, 22, 28, 24, 27, 21, 29, 23, 26]
}

df = pd.DataFrame(data)


df["marks"] = [78, 45, 67, 90, 88, 56, 72, 91, 39, 80]


print("Original DataFrame:\n")
print(df)


mean_marks = df["marks"].mean()

print("\nMean of Marks:", mean_marks)


lowest_5 = df.nsmallest(5, "marks")

print("\nLowest 5 Members:\n")
print(lowest_5)


sorted_df = df.sort_values(by="age")

print("\nSorted DataFrame by Age:\n")
print(sorted_df)