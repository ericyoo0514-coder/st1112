import streamlit as st


st.title("11/12 실습")


# 초기화
if "saved_a1" not in st.session_state:
    st.session_state.saved_a1 = ""
if "saved_a2" not in st.session_state:
    st.session_state.saved_a2 = ""


with st.form("forms1"):
    a1 = st.text_input("a1")
    s1 = st.form_submit_button("제출 1")


if s1:
    st.session_state.saved_a1 = a1


with st.form("forms2"):
    a2 = st.text_input("a2")
    s2 = st.form_submit_button("제출 2")


if s2:
    st.session_state.saved_a2 = a2  


st.divider()
st.write("기억된 a1:", st.session_state.saved_a1)
st.write("기억된 a2:", st.session_state.saved_a2)
st.write(a1+a2)


# Numeric input example using session_state
if "saved_num_a1" not in st.session_state:
    st.session_state.saved_num_a1 = 0
if "saved_num_a2" not in st.session_state:
    st.session_state.saved_num_a2 = 0

with st.form("number_form1"):
    num_a1 = st.number_input("Numeric a1")
    save_num1 = st.form_submit_button("Save 1")

if save_num1:
    st.session_state.saved_num_a1 = num_a1

with st.form("number_form2"):
    num_a2 = st.number_input("Numeric a2")
    save_num2 = st.form_submit_button("Save 2")

if save_num2:
    st.session_state.saved_num_a2 = num_a2

st.divider()
st.write("Saved numeric a1:", st.session_state.saved_num_a1)
st.write("Saved numeric a2:", st.session_state.saved_num_a2)
st.write(st.session_state.saved_num_a1 + st.session_state.saved_num_a2)
