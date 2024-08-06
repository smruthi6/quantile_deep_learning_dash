import streamlit as st

def main():
    st.title("Cryptocurrency Dashboard")

    st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }
    .stButton > button {
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
    .stButton > button:first-child {
        background-color: #FFA07A; /* Light orange background */
    }
    .stButton > button:first-child:hover {
        background-color: #FF8C00; /* Darker orange */
    }
    .stButton > button:nth-child(2) {
        background-color: #ADD8E6; /* Light blue background */
    }
    .stButton > button:nth-child(2):hover {
        background-color: #6495ED; /* Darker blue */
    }
    </style>
    """, unsafe_allow_html=True)

    # Display buttons in a single row
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Bitcoin"):
            st.session_state.page = "bitcoin"
    with col2:
        if st.button("Ethereum"):
            st.session_state.page = "ethereum"

    # Initialize session state if not already set
    if "page" not in st.session_state:
        st.session_state.page = "main"

    # Display the appropriate page content based on the selected button
    if st.session_state.page == "bitcoin":
        import bitcoin
        bitcoin.main()
    elif st.session_state.page == "ethereum":
        import ethereum
        ethereum.main()

if __name__ == '__main__':
    main()
