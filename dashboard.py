import streamlit as st

def main():
    st.title("Cryptocurrency Dashboard")
    
    if st.button("Bitcoin"):
        st.experimental_set_query_params(page="bitcoin")
    if st.button("Ethereum"):
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
