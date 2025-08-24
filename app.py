import streamlit as st
import numpy as np
import pickle as pkl

# Load the saved model
model = pkl.load(open("finalpro.p", "rb"))

st.set_page_config(page_title="IDS", page_icon="⚕️", layout="centered", initial_sidebar_state="expanded")

def preprocess(logged_in, srv_diff_host_rate, dst_host_same_srv_rate, dst_host_rerror_rate, dst_host_same_src_port_rate, diff_srv_rate, dst_host_count, dst_host_srv_diff_host_rate, rerror_rate, srv_rerror_rate, dst_host_srv_count, dst_host_srv_rerror_rate, l12):   
    # Pre-processing user input   
    user_input = [logged_in, srv_diff_host_rate, dst_host_same_srv_rate, dst_host_rerror_rate, dst_host_same_src_port_rate, diff_srv_rate, dst_host_count, dst_host_srv_diff_host_rate, rerror_rate, srv_rerror_rate, dst_host_srv_count, dst_host_srv_rerror_rate, l12,1,1,10,1,0,0,0,0.04]
    user_input = np.asarray(user_input)
    user_input = user_input.reshape(1, -1)
    prediction = model.predict(user_input)
    return prediction

# Front end elements of the web page 
html_temp = """ 
    <style>
        body {
            background-size: cover;
        }
    </style>
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Intrusion detection System</h1> 
    </div> 
    """
# Display the front end aspect
st.markdown(html_temp, unsafe_allow_html=True) 

# Divide input fields into three columns
col1, col2, col3 = st.columns(3)

# First column
with col1:
    logged_in = st.number_input(label="dst_host_same_srv_rate", step=1., format="%.2f")
    srv_diff_host_rate = st.number_input(label="srv_serror_rate", step=1., format="%.2f")
    dst_host_same_srv_rate = st.number_input(label="logged_in", step=1., format="%.2f")
    dst_host_rerror_rate = st.number_input(label="dst_host_srv_serror_rate", step=1., format="%.2f")
   
# Second column
with col2:
    dst_host_same_src_port_rate = st.number_input(label="diff_srv_rate", step=1., format="%.2f")
    diff_srv_rate = st.number_input(label="dst_host_srv_count", step=1., format="%.2f")
    dst_host_count = st.number_input(label="dst_host_diff_srv_rate", step=1., format="%.2f")
    dst_host_srv_diff_host_rate = st.number_input(label="dst_host_serror_rate", step=1., format="%.2f")
    
# Third column
with col3:
    rerror_rate = st.number_input(label="dst_host_count", step=1., format="%.2f")
    srv_rerror_rate = st.number_input(label="same_srv_rate", step=1., format="%.2f")
    dst_host_srv_count = st.number_input(label="count", step=1., format="%.2f")
    dst_host_srv_rerror_rate = st.number_input(label="serror_rate", step=1., format="%.2f")
    l12 = st.number_input(label="dst_host_same_src_port_rate", step=1., format="%.2f")

# User input
if st.button("Predict"):    
    pred = preprocess(logged_in, srv_diff_host_rate, dst_host_same_srv_rate, dst_host_rerror_rate, dst_host_same_src_port_rate, diff_srv_rate, dst_host_count, dst_host_srv_diff_host_rate, rerror_rate, srv_rerror_rate, dst_host_srv_count, dst_host_srv_rerror_rate, l12)
    if pred[0] == 0:
        st.success('Normal')  
    elif pred[0] == 1:
        st.success('DoS attack')
        st.success('Denial of Service (DoS) attack is a type of cyber attack where an online resource, such as a website or network service, is made inaccessible to its intended users by overwhelming it with a large amount of traffic, requests, or malicious data.')
    elif pred[0] == 2:
        st.success('Probe attack')
        st.success('probe attack is a type of cyber attack where an unauthorized individual or entity attempts to gather information about a target network or system to identify vulnerabilities, potential entry points, or sensitive data.')
    elif pred[0] == 3:
        st.success('R2L attack')
        st.success(' R2L (Remote-to-Local) attack is a type of cyber attack where an unauthorized user attempts to gain access to a target system or network remotely in order to escalate their privileges and obtain unauthorized access to resources that are typically restricted to local users.')
    elif pred[0] == 4:
        st.success('U2R attack')
        st.success('U2R (User-to-Root) attack is a type of cyber attack where an unauthorized user with limited privileges on a system attempts to escalate their privileges to gain root or administrative access.')
