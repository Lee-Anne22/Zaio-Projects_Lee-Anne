#Import library
import pandas as py
import matplotlib.pyplot as mat
import seaborn as sb
# Pandas Basic Dataframes
print("Pandas Dataframe and Data Manipulation")

#create a dataframe
data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[23,25,35,40],
    'Subject':['Maths', 'English','Maths','Geography'],
    'Score':[88,98,96,78]
}
df=py.DataFrame(data)
print(df)

data2={
    'Name':['Sarah', 'Amet', 'Candace'],
    'Favourite Color':['Blue', 'Red', 'Purple'],
    'Favourite Food':['Pizza', 'Burgers', 'Ice-Cream']
}
df2=py.DataFrame(data2)
print(df2)

# Filtering Data
print("\nPeople older than 30:")
print(df[df['Age']>30])

#Add a new column
df['Passed']=df['Score']>75
#Telling data to print data in new line via \n
print("\n with new column:")
print(df)

#File Handling with Pandas
#Save to CSV
df.to_csv("Students.csv", index=False)

#Load to csv (case sensitive)
df_loaded=py.read_csv("Students.csv")
print("\n Loaded from CSV:")
print(df_loaded)

#Plotting with Matplotlib

mat.figure(figsize=(6,4))
mat.plot(df['Name'],df['Score'],
marker='o', color='green')
mat.title("Student Scores")
mat.xlabel("Name")
mat.ylabel("Score")
mat.grid(True)
mat.show()

#Plotting for better visual with seaborn (sb)
mat.figure(figsize=(10,8))
sb.barplot(x="Name", y="Score", data=df, palette='coolwarm')
mat.title("Student Scores")
mat.show()