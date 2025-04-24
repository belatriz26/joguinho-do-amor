import streamlit as st
import time

st.set_page_config(page_title="MOMOS<3", layout="centered")

def countdown():
    for i in range(3, 0, -1):
        st.markdown(f"<h1 style='text-align:center; color:white; font-size:72px'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
        st.empty()

def run_race():
    for i in range(8):
        st.image("city-night-race-bg.jpg", use_column_width=True)
        st.image("car-male.png", width=100)
        time.sleep(0.25)
        st.empty()

def show_love_screen():
    st.image("city-night-race-bg.jpg", use_column_width=True)
    st.image("car-female.png", width=100)
    st.markdown("<h1 style='text-align:center; color:pink;'>Te Amo 💖</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🚗 Joguinho do Amor</h1>", unsafe_allow_html=True)

if "started" not in st.session_state:
    st.session_state.started = False

if st.button("Start" if not st.session_state.started else "Reiniciar"):
    st.session_state.started = True
    st.empty()
    countdown()
    run_race()
    show_love_screen()
