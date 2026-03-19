import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

st.title("NewsPulse Dashboard")
st.write("Global News Trend Analyzer")

# Load dataset

df = pd.read_csv("news_with_sentiment (1).csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Detect text column automatically
text_col = df.columns[0]

if "cleaned_text" in df.columns:
    text_col = "cleaned_text"
elif "text" in df.columns:
    text_col = "text"
elif "title" in df.columns:
    text_col = "title"
else:
    text_col = df.columns[0]

# Top Trending Keywords

all_words = " ".join(df[text_col].astype(str)).split()

word_count = Counter(all_words)

top_words = word_count.most_common(10)

words = [w[0] for w in top_words]
counts = [w[1] for w in top_words]

st.subheader("Top Trending Keywords")

fig, ax = plt.subplots()
ax.bar(words, counts)

plt.xticks(rotation=45)

st.pyplot(fig)

# Sentiment Distribution


if "sentiment" in df.columns:

    st.subheader("Sentiment Distribution")

sentiment_count =df["Sentiment"].value_counts()

st.subheader("Sentiment Distribution")

st.write(sentiment_count)

# Pie Chart
labels = sentiment_count.index
values = sentiment_count.values

st.subheader("Sentiment Pie Chart")

fig2, ax2 = plt.subplots()
ax2.pie(values, labels=labels, autopct="%1.1f%%")

st.pyplot(fig2)

#News Summary

st.subheader("News Summary")

st.write("Total News Articles:", len(df))
st.write("Total Words:", len(all_words))

#Interactive Search

st.subheader("Search News")

keyword = st.text_input("Enter keyword")

if keyword:
#result = df[df[text_col].str.contains(keyword, case=False)]
 st.dataframe(result)