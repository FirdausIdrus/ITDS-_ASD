import streamlit as st

# Set the title of the app
st.title('Autism Prediction Disorder (ASD) Prediction Analysis')

# Displaying an image
st.image("img_1.jpg",
         caption="Accept . Understand . Love")

# Sections
st.markdown("## Introduction")
st.markdown("""
Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition characterized by challenges in social interaction, repetitive behaviors, and communication. Understanding the prevalence and factors associated with ASD is crucial for early diagnosis and intervention.
Recent figures from 2023 show a significant rise in the number of individuals diagnosed with ASD, underscoring the importance of developing efficient diagnostic methods. This project aims to analyze demographic and behavioral data to identify patterns and factors that can assist in the early detection and treatment of ASD.

""")

st.markdown("## Problem Statement")
st.markdown("""
Autism Spectrum Disorder (ASD) presents major obstacles to early diagnosis and treatment, which affect patient outcomes and how resources are distributed in healthcare facilities. The majority of current diagnostic techniques primarily depend on behavioural observations and standardized screening tests, which frequently fail to detect subtle or atypical signs of ASD and hinder the development of individualized treatment plans and early intervention. Thus, a predictive model that makes use of machine learning algorithms is desperately needed in order to evaluate ASD risk, improve diagnostic precision, and provide prompt intervention and tailored therapy sessions. Furthermore, by offering insights into the severity of ASD in specific individuals, such a model would enable optimal resource allocation, minimizing resource waste and maximizing care for those in need. In line with the objectives of enhancing well-being and streamlining healthcare delivery, the overarching problem statement seeks to create an ASD prediction model that helps medical professionals—especially neurologists and therapists—identify, diagnose, and plan individualized interventions for patients with ASD.
""")

st.markdown("## Project Objectives")
st.markdown("""
Developing predictive models for autism spectrum disorder (ASD) with data science techniques aims to increase diagnostic accuracy and facilitate early therapies, both of which can improve outcomes for ASD sufferers. Analyzing extensive datasets of behavioral, genetic, and environmental ASD-related data allows machine learning algorithms to detect patterns and trends indicative of ASD likelihood. Clinicians can detect early warning signs and symptoms that may point to the presence of ASD in patients who may be at risk of the disorder by using precise predictive models. By offering extra information and insights to help physicians make diagnoses, the autism prediction model increases the diagnostic process' efficiency and accuracy. The lives of people with ASD and their families can undoubtedly be significantly impacted by increasing diagnostic accuracy and offering early interventions. It can also lessen the load on support networks and healthcare systems by identifying those who need interventions and therapies at an earlier age, when they are most successful.
""")


st.markdown("## Team Members")
st.markdown("""
- AINULHAYAT AWATIF BINTI ZAINUL  U2000999
- AINA SOFEAH BINTI YUSOFF  U2001013
- MUHAMMAD NUR FIRDAUS BIN MOHD IDRUS  U2001256
- NAZIF AQIF BIN MUHAMMAD AFIFI  U2102726
- NURUL AISYAH BINTI NORHISHAM  U2100789
""")


# Sidebar for selecting analysis
# st.sidebar.title('ASD Analysis Options')
# analysis_type = st.sidebar.selectbox(
#   'Select Analysis Type',
#   ('ASD by Ethnicity', 'ASD by Gender', 'ASD by Age',
#    'ASD by Country of Residence', 'ASD by Jaundice', 'ASD by Genetic Root')
# )
