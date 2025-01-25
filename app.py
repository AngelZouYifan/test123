import streamlit as st
import random

# Load words from a txt file
try:
    with open("words.txt", "r") as file:
        words = [line.strip() for line in file.readlines() if line.strip()]
except FileNotFoundError:
    words = []

# Title and description
st.title("Random Word & Sequence Generator")
st.write("Words are loaded from the file: `words.txt` (format: Adobe, <NAME>)")

# Show current words
if words:
    n = len(words)
    st.write(str(n)+" words are loaded.")
else:
    st.warning("No words found in the file. Please ensure `words.txt` is in the correct format.")

# Button to display a random combination of 4 unique words
words_shown = 0

if st.button("Show/Hide Random Words (4)"):
    if words_shown == 1:
        words_shown = 0
        st.write("Words hided")
    elif words_shown == 0 and len(words) >= 4:
        random_combination = random.sample(words, 4)
        st.write("### Random Combination of 4 Words")
        for word in random_combination:
            st.write(word)
        words_shown = 1
    else:
        st.warning("Not enough words to generate a combination of 4. Please add more words to the file.")


# Button to display a random sequence of 3 of 1, 2, 3, 4
if st.button("Generate Random Sequence (3 of 1, 2, 3, 4)"):
    sequence = random.sample([1, 2, 3, 4], 3)
    st.write("### Random Sequence of 3")
    st.write(", ".join(map(str, sequence)))
