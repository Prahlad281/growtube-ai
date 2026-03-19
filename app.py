import streamlit as st
import random

st.set_page_config(page_title="GrowTube AI", layout="centered")

st.title("🔥 GrowTube AI")
st.write("Generate Viral YouTube Titles + Hooks 🚀")

topic = st.text_input("Enter your video idea (example: survival, fitness, motivation)")

if st.button("Generate Ideas"):

    templates = [
        "I Survived {n} Days {idea} 😱",
        "No Food, No Help – {n} Days {idea} 😨",
        "I Tried {idea} For {n} Days 😳",
        "{n} Days Challenge ({idea}) 😬",
        "This {idea} Almost Broke Me 😰"
    ]

    hooks = [
        "Day 1 was easy... but Day {n} almost broke me 😳",
        "I didn’t expect THIS to happen 😨",
        "This challenge almost killed me... 😱",
        "No food. No help. Just survival 😬",
        "I was not ready for this 😳"
    ]

    st.subheader("🔥 Results:")

    for i in range(5):
        n = random.choice([3,5,7,10])
        idea = topic

        title = random.choice(templates).format(n=n, idea=idea)
        hook = random.choice(hooks).format(n=n)

        st.write(f"🎬 Title: {title}")
        st.write(f"💡 Hook: {hook}")
        st.write("---")
