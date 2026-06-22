import streamlit as st
import pandas as pd
from scraper import get_books

st.set_page_config(
    page_title="Book Price Tracker",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Price Tracker")
st.write("Search books scraped from BooksToScrape.")

@st.cache_data
def load_data():
    return get_books()

books = load_data()
st.write(f"Books scraped: {len(books)}")

df = pd.DataFrame(books)

search = st.text_input("🔍 Search Book")

# Pagination settings
PAGE_SIZE = 20

# Initialize session state for current page
if "current_page" not in st.session_state:
    st.session_state.current_page = 1

# Reset page to 1 if search term changes
if "last_search" not in st.session_state:
    st.session_state.last_search = ""

if search != st.session_state.last_search:
    st.session_state.current_page = 1
    st.session_state.last_search = search

if search:
    df = df[df["Title"].str.contains(search, case=False)]

# Calculate total pages
total_books = len(df)
total_pages = max(1, (total_books - 1) // PAGE_SIZE + 1)

# Adjust current page if it exceeds total pages
if st.session_state.current_page > total_pages:
    st.session_state.current_page = total_pages

# Slice dataframe for the current page
start_idx = (st.session_state.current_page - 1) * PAGE_SIZE
end_idx = start_idx + PAGE_SIZE
page_df = df.iloc[start_idx:end_idx]

st.dataframe(page_df, use_container_width=True)

# Pagination buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅ Previous", disabled=st.session_state.current_page == 1, use_container_width=True):
        st.session_state.current_page -= 1
        st.rerun()

with col2:
    st.markdown(
        f"<p style='text-align: center; font-size: 1.1rem; font-weight: 500; margin-top: 5px;'>Page {st.session_state.current_page} of {total_pages}</p>",
        unsafe_allow_html=True
    )

with col3:
    if st.button("Next ➡", disabled=st.session_state.current_page == total_pages, use_container_width=True):
        st.session_state.current_page += 1
        st.rerun()

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="books.csv",
    mime="text/csv"
)

st.success(f"Found {len(df)} books")

