import streamlit as st

# Sahifa sozlamalari
st.set_page_config(page_title="Abdulazizning Hazil Zonasi", page_icon="👨‍💻")

st.title("👨‍💻 Abdulazizning Hazil Zonasi")
st.sidebar.header("Menyu")

menu = ["Ism Testi", "Dangasalik Detektori", "Kelajak Bashorati", "Abdulaziz bilan Bahs", "Mantiqiy Tuzoq", "Sirli Tugma"]
choice = st.sidebar.selectbox("Bo‘limni tanlang:", menu)

# 1. Ism Testi
if choice == "Ism Testi":
    st.subheader("Qaysi ism chiroyliroq?")
    name = st.text_input("Ismingizni kiriting:")
    if name:
        option = st.radio("Tanlang:", ["Abdulaziz", "Diyora", "Farzona"])
        if st.button("Tekshirish"):
            if option == "Abdulaziz":
                st.balloons()
                st.write("Didingiz chakki! Bu mening yaratuvchimning ismi. Shunchaki paxta qo‘ydim 😂")
            elif option == "Diyora":
                st.write("Voy, siz eng zo‘rini tanladingiz! Bu ism juda chiroyli. Paxta! 🤣😂")
            elif option == "Farzona":
                st.write("Bu eng chiroyli ism! Bu paxta emas, shunchaki paxta paxta xal qulay 2 ta paxta 😂")
            
            st.markdown("---")
            if st.button("Keyingi sahifa"):
                st.write("Xayr! Tug‘ilgan kuningiz bilan! O‘zi bugunmidi? 🤔 Iye, atiga 1 yilgina adashibman, xayr! 👋")

# 2. Dangasalik Detektori
elif choice == "Dangasalik Detektori":
    st.subheader("Bugun dangasalik qildingizmi?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ha"):
            st.success("Tabriklayman! Dunyoni dangasalar boshqaradi, chunki ular ishlarni osonlashtirish yo‘lini izlashadi. Siz dahosiz!")
    with col2:
        if st.button("Yo‘q"):
            st.warning("Yolg‘on gapirmang! Abdulaziz ham kod yozayotganda ba'zida dangasalik qiladi, tan oling! 😉")

# 3. Kelajak Bashorati
elif choice == "Kelajak Bashorati":
    st.subheader("Kelajagingizni ko‘ramiz...")
    if st.button("Bashoratni ko‘rish"):
        st.info("Siz kelgusi 5 daqiqada... telefoningizga qarab o‘tirishingizni ko‘ryapman. Bu bashorat 100% to‘g‘ri chiqadi! 🔮")

# 4. Abdulaziz bilan Bahs
elif choice == "Abdulaziz bilan Bahs":
    st.subheader("Abdulaziz (AI) bilan bahs")
    user_arg = st.text_input("Fikringizni yozing:")
    if st.button("Bahslashish"):
        if user_arg:
            st.write(f"'{user_arg}' dedingizmi? Hmm... Yo‘q, bu mutlaqo xato! Abdulaziz hammasini sizdan yaxshiroq biladi, qabul qiling! 😎")

# 5. Mantiqiy Tuzoq
elif choice == "Mantiqiy Tuzoq":
    st.subheader("Abdulazizning mantiqiy tuzog‘i")
    ans = st.radio("Bir kunda necha marta ovqatlanish kerak?", ["1 marta", "3 marta", "Abdulaziz xohlagancha"])
    if st.button("Tekshirish"):
        if ans == "Abdulaziz xohlagancha":
            st.write("Dahshat! Siz haqiqiy 'Abdulaziz fanati'siz! Lekin baribir sog‘lig‘ingizni o‘ylang! 😉")
        else:
            st.write("Xato! To‘g‘ri javob: 'Abdulaziz xohlagancha'. Chunki qoida shunaqa! 😂")

# 6. Sirli Tugma
elif choice == "Sirli Tugma":
    st.subheader("Bu yerda hech narsa yo‘q...")
    if st.button("Bosma!"):
        st.error("Dedim-ku, bosmang deb! Endi Abdulaziz sizning ekraningizni buzib qo‘yadi (hazil)! ⚠️")
