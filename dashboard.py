import streamlit as st

def main():
    st.title("Cryptocurrency Dashboard")
    st.markdown("""
    <style>
    .button {
        background-color: #4CAF50; /* Green background */
        border: none; /* Remove borders */
        color: white; /* White text */
        padding: 15px 32px; /* Some padding */
        text-align: center; /* Centered text */
        text-decoration: none; /* Remove underline */
        display: inline-block; /* Get the block-level display */
        font-size: 16px; /* Increase font size */
        margin: 4px 2px; /* Some margin */
        cursor: pointer; /* Pointer/hand icon */
        border-radius: 12px; /* Rounded corners */
    }
    .button:hover {
        background-color: #45a049; /* Darker green */
    }
    </style>
    """, unsafe_allow_html=True)

    if st.markdown('<a href="?page=bitcoin" class="button">Bitcoin</a>', unsafe_allow_html=True):
        st.experimental_set_query_params(page="bitcoin")
    if st.markdown('<a href="?page=ethereum" class="button">Ethereum</a>', unsafe_allow_html=True):
        st.experimental_set_query_params(page="ethereum")

    page = st.experimental_get_query_params().get("page", ["main"])[0]
    
    if page == "bitcoin":
        import bitcoin
        bitcoin.main()
    elif page == "ethereum":
        import ethereum
        ethereum.main()

if __name__ == '__main__':
    main()
