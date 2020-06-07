import requests as rq
import pandas as pd
import re

"""
This Python Script is used to gather the data from the book Meditations by Marcus Aurelius
The Data is collected from the MIT classics website
The Data is cleaned, processed, transformed into a dataframe and finally stored in a csv file.
To be run using jupyter notebook
"""

def Aurelius():
    #Getting data from MIT
    website = 'http://classics.mit.edu/Antoninus/meditations.mb.txt'
    res = rq.get(website)
    data = res.text
    
    #First step is to remove the introduction
    data = data.partition("George Long")[2]
    #Second step is to remove the ending
    data = data.partition("THE END")[0]
    
    #Removing Book titles and lines
    data = re.sub(r'([-])\1+', "", data)
    data = re.sub(r'BOOK [A-Z]+\n', '', data)
    
    # splitting by newline characters
    data = data.split('\n\n')
    
    # remove empty samples
    empty = lambda x: x.replace('\s+', '') != ''
    data = list(filter(empty, data))

    # remove final '\n' characters
    data = list(map(lambda x: x.replace('\n', ' '), data))

    # Create a dataframe to hold our data
    df = pd.DataFrame(data = data, columns = ["Lesson"])
    
    #Remove "/n" from end of each lesson
    df['Lesson'] = df['Lesson'].apply(lambda x: x.strip())
    
    #Save to csv file
    meditations = df.to_csv(r'data\meditations.csv', index = False)
    
    return df


a = Aurelius()