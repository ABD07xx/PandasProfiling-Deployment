import streamlit as st 
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

st.title("Pandas Profiling in Streamlit!!!")

upload_file = st.file_uploader("Upload Data",type=["csv"])
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.dataframe(df)
    profile = ProfileReport(df)
    st_profile_report(profile)
    f_pn=profile.to_file("Analysis.html")
    if st.button('Yes'):
        f_pn

