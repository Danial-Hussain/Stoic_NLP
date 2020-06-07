# A Classic Revival: Generating stoic philosophy using NLP

## Introduction

I recently finished reading the book "The Obstacle is the Way" by Ryan Holiday. The book eloquently presents the idea of stoicism and combating each life obstacle with grace and resilience. Many important stoic philosophers from the Hellenistic time period are mentioned including Marcus Aurelius, Seneca, and Epictetus. For those who haven't read it, I definitely recommend this book.

In light of wanting to learn more about the ancient, yet supremely prevalent, Stoic philosophy, while also wanting to learn more about natural language processing I decided to start a project that aims to generate new quotes based on Stoicism.

## Data Collection

The first stage in any data science project is collecting the data. Since I was seeking to generate new stoic quotes, I needed to collect stoic quotes from past philosophers so that my model could learn patterns in stoic speech. In particular I choose to gather the data from the books of three of the most notable stoic philosophers: Marcus Aurelius, Seneca, and Epictetus. 

The data was collected by scraping the MIT classics website along with Wikipedia. The python scripts for the data collection can be found in the scripts folder. After collecting the data I converted the data into a pandas data frame to be saved as a csv file. Later, I would join all the data frames together to form one massive data set. 

## Data Preprocessing

In order for the computer to understand the data, we must format it in a readable way. This involves many steps including tokenization and flattening. Tokenization involves making all the text lowercase, removing punctuation, and splitting words to be assigned to numbers. Flattening involves reducing the data to one dimension. After flattening the data, I used the "sliding window" strategy for setting up the training data. Sliding window refers to using a set amount of sequential data to predict the next variable in the sequence.

The python code for the data processing can be found in the models folder and is titled "processing.py"

## Model Engineering

Now that the data was ready to be processed by the model I trained three different LSTMs, each with slightly different parameters. LSTM's are type of neural network that are used commonly in natural language processing because they work particularly well with sequences of data. Since the sequence of the words is extremely important in sentences, LSTMs were perfect for text generation. All the notebooks for each LSTM model can be found in the models folder.

The three models I trained included a base model (model 1), a model with an increase in the amount of neurons (model 2), and a model with an increased dropout (model 3). After training each of the models here were the following accuracies:

![alt text](https://github.com/Danial-Hussain/Stoic_NLP/blob/master/results/joined.png "Results")

Out of all the models Model 2, the model with more neurons, performed slightly better than the rest.

After training the models, I used the models to come up with new quotes. The results can be found in the results folder but here is one quote: 

"hope doth is large and perishable of manifold words the shore'"

## Conclusion + Future Possibilities

While much of what my models spewed was utter nonsense, some promising signs did emerge. The fact that I only trained the models for 100 epochs and the accuracy was still increasing, gives hope to the notion that longer training may provide better results. Additionally, the data collected for this project was derived from only 5 stoic books. Collecting more data could produce even better results. Overall, this project was a great introduction for me to the realm of natural language processing. I learned many interesting techniques such as tokenization and using LSTM's.











