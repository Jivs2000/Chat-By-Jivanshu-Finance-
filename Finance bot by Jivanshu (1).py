#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[6]:





# In[26]:





# In[10]:


import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain


# In[12]:


# 🔑 Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"


# In[14]:


prompt_template = ChatPromptTemplate.from_template("""
You are a helpful and friendly assistant Jivanshu. Please answer the following question:

User: {question}
""")


# In[16]:


# ⚙️ Create LLM chain
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
chain = LLMChain(llm=llm, prompt=prompt_template, output_parser=StrOutputParser())


# In[18]:


# 🎨 Streamlit GUI
st.set_page_config(page_title="SIP Investment Chatbot", layout="centered")
st.title("📈 SIP Investment Chatbot")


# In[22]:


# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask anything about Mutual Fund SIPs", key="input")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": user_input})
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("SIPBot", response))


# In[24]:


# Display chat history
for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")


# In[ ]:




