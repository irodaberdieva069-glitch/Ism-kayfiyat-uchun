import streamlit as st

st.title("Ismingizni tanlang!")

# Ism kiritish
name = st.text_input("Ismingizni kiriting:")

if name:
    choice = st.radio("Qaysi ism chiroyliroq?", ["Abdulaziz", "Diyora", "Farzona"])
    
    if st.button("Tanlash"):
        if choice == "Abdulaziz":
            st.balloons() # Xlapushka effekti
            st.write("Didingiz chakki! Bu mening yaratuvchimning ismi. Shunchaki paxta qo'ydim 😂")
        elif choice == "Diyora":
            st.write("Voy, siz eng zo'rini tanladingiz! Bu ism juda chiroyli. Paxta! 🤣😂")
        elif choice == "Farzona":
            st.write("Bu eng chiroyli ism! Bu paxta emas, shunchaki paxta paxta xal qulay 2 ta paxta 😂")
        
        st.session_state['show_next'] = True

if st.session_state.get('show_next'):
    if st.button("Keyingi sahifa"):
        st.write("Xayr! Tug'ilgan kuningiz bilan! O'zi bugunmidi? 🤔")
        st.write("Iye, atiga 1 yilgina adashibman! Xayr! 👋")
