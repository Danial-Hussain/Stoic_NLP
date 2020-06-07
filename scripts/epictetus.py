import requests as rq
import pandas as pd
import re

"""
This Python script is used to gather the data from the book Enchiridion by Epictetus
The Data is collected from the MIT Classics website
The Data is cleaned, processed, transformed into a dataframe and finally stored as a csv file.
To be run using jupyter notebook
"""

def Enchiridion():
    #Getting data from MIT
    website = 'http://classics.mit.edu/Epictetus/epicench.1b.txt'
    res = rq.get(website)
    data = res.text

    #First step is to remove the introduction
    data = data.partition("Elizabeth Carter")[2]
    #Second step is to remove the ending
    data = data.partition("THE END")[0]
    
    #Remove any number
    data = re.sub(r"[0-9].", "", data)
    
    # splitting by newline characters
    data = data.split('\n\n')
    
    #Remove the first blank element and last blank element
    data.pop(0)
    data.pop(len(data)-1)
        
    # remove empty samples
    empty = lambda x: x.replace('\s+', '') != ''
    data = list(filter(empty, data))

    # Create a dataframe to hold our data
    df = pd.DataFrame(data = data, columns = ["Lesson"])
    
    #Remove "/n" from end of each lesson
    df['Lesson'] = df['Lesson'].apply(lambda x: x.strip())
    
    #Remove "/n" from middle of strings
    df['Lesson'] = df['Lesson'].apply(lambda x: x.replace('\n', " "))
    
    #Remove period if at the front of string
    df['Lesson'] = df['Lesson'].apply(lambda x: x[2:] if x[0] == '.' else x)
    
    df['Lesson'] = df['Lesson'].str.split('.')
    df = df.explode('Lesson')
    df = df.reset_index().drop(columns = 'index')
    df = df.replace(" ", float('NaN'))
    df = df.replace("", float('NaN'))
    df = df.drop(index = df[df['Lesson'].isnull()].index).reset_index().drop(columns = 'index')
    df = df.drop(index = df[df['Lesson'].map(len)<2].index).reset_index().drop(columns = 'index')
    
        
    #Save to csv file
    enchiridion = df.to_csv(r'data\enchiridion.csv', index = False)
    
    return df

e = Enchiridion()



import requests as rq
import pandas as pd
import re

"""
This Python script is used to gather the data from the book Dicourses by Epictetus
The Data is collected from the MIT Classics website
The Data is cleaned, processed, transformed into a dataframe and finally stored as a csv file.
"""

def Discourses():
    #Getting data from MIT
    website = 'http://classics.mit.edu/Epictetus/discourses.mb.txt'
    res = rq.get(website)
    data = res.text
    
    #Remove Introduction
    data = data.partition('BOOK ONE')[2]
    #Remove Conclusion
    data = data.partition('</pre')[0]
    
    #Remove the word chapter followed by number
    data = re.sub(r"Chapter [0-9]", "", data)
    #Remove any number
    data = re.sub(r"[0-9]", "", data)
    
    # splitting by newline characters
    data = data.split('\n\n')
    
    # remove empty samples
    empty = lambda x: x.replace('\s+', '') != ''
    data = list(filter(empty, data))
    data.pop(0)
    
    # Create a dataframe to hold our data
    df = pd.DataFrame(data = data, columns = ["Lesson"])
    
    #Remove "/n" from end of each lesson
    df['Lesson'] = df['Lesson'].apply(lambda x: x.strip())
    
    #Remove "/n" from middle of strings
    df['Lesson'] = df['Lesson'].apply(lambda x: x.replace('\n', " "))
    
    #Remove non paragraphs
    for x in range(len(df['Lesson'])):
        if len(df.loc[x][0]) < 80:
            df.drop(x,inplace = True)
    
    df = df.reset_index().drop(columns = 'index')
    df['Lesson'] = df['Lesson'].str.split('.')
    df = df.explode('Lesson')
    df = df.reset_index().drop(columns = 'index')
    df = df.replace(" ", float('NaN'))
    df = df.replace("", float('NaN'))
    df = df.drop(index = df[df['Lesson'].isnull()].index).reset_index().drop(columns = 'index')
    df = df.drop(index = df[df['Lesson'].map(len)<2].index).reset_index().drop(columns = 'index')
    
    #Save to csv file
    discourses = df.to_csv(r'data\discourses.csv', index = False)
    
    return df

d = Discourses()


"""
This Python script is used to gather the data from the book The Golden Sayings by Epictetus
The Data is collected from the MIT Classics website
The Data is cleaned, processed, transformed into a dataframe and finally stored as a csv file.
To be run in jupyter notebook
"""

def Golden_Sayings():
    #Getting data from MIT
    website = 'http://classics.mit.edu/Epictetus/goldsay.mb.txt'
    res = rq.get(website)
    data = res.text
    
    #Remove introduction
    data = data.partition('SECTION 1')[2]
    #Remove Conclusion and section 4
    data = data.partition("SECTION 4")[0]
    
    #Remove the word chapter followed by number
    data = re.sub(r"SECTION [0-9]", "", data)
    #Remove any number
    data = re.sub(r"[0-9]", "", data)
    
    #Remove Lines
    data = re.sub(r'([-])\1+', "", data)

    # splitting by newline characters
    data = data.split('\n\n')
    
    #Remove Roman numerals
    for element in range(len(data)):
        data[element] = re.sub(r'(^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$)', '', data[element])
    
    # remove empty samples
    empty = lambda x: x.replace('\s+', '') != ''
    data = list(filter(empty, data))
    data.pop(0)
    
    # Create a dataframe to hold our data
    df = pd.DataFrame(data = data, columns = ["Lesson"])
    
    #Remove "/n" from end of each lesson
    df['Lesson'] = df['Lesson'].apply(lambda x: x.strip())
    
    #Remove "/n" from middle of strings
    df['Lesson'] = df['Lesson'].apply(lambda x: x.replace('\n', " "))
    
    df['Lesson'] = df['Lesson'].str.split('.')
    df = df.explode('Lesson')
    df = df.reset_index().drop(columns = 'index')
    df = df.replace(" ", float('NaN'))
    df = df.replace("", float('NaN'))
    df = df.drop(index = df[df['Lesson'].isnull()].index).reset_index().drop(columns = 'index')
    df = df.drop(index = df[df['Lesson'].map(len)<2].index).reset_index().drop(columns = 'index')
    
    #Save to csv file
    golden_sayings = df.to_csv(r'data\golden_sayings.csv', index = False)
    
    return df
    
g = Golden_Sayings()