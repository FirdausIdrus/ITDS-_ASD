import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("autism_train_after_cleaning.csv")

# Create a sidebar for navigation
st.sidebar.title('Analysis and Prediction')
nav = st.sidebar.selectbox('Select: ', ['Analysis', 'Prediction'])

# Analysis Section
if nav == 'Analysis':
    st.title('Autism Specrtum Disorder (ASD) Analysis')
    st.subheader('Select an aspect to analyze:')
    analysis_type = st.selectbox('Select an aspect', [
                                 'ethnicity', 'gender', 'age', 'country', 'jaundice', 'autism_genetic_root'])

    if analysis_type == 'ethnicity':
        st.subheader('ASD by Ethnicity')
        ethnicity_counts = df['ethnicity'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(ethnicity_counts.index, ethnicity_counts.values)
        ax.set_title('ASD by Ethnicity')
        ax.set_xlabel('ethnicity')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    elif analysis_type == 'gender':
        st.subheader('ASD by Gender')
        gender_counts = df['gender'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(gender_counts.index, gender_counts.values)
        ax.set_title('ASD by Gender')
        ax.set_xlabel('gender')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    elif analysis_type == 'age':
        st.subheader('ASD by Age')
        age_counts = df['age'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(age_counts.index, age_counts.values)
        ax.set_title('ASD by Age')
        ax.set_xlabel('age')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    elif analysis_type == 'country':
        st.subheader('ASD by Country of Residence')
        country_counts = df['country'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(country_counts.index, country_counts.values)
        ax.set_title('ASD by Country of Residence')
        ax.set_xlabel('country')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    elif analysis_type == 'jaundice':
        st.subheader('ASD by Jaundice')
        jaundice_counts = df['jaundice'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(jaundice_counts.index, jaundice_counts.values)
        ax.set_title('ASD by Jaundice')
        ax.set_xlabel('jaundice')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    elif analysis_type == 'autism_genetic_root':
        st.subheader('ASD by Genetic Root')
        genetic_root_counts = df['autism_genetic_root'].value_counts()
        fig, ax = plt.subplots()
        ax.bar(genetic_root_counts.index, genetic_root_counts.values)
        ax.set_title('ASD by Genetic Root')
        ax.set_xlabel('autism_genetic_root')
        ax.set_ylabel('Count')
        st.pyplot(fig)

# Prediction Section
elif nav == 'Prediction':
    st.title('Autism Specrtum Disorder (ASD) Prediction')
    st.subheader('Please answer the following questions:')
    questions = [
        'I often notice small sounds when others do not.',
        'I usually concentrate more on the whole picture, rather than the small details.',
        'I find it easy to do more than one thing at once.',
        'If there is an interruption, I can switch back to what I was doing very quickly.',
        'I find it easy to read between the lines when someone is talking to me..',
        'I know how to tell if someone listening to me is getting bored.',
        'When I am reading a story, I find it difficult to work out the character s intention.',
        'I like to collect information about categories of things (e.g. types of car, types of bird, types of train, types of plant, etc.)',
        'I find it easy to work out what someone is thinking or feeling just by looking at their face.',
        'I find it difficult to work out people’s intentions.'
    ]
    answers = []
    for question in questions:
        answer = st.selectbox(question, [0, 1])
        answers.append(answer)

    if st.button('Get Prediction'):
        # Calculate the prediction score
        prediction_score = sum(answers) / len(answers)

        # Display the prediction result
        if prediction_score > 0.5:
            st.subheader('You are at high risk of having ASD.')
        else:
            st.subheader('You are at low risk of having ASD.')
