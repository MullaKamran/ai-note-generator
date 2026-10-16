from structured import get_structured_notes
import streamlit as st
st.title("AI Notes Generator")
notes=st.text_area("Enter your notes here:", height=200)

if st.button("Generate"):
    if len(notes.strip()) < 15:
        
        st.warning("Please enter valid notes before generating.")
        st.stop()

    with st.spinner("Generating..."):
        data = get_structured_notes(notes)

    if data:
        st.subheader("Summary")
        st.write(data["summary"])
        st.subheader("Key Points")
        for point in data["key_points"]:
            st.write(f"- {point}")
    else:
        st.error("Failed to generate structured notes. Please try again.")