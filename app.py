import streamlit as st
from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]['label'], result[0]['score']  # Return both label and confidence score

# Custom CSS for a more subtle and flat design
st.markdown("""
<style>
body {
    background-color: #ffffff;  /* White background for the entire page */
    font-family: 'Helvetica', sans-serif;
}
.css-2trqyj {
    padding-top: 0rem;
}
.css-18e3th9 {
    padding: 0rem;
}
.stTextInput>div>div>input {
    background-color: #ffffff; /* Matching the background */
    border: none; /* No borders */
    padding: 10px;
    font-size: 16px;
    box-shadow: none; /* No shadow for a flatter look */
}
.stButton>button {
    color: #ffffff;
    background-color: #ff6347;
    border-radius: 10px;
    border: none;
    padding: 10px 24px;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s, color 0.3s;
    box-shadow: none;  /* No shadow for buttons */
}
.stButton>button:hover {
    background-color: #e55347;
}
.stMarkdown {
    background-color: #ffffff;
    border: none;
    padding: 10px;
    box-shadow: none; /* Removing shadows from markdown */
}
</style>
""", unsafe_allow_html=True)

# Set up the title and intro text
st.title('Sentiment Analysis App')
st.markdown("""
This app analyzes the sentiment of the text you provide. Type a comment and hit the 'Analyze' button to see the sentiment and confidence level of the analysis.
""", unsafe_allow_html=True)

# Text input for user
user_input = st.text_area("Enter your comment:", value="", placeholder="Type your comment here...", height=150)

if st.button('Analyze'):
    if user_input:
        sentiment, confidence = analyze_sentiment([user_input])
        st.success(f"Sentiment: **{sentiment}**")
        st.info(f"Confidence: **{confidence:.2f}**")

        st.bar_chart([confidence, 1-confidence])

        # Display the sentiment in a colored font
        color = 'green' if sentiment == 'POSITIVE' else 'red'
        st.markdown(f"<h1 style='color: {color};'>{sentiment}</h1>", unsafe_allow_html=True)
    else:
        st.error("Please enter a valid comment.")
else:
    st.write("Results will appear here after you submit your comment.")
