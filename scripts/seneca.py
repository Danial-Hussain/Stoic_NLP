import html2text
import requests as rq
import pandas as pd
import re

"""
This Python script is used to gather the data from the book Moral letters to Lucilius by Seneca
The Data is collected from the MIT Classics website
The Data is cleaned, processed, transformed into a dataframe and finally stored as a csv file.
To be run in a jupyter notebook
"""

def seneca():
    letters = [x for x in range(1,125)]
    df = pd.DataFrame(columns = ["Lesson"])
    
    for letter in letters:
        website = "https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_{}".format(letter)
        try:
            res = rq.get(website)
        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"      
        
        res = rq.get(website)
        data = res.text
        data = html2text.html2text(data)
        
        #Remove introduction and conclusion
        data = data.partition("Footnotes")[0]
        data = data.partition("\n\n**1.** ")[2]
        
        #Remove ending
        data = re.sub(r'\n\n##\n', '', data)
        
        #Remove bolded numbers
        data = re.sub(r'[**0-9**].', '', data)

        #Remove brackets
        data = re.sub(r'[[]','',data)

        #Remove underlines
        data = re.sub(r'_', "", data)
        
        #add new data to the end of dataframe
        df.loc[len(df)] = [data]
        
    #Clean data frame
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
    letters = df.to_csv(r'data\letters.csv', index = False)
    
    return df

    
s = seneca()