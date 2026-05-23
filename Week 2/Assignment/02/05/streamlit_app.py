
import streamlit as st, requests
st.title('Week2 Backend API Tester')
base=st.text_input('Base URL','http://localhost:8105')
if st.button('Health'): st.write(requests.get(f"{base}/health",timeout=5).json())
with st.form('post'):
    title=st.text_input('title'); content=st.text_area('content'); ok=st.form_submit_button('Create Post')
if ok: st.write(requests.post(f"{base}/posts",json={'title':title,'content':content},timeout=5).json())
if st.button('List Posts'): st.write(requests.get(f"{base}/posts",timeout=5).json())
prompt=st.text_input('AI Prompt')
if st.button('AI Chat'): st.write(requests.post(f"{base}/ai/chat",json={'prompt':prompt},timeout=5).json())
