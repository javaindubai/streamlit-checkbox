import streamlit as st


def checkbox_advance_examples():
    st.subheader("Streamlit Checkbox advance examples")
    st.checkbox('Send SMS', key='sms', help='Sending message to registered **mobile**', on_change=what_is_sending, args=('SMS',))
    st.checkbox('Send Email', key='email', on_change=what_is_sending, args=('Email',))
    st.checkbox('Send SMS and Email', key='emailsms', on_change=what_is_sending, args=('SMS and Email',))
    st.checkbox('Thank You', key='ty', value=True, disabled=True)
    st.checkbox('Share and Comment', key='sac', value=True, disabled=True)
    st.checkbox('Subscribe', key='s', value=True, disabled=True)
    st.markdown('----')
    st.subheader("End of Checkbox Tutorial")
    st.markdown('----')



def what_is_sending(type: str):
    st.write("on_change is called and selected option : "+type)