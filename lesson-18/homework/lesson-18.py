Homework 2:

import pandas as pd

1. Find all questions that were created before 2014

tack['creationdate'] = pd.to_datetime(tack['creationdate'])
tack[tack['creationdate'].dt.year<2014]


2. Find all questions with a score more than 50

# Score 50 dan katta bo'lgan savollarni ajratib olish
questions_high_score = df[df['score'] > 50]

# Natijani chiqarish
print(questions_high_score)


3. Find all questions with a score between 50 and 100

# Avval, score ustunini raqamga o'tkazamiz, agar hali o'tkazilmagan bo‘lsa
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# 50 dan katta va 100 dan kichik bo‘lgan score'lar
filtered = df[(df['score'] > 50) & (df['score'] < 100)]

print(filtered)



4. Find all questions answered by Scott Boston

# "ans_name" ustunida Scott Boston bo'lgan qatorlarni filtrlash
scott_questions = df[df['ans_name'] == 'Scott Boston']

print(scott_questions)


5. Find all questions answered by the following 5 users

import pandas as pd

# Faraz qilamiz, df bu sizning DataFrame
users = ['Scott Boston', 'unutbu', 'DSM', 'Mike Pennington', 'Jubbles']

# Foydalanuvchilar tomonidan javob berilgan savollar
answered_by_users = df[df['ans_name'].isin(users)]

# Natijani chiqarish
print(answered_by_users)


6. Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

import pandas as pd

# Sana ustunini datetime formatga o'tkazamiz (agar hali o'tkazilmagan bo'lsa)
df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')

# 'ans_name' ustunidagi NaN qiymatlarni bo'sh qator bilan to'ldiramiz va kichik harflarga o'tkazamiz
df['ans_name'] = df['ans_name'].fillna('').str.lower()

# Filtrlash shartlari
filtered = df[
    (df['score'] < 5) &
    (df['ans_name'] == 'unutbu') &  # kichik harflarda tekshiriladi
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31')
]

print(filtered)


7. Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

# Avval raqam ustunlarini to'g'rilab olamiz (agar kerak bo'lsa)
df['score'] = pd.to_numeric(df['score'], errors='coerce')
df['viewcount'] = pd.to_numeric(df['viewcount'], errors='coerce')

# Shartlar
score_filter = (df['score'] >= 5) & (df['score'] <= 10)
view_filter = df['viewcount'] > 10000

# OR bilan birlashtiramiz
final_filter = score_filter | view_filter

# Natijani ajratib olamiz
result = df[final_filter]

print(result)



8. Find all questions that are not answered by Scott Boston

# Scott Boston tomonidan javob berilmagan savollar
not_by_scott = df[df['ans_name'] != 'Scott Boston']

print(not_by_scott)

Homework 3:

Titanic data set, stored as CSV. The data consists of the following data columns:

- PassengerId: Id of every passenger.
- Survived: Indication whether passenger survived. 0 for yes and 1 for no.
- Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
- Name: Name of passenger.
- Sex: Gender of passenger.
- Age: Age of passenger in years.
- SibSp: Number of siblings or spouses aboard.
- Parch: Number of parents or children aboard.
- Ticket: Ticket number of passenger.
- Fare: Indicating the fare.
- Cabin: Cabin number of passenger.
- Embarked: Port of embarkation.

```
titanic_df = pd.read_csv("task\\titanic.csv")
titanic_df.head()
```

| PassengerId | Survived | Pclass | Name                                             | Sex    | Age   | SibSp | Parch | Ticket           | Fare    | Cabin | Embarked |
|-------------|----------|--------|--------------------------------------------------|--------|-------|-------|-------|------------------|---------|-------|----------|
| 1           | 0        | 3      | Braund, Mr. Owen Harris                         | male   | 22.0  | 1     | 0     | A/5 21171        | 7.2500  | NaN   | S        |
| 2           | 1        | 1      | Cumings, Mrs. John Bradley (Florence Briggs Th.) | female | 38.0  | 1     | 0     | PC 17599         | 71.2833 | C85   | C        |
| 3           | 1        | 3      | Heikkinen, Miss. Laina                          | female | 26.0  | 0     | 0     | STON/O2. 3101282 | 7.9250  | NaN   | S        |
| 4           | 1        | 1      | Futrelle, Mrs. Jacques Heath (Lily May Peel)    | female | 35.0  | 1     | 0     | 113803           | 53.1000 | C123  | S        |
| 5           | 0        | 3      | Allen, Mr. William Henry                        | male   | 35.0  | 0     | 0     | 373450           | 8.0500  | NaN   | S        |


1. Select Female Passengers in Class 1 with Ages between 20 and 30:
Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

# Female passengers in Class 1 with ages between 20 and 30
female_class1_20_30 = titanic[
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1) &
    (titanic['Age'] >= 20) &
    (titanic['Age'] <= 30)
]

female_class1_20_30.head()  # Natijani ko‘rish uchun


2. Filter Passengers Who Paid More than $100:
Create a DataFrame with passengers who paid a fare greater than $100.

# Passengers who paid more than $100
paid_more_than_100 = titanic[titanic['Fare'] > 100]

paid_more_than_100.head()  # Natijani ko‘rish uchun


3. Select Passengers Who Survived and Were Alone:
Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

# Passengers who survived (Survived == 0) and were alone (SibSp == 0 and Parch == 0)
survived_alone = titanic_df[
    (titanic['Survived'] == 1) &
    (titanic['SibSp'] == 0) &
    (titanic['Parch'] == 0)
]

survived_alone.head()


4. Filter Passengers Embarked from 'C' and Paid More Than $50:
Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

# Passengers embarked from 'C' and paid more than $50
embarked_C_paid_over_50 = titanic[
    (titanic['Embarked'] == 'C') &
    (titanic['Fare'] > 50)
]

embarked_C_paid_over_50.head()



5. Select Passengers with Siblings or Spouses and Parents or Children:
Extract passengers who had both siblings or spouses aboard and parents or children aboard.

# Passengers who had both siblings/spouses and parents/children aboard
with_family = titanic[
    (titanic['SibSp'] > 0) &
    (titanic['Parch'] > 0)]

with_family.head()



6. Filter Passengers Aged 15 or Younger Who Didn't Survive:
Create a DataFrame with passengers aged 15 or younger who did not survive.

# Passengers aged 15 or younger who did not survive (Survived == 1)
young_not_survived = titanic[
    (titanic['Age'] <= 15) &
    (titanic['Survived'] == 0)]

young_not_survived.head()



7. Select Passengers with Cabins and Fare Greater Than $200:
Extract passengers with known cabin numbers and a fare greater than $200.

# Passengers with known cabins (non-null) and fare greater than $200
cabins_fare_over_200 = titanic[
    titanic['Cabin'].notna() & 
    (titanic['Fare'] > 200)
]

cabins_fare_over_200.head()


8. Filter Passengers with Odd-Numbered Passenger IDs:
Create a DataFrame with passengers whose PassengerId is an odd number.

# Passengers with odd-numbered PassengerId
odd_passenger_ids = titanic[titanic['PassengerId'] % 2 == 1]

odd_passenger_ids.head()


9. Select Passengers with Unique Ticket Numbers:
Extract a DataFrame with passengers having unique ticket numbers.

# Find ticket numbers that appear only once
unique_tickets = titanic['Ticket'].value_counts()
unique_ticket_numbers = unique_tickets[unique_tickets == 1].index

# Filter passengers with these unique tickets
passengers_unique_tickets = titanic[titanic['Ticket'].isin(unique_ticket_numbers)]

passengers_unique_tickets.head()


10. Filter Passengers with 'Miss' in Their Name and Were in Class 1:
Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

# Female passengers with 'Miss' in their name and in Class 1
miss_class1 = titanic[
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1) &
    (titanic['Name'].str.contains('Miss'))
]

miss_class1.head()

