import streamlit as st
import n1tk
from transformer import pipline
from nltk.corpus import word_tokenize

chatbot = pipline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please Consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "would you like to schedule appointment with doctor?"
    elif "medication" in user_input:
        return "its important to take prescribed medicines regularly. if you have cocerns, consult your doctor"
    else :
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input=st.text_input("How I can Assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User : ", user_input)
            with st.spinner("processing your query, please wait...."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant :",response)
            print(response)
    else:
             st.write("Please enter message to get a response.")

main()
