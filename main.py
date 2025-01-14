#import libraries
import streamlit as st
import pandas as pd
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Netflix Userbase Data Information Collab")

#adding a description to your website
st.header('Bari, Mark, & Ojas')

st.write("Hi! My name is Barindra Surjaudaja and I will be attending Grade 10. Furthermore, I've had quite a bit of experience with Python coding using IDLE (eg: selection statements, loops, if statements, lists, etc). However, this AI course has definately enhanced my knowledge regarding AI and the extraction of data and information to form data charts. This knowledge, without a doubt, will be very useful!")

st.write("Hi, I'm Ojas, I'm currently in high school. I had a bit of prior experience in coding before joining AI camp, but I plan to deepen my understanding and learn some new skills.")

st.write("Hello! My name is Mark Liu. Currently, I am a high school student. I have studied both Java and Python in the past. I joined this camp to delve deeper into AI coding and further expand my expertise.")



st.header('Context to the Dataset')

st.write("These charts are formed to show numerous different data informative charts mainly revolving around the topic of the Netflix subscriptions. Within this split, we have charts outputting information on which subscription is most popular, the different gender-wise interests of different subscriptions, the country-wise choices of subscriptions, and shows which subscription is most profitable. In addition to that, we have a few other charts that also shows information regarding Netflix itself: which country generates most income for the company and which is the most used device to watch Netflix. All these charts are extremely important to propose a sense of what the company, Netflix, is like.")



st.header("Dataset")

image = Image.open("Subscription Type in Different Country.png")
st.image(image,caption="Bar graph showing the number of various subscription types from different countries.")

st.write("The bar graph provides a visualization of the three primary Netflix subscription tiers: Basic, Standard, and Premium, across various countries. Each country has a distinct preference pattern, with variations in the distribution of these subscription types. This variation highlights the differing consumption tendencies of Netflix's subscription in different geographical regions.")

image = Image.open("Device Percentage.png")
st.image(image,caption="Pie chart showing the various device types used to watch Netflix.")

st.write("The pie chart provides a visual representation of the diverse range of device types utilized to access Netflix. From smartphones to laptops, the chart displays a similar user count, suggesting a balanced preference among Netflix's audience across all platforms.")

image = Image.open("chart that shows gender-wise interest of subscription type.png")
st.image(image, caption="This graph illustrates which subscription is most popular among the 2 genders")

image = Image.open("chart that shows how many subscriptions are buyed according to type of subscription.png")
st.image(image, caption="This graph illustrates the most profitable and popular Netflix subscriptions by examining which is most frequently purchased")

image = Image.open('total revenue by subscription.png')
st.image(image, caption='Displays the total revenue generated by different subscriptions')

st.write("This chart explains which subscription tiers are the most profitable. Knowing this can guide business strategies, like restructuring the subscriptions ot maximize revenue.")

image = Image.open('total revenue by country.png')
st.image(image, caption='Visualizes the cumulative revenue generated by each country')

st.write("The chart showcases the economic contribution of different countries to the platform, with certain countries standing out. This insight can be crucial when deciding on things like marketing strategies.")


st.header("Conclusion")
st.write("The analysis of the sample Netflix dataset offers insights into user behavior and preferences. We observe that certain countries not only have a higher number of subscribers but also contribute significantly to the platform's revenue. This indicates potential markets for targeted advertising or exclusive content launches. The data also reveals a varied device usage pattern among subscribers, emphasizing the importance of ensuring optimal streaming quality across all platforms. Interestingly, the more expensive subscriptions do not always lead to more profit. Understanding these nuances, even from a hypothetical dataset, is instrumental for strategic planning in areas like content creation and marketing campaigns.")
