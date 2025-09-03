import streamlit as st
import pandas as pd
from datetime import datetime

# -----------------------------
# App Title
# -----------------------------
st.set_page_config(page_title="Heritage Hub", layout="wide")
st.title("🏛️ Heritage Hub – Local History Collector")
st.write("Share and explore local stories, legends, and cultural heritage.")

# -----------------------------
# Session state for storage
# -----------------------------
if "stories" not in st.session_state:
    st.session_state["stories"] = []

# -----------------------------
# Input Form
# -----------------------------
st.header("✍️ Submit Your Story")

with st.form("story_form"):
    name = st.text_input("Your Name (optional)")
    location = st.text_input("Location (village, town, or city)")
    story_text = st.text_area("Write your story or fact")
    story_audio = st.file_uploader(
        "Or upload an audio recording (MP3/WAV)", type=["mp3", "wav"]
    )
    submitted = st.form_submit_button("Submit")

    if submitted:
        if story_text.strip() == "" and story_audio is None:
            st.warning("⚠️ Please enter a story or upload audio.")
        else:
            st.session_state["stories"].append(
                {
                    "name": name if name else "Anonymous",
                    "location": location,
                    "story_text": story_text,
                    "story_audio": story_audio,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            st.success("✅ Story submitted successfully!")

# -----------------------------
# Display Archive
# -----------------------------
st.header("📚 Community Story Archive")

if len(st.session_state["stories"]) == 0:
    st.info("No stories collected yet. Be the first to share!")
else:
    for idx, story in enumerate(st.session_state["stories"], start=1):
        with st.expander(
            f"📖 Story {idx} from {story['location']} ({story['timestamp']})"
        ):
            st.write(f"👤 **{story['name']}**")
            if story["story_text"]:
                st.write(story["story_text"])
            if story["story_audio"] is not None:
                st.audio(story["story_audio"], format="audio/mp3")
