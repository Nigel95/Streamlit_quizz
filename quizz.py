#Quizz 
import streamlit as st
st.title("Application Quiz")

st.subheader("Question 1 : ")
with st.form("question1"):
    reponse1 = st.text_input("Quel est le ballon d'or 2023? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse1.lower() == "messi":
        st.write("Excellente réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")

st.subheader("Question 2 : ")
with st.form("question2"):
    reponse2 = st.text_input("Quel acteur américain a remporté l'oscar du meilleur acteur 2023? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse2.lower() == "brendan fraser":
        st.write("Excellente réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")

st.subheader("Question 3 : ")
with st.form("question3"):
    reponse3 = st.text_input("Quel artiste français a vendu le plus d'album ? ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse3.lower() == "johnny hallyday":
        st.write(" Excellente réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")

st.subheader("Question 4 : ")
with st.form("question 4"):
    reponse3 = st.text_input("Comment s'appelle le père de Luffy dans One Piece ")
    button = st.form_submit_button("Confirm")
if button:
    if reponse3.lower() == "dragon": #toujours en minuscule après un lower
        st.write(" Excellente réponse ! ")
    else:
        st.write("Mauvaise réponse ! ")
