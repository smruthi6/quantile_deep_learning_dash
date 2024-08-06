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
    .button-orange {
        background-color: #FFA07A; /* Light orange background */
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
    .button-orange:hover {
        background-color: #FF8C00; /* Darker orange */
    }
    .button-blue {
        background-color: #ADD8E6; /* Light blue background */
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
    .button-blue:hover {
        background-color: #6495ED; /* Darker blue */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="button-container">'
                '<a href="?page=bitcoin" class="button-orange">Bitcoin</a>'
                '<a href="?page=ethereum" class="button-blue">Ethereum</a>'
                '</div>', unsafe_allow_html=True)

    page = st.experimental_get_query_params().get("page", ["main"])[0]
    
    if page == "bitcoin":
        import bitcoin
        bitcoin.main()
    elif page == "ethereum":
        import ethereum
        ethereum.main()
if __name__ == '__main__':
    main()
