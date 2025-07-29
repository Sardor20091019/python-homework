import pandas as pd
df = pd.read_csv(r"D:\python\stackoverflow_qa.csv")
df.head()
#1
df['creationdate'] = pd.to_datetime(df['creationdate'])
questions_before_2014 = df[df['creationdate'] < '2014-01-01']
#2
questions_score_gt_50 = df[df['Score'] > 50]
#3
questions_score_50_100 = df[(df['Score'] >= 50) & (df['Score'] <= 100)]
#4 
questions_by_scott = df[df['Answerer'] == 'Scott Boston']
#5
users = ['User1', 'User2', 'User3', 'User4', 'User5']
questions_by_users = df[df['Answerer'].isin(users)]
#6
questions_unutbu = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['Answerer'] == 'Unutbu') &
    (df['Score'] < 5)
]
#7
questions_score_or_views = df[
    ((df['Score'] >= 5) & (df['Score'] <= 10)) |
    (df['ViewCount'] > 10000)
]
#8
questions_not_scott = df[df['Answerer'] != 'Scott Boston']




















import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("path/to/titanic.csv")

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Fare'].fillna(df['Fare'].median(), inplace=True)
df.drop(columns=['Cabin'], inplace=True)

survival_counts = df['Survived'].value_counts()
survival_rate = df['Survived'].value_counts(normalize=True) * 100
survival_by_gender = df.groupby('Sex')['Survived'].value_counts(normalize=True).unstack() * 100
avg_fare_by_class = df.groupby('Pclass')['Fare'].mean()
survival_by_class = df.groupby('Pclass')['Survived'].value_counts(normalize=True).unstack() * 100
embarked_counts = df['Embarked'].value_counts()

df['Age'].hist(bins=30)
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.title('Age Distribution')
plt.show()












# 1. Female Passengers in Class 1 with Ages between 20 and 30
female_class1_age20_30 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Age'].between(20, 30))]

# 2. Passengers Who Paid More than $100
fare_over_100 = df[df['Fare'] > 100]

# 3. Passengers Who Survived and Were Alone
survived_alone = df[(df['Survived'] == 1) & (df['SibSp'] == 0) & (df['Parch'] == 0)]

# 4. Passengers Embarked from 'C' and Paid More Than $50
embarked_c_fare_over_50 = df[(df['Embarked'] == 'C') & (df['Fare'] > 50)]

# 5. Passengers with Siblings or Spouses and Parents or Children
family_both = df[(df['SibSp'] > 0) & (df['Parch'] > 0)]

# 6. Passengers Aged 15 or Younger Who Didn't Survive
child_not_survived = df[(df['Age'] <= 15) & (df['Survived'] == 0)]

# 7. Passengers with Cabins and Fare Greater Than $200
df_with_cabin = pd.read_csv("path/to/titanic.csv")  # Reload original with 'Cabin' if it was dropped earlier
with_cabin_fare_over_200 = df_with_cabin[df_with_cabin['Fare'] > 200].dropna(subset=['Cabin'])

# 8. Passengers with Odd-Numbered Passenger IDs
odd_passenger_ids = df[df['PassengerId'] % 2 == 1]

# 9. Passengers with Unique Ticket Numbers
unique_ticket_df = df[df['Ticket'].duplicated(keep=False) == False]

# 10. Passengers with 'Miss' in Their Name and Were in Class 1
miss_class1 = df[(df['Name'].str.contains('Miss')) & (df['Pclass'] == 1)]
