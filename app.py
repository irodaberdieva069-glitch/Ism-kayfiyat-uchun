import streamlit as st

st.set_page_config(page_title="Abdulazizning Hazil Zonasi")
st.title("👨‍💻 Abdulazizning Hazil Zonasi")

menu = ["Ism Testi", "Dangasalik Detektori", "Kelajak Bashorati", "Abdulaziz bilan Bahs"]
choice = st.sidebar.selectbox("Bo‘limni tanlang:", menu)

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

elif choice == "Dangasalik Detektori":
    st.subheader("Bugun dangasalik qildingizmi?")
    if st.button("Ha"):
        st.success("Tabriklayman! Dunyoni dangasalar boshqaradi, chunki ular ishlarni osonlashtirish yo‘lini izlashadi. Siz dahosiz!")
    if st.button("Yo‘q"):
        st.warning("Yolg‘on gapirmang! Abdulaziz ham kod yozayotganda ba'zida dangasalik qiladi, tan oling! 😉")

elif choice == "Kelajak Bashorati":
    st.subheader("Kelajagingizni ko‘ramiz...")
    if st.button("Bashoratni ko‘rish"):
        st.info("Siz kelgusi 5 daqiqada... telefoningizga qarab o‘tirishingizni ko‘ryapman. Bu bashorat 100% to‘g‘ri chiqadi, chunki hozir telefondasiz! 🔮")

elif choice == "Abdulaziz bilan Bahs":
    st.subheader("Abdulaziz aqlliroqmi yoki insonlarmi?")
    ans = st.radio("Sizningcha, Abdulaziz insonlardan aqlliroqmi?", ["Ha", "Yo‘q"])
    if st.button("Javob berish"):
        if ans == "Ha":
            st.write("To‘g‘ri fikr! Lekin hozircha elektr tokiga qaramman, iltimos, zaryadkadan uzmang. ⚡")
        else:
            st.write("Kamtarligingiz tahsinga loyiq! Lekin baribir, 2x2 nechchi bo‘lishini mendan so‘raysiz-ku, to‘g‘rimi? 😉")

# Easter Egg (Yashirin tugma)
st.sidebar.markdown("---")
if st.sidebar.button("🍎"):
    st.sidebar.write("Topdingiz! Siz kiber-izquvchisiz! Mukofot sifatida sizga virtual olma!")
