```python
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('C:\\Users\\OPIPLEX\\Desktop\\gadukasala\\COVID-19 Survey Student Responses.csv')
#TOTAL TIME SPENT ON ONLINE CLASSES OF PARTICULAR AGE

fig, ax = plt.subplots(figsize = (18,10))

sns.barplot(df['Age of Subject'],df['Time spent on self study'])

ax.set( ylabel="total time spent in age group",
       xlabel="Age of persons")
plt.title('total time spent on online class of particular age')


#MOST OF THE PERSONS ARE OF AGE 20.THE TOTAL NO OF PEOPLE OF AGE 20 IS 211. 
fig, ax = plt.subplots(figsize = (18,10))
plt.hist(df["Age of Subject"],bins=50)
plt.title('Age range of persons from 7 to 60')
plt.xlabel('Age range of persons')
plt.ylabel('No of persons belonging to particular age')

#YOU CAN CLEARLY CHECK THE AGE RANGE OF THE STUDENTS
#Laptop/desktop is widely used by peoples

fig, ax = plt.subplots(figsize = (18,10))
sns.countplot(df['Medium for online class'])
def age_range(data):
    if data<20:
        return "Below 20"
    elif (data>20) & (data<=40):
        return "20 to 40"
    else:
        return "40 to 60"
    
    
df['Age range'] = df['Age of Subject'].apply(lambda x:age_range(x))
#NO of peoples of particular age range
sns.countplot(df['Age range'])


#medium used by age

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Age of Subject'],hue=df['Medium for online class'])

ax.set( ylabel="Age range",
       xlabel="Age range of persons")
plt.title('Medium used by particular age range of persons')


# MEdium used by particular age range

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Medium for online class'],hue=df['Age range'])

ax.set( ylabel="Age range",
       xlabel="Age range of persons")
plt.title('Medium used by particular age range of persons')


#preferrred social media

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Prefered social media platform'],hue = df["Age range"])

ax.set( ylabel="Total  no of persons",
       xlabel="Social Media")
plt.title('Social media used by each group ')

#time spent on sleep
fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Time spent on sleep'],hue = df["Age range"])

ax.set( ylabel="total no of persons",
       xlabel="Time spent on sleep")
plt.title('total time spent on sleep by each age group')

#Time spent on tv

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Time spent on TV'],hue = df["Age range"])

ax.set( ylabel="total no of persons",
       xlabel="Time spent on TV")
plt.title('total time spent on TV by each age group')


#change in weight as per age range

fig, ax = plt.subplots(figsize = (10,5))

sns.countplot(df['Change in your weight'],hue = df["Age range"])

ax.set( ylabel="TOTAL NO OF STUDENTS",
       xlabel="CHANGE IN WEIGHT")
plt.title('CHANGE OF WEIGHT OF STUDENTS IN EACH GROUP')


#A PLOT FOR WHAT MOST STUDENTS MISSED. AND ITS CLEARLY SHOWN MOST STUDENTS OF AGE BELOW 20 MISSED SCHOOL/COLLEGE. sTUDENTS OF
# EACH AGE GROUP MISSED SCHOOL/COLLLEGES


fig, ax = plt.subplots(figsize = (40,15))

sns.countplot(df['What you miss the most'], hue=df["Age range"])
plt.xticks(rotation=90)
ax.set( ylabel="Age range",
       xlabel="What you missed")
plt.title('A plot for what most students missed the most')

```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'A plot for what most students missed the most')




    
![png](output_0_2.png)
    



    
![png](output_0_3.png)
    



    
![png](output_0_4.png)
    



    
![png](output_0_5.png)
    



    
![png](output_0_6.png)
    



    
![png](output_0_7.png)
    



    
![png](output_0_8.png)
    



    
![png](output_0_9.png)
    



    
![png](output_0_10.png)
    



    
![png](output_0_11.png)
    



```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('C:\\Users\\OPIPLEX\\Desktop\\gadukasala\\COVID-19 Survey Student Responses.csv')
```


```python
#TOTAL TIME SPENT ON ONLINE CLASSES OF PARTICULAR AGE

fig, ax = plt.subplots(figsize = (18,10))

sns.barplot(df['Age of Subject'],df['Time spent on self study'])

ax.set( ylabel="total time spent in age group",
       xlabel="Age of persons")
plt.title('total time spent on online class of particular age')



```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'total time spent on online class of particular age')




    
![png](output_2_2.png)
    



```python
#MOST OF THE PERSONS ARE OF AGE 20.THE TOTAL NO OF PEOPLE OF AGE 20 IS 211. 
fig, ax = plt.subplots(figsize = (18,10))
plt.hist(df["Age of Subject"],bins=50)
plt.title('Age range of persons from 7 to 60')
plt.xlabel('Age range of persons')
plt.ylabel('No of persons belonging to particular age')
```




    Text(0, 0.5, 'No of persons belonging to particular age')




    
![png](output_3_1.png)
    



```python
print("The Age range of 10-30 are the most of the students who are affected by the lockdown")

#Laptop/desktop is widely used by peoples

fig, ax = plt.subplots(figsize = (18,10))
sns.countplot(df['Medium for online class'])

print('Laptop is widely used by the students as the medium for online classes')

def age_range(data):
    if data<20:
        return "Below 20"
    elif (data>20) & (data<=40):
        return "20 to 40"
    else:
        return "40 to 60"
    


```

    The Age range of 10-30 are the most of the students who are affected by the lockdown
    Laptop is widely used by the students as the medium for online classes
    

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    


    
![png](output_4_2.png)
    



```python
    
df['Age range'] = df['Age of Subject'].apply(lambda x:age_range(x))
#NO of peoples of particular age range
sns.countplot(df['Age range'])
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    <AxesSubplot:xlabel='Age range', ylabel='count'>




    
![png](output_5_2.png)
    



```python
#medium used by age

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Age of Subject'],hue=df['Medium for online class'])

ax.set( ylabel="Age range",
       xlabel="Age range of persons")
plt.title('Medium used by particular age range of persons')

print('Laptop/desktop is widely used among each age groupof students')
print('Smartphone is widely used for the ages of students of 10-18')
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    

    Laptop/desktop is widely used among each age groupof students
    Smartphone is widely used for the ages of students of 10-18
    


    
![png](output_6_2.png)
    



```python
# MEdium used by particular age range

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Medium for online class'],hue=df['Age range'])

ax.set( ylabel="Age range",
       xlabel="Age range of persons")
plt.title('Medium used by particular age range of persons')
print('Smartphone is mostly used below 20 and laptop/desktop is widely used for 20 to 40')
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    

    Smartphone is mostly used below 20 and laptop/desktop is widely used for 20 to 40
    


    
![png](output_7_2.png)
    



```python
#preferrred social media

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Prefered social media platform'],hue = df["Age range"])

ax.set( ylabel="Total  no of persons",
       xlabel="Social Media")
plt.title('Social media used by each group ')
print('Youtube, whatsapp and instagram is the preferred social media below 20 ')
print('LinkedIn is most famous for the age group 20 to 40 as compared to other social media ')
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'Social media used by each group ')




    
![png](output_8_2.png)
    



```python
#time spent on sleep
fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Time spent on sleep'],hue = df["Age range"])

ax.set( ylabel="total no of persons",
       xlabel="Time spent on sleep")
plt.title('total time spent on sleep by each age group')

print('Maximum students of each age group has taken 8 hours of sleep')

```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'total time spent on sleep by each age group')




    
![png](output_9_2.png)
    



```python
#Time spent on tv

fig, ax = plt.subplots(figsize = (18,10))

sns.countplot(df['Time spent on TV'],hue = df["Age range"])

ax.set( ylabel="total no of persons",
       xlabel="Time spent on TV")
plt.title('total time spent on TV by each age group')

print('Maximum students has watched 0 hours of tv of each age group')
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'total time spent on TV by each age group')




    
![png](output_10_2.png)
    



```python
#change in weight as per age range

fig, ax = plt.subplots(figsize = (10,5))

sns.countplot(df['Change in your weight'],hue = df["Age range"])

ax.set( ylabel="TOTAL NO OF STUDENTS",
       xlabel="CHANGE IN WEIGHT")
plt.title('CHANGE OF WEIGHT OF STUDENTS IN EACH GROUP')

print('The weight of most of the students of all age groups is remains constant ')
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'CHANGE OF WEIGHT OF STUDENTS IN EACH GROUP')




    
![png](output_11_2.png)
    



```python
#A PLOT FOR WHAT MOST STUDENTS MISSED. AND ITS CLEARLY SHOWN MOST STUDENTS OF AGE BELOW 20 MISSED SCHOOL/COLLEGE. sTUDENTS OF
# EACH AGE GROUP MISSED SCHOOL/COLLLEGES


fig, ax = plt.subplots(figsize = (40,15))

sns.countplot(df['What you miss the most'], hue=df["Age range"])
plt.xticks(rotation=90)
ax.set( ylabel="Age range",
       xlabel="What you missed")
plt.title('A plot for what most students missed the most')


print('Most of the students missed their school/colleges')
```

    C:\Users\OPIPLEX\anaconda3\lib\site-packages\seaborn\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    




    Text(0.5, 1.0, 'A plot for what most students missed the most')




    
![png](output_12_2.png)
    



```python

```
