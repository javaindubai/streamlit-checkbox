import streamlit as st


def checkbox_basic_examples():
    st.subheader("Streamlit Checkbox basic Examples")
    st.checkbox('Unchecked')
    st.checkbox('Checked', value=True, key="DefaultChecked")
    st.checkbox('Default Disabled', value=False, key="dd", disabled=True)
    st.checkbox('Checked Disabled', value=True, key='cd', disabled=True)
    st.subheader('Read Checkbox status (checked/unchecked) Examples')
    isChecked = st.checkbox('One', key='one')
    st.write('Value of isChecked: '+str(isChecked))
    if isChecked:
        st.write('CHECKED')
    else:
        st.write('UNCHECKED')
    st.subheader('Basic Examples Done')