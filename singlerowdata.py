import streamlit as st
from streamlit import session_state as ss
import pandas as pd

st.set_page_config(page_title="Page Title", layout="wide")



hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,

    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.header("Single Record Selection with Sorting and Export to Excle")

def mpg_change():
    edited_rows: dict = ss.mpg['edited_rows']
    df4 =   pd.DataFrame(edited_rows) 
    rowco = df4.shape[0]
    if rowco>0: 
        ss.selected_row_index = next(iter(edited_rows))
    
        
    ss.df1.loc[ss.df1['selected'], 'selected'] = False
    update_dict = {idx: values for idx, values in edited_rows.items()}
    ss.df1.update(pd.DataFrame.from_dict(update_dict, orient='index'))

if 'selected_row_index' not in ss:
    ss.selected_row_index = None

@st.cache_data
def get_data(nrows):
    url = 'https://raw.githubusercontent.com/Munees11/Auto-MPG-prediction/master/Scripts/auto_mpg_dataset.csv'
    return pd.read_csv(url, nrows=nrows)

if 'df1' not in ss:
    ss.df1 = get_data(10)
    ss.df1['selected'] = [False] * len(ss.df1)
    ss.df1 = ss.df1[['cylinders', 'car_name', 'mpg', 'selected']]

st.markdown('### Master Table')
with st.container(border=True):
        edf = st.data_editor(
            ss.df1,
             num_rows="dynamic",
            hide_index=True,
            on_change=mpg_change,
            key='mpg',
            use_container_width=True
        )



st.subheader(f'Detail Table')
selected_indices = ss.selected_row_index

if selected_indices == None:
        st.write("Muhammad is the best ")
else :
        df3 = pd.DataFrame(edf)
        dfm = df3.iloc[[selected_indices]]
        #st.dataframe(dfm)
        st.data_editor(dfm,
             num_rows="dynamic", hide_index=True)
