import streamlit as st
import pandas as pd
import numpy as np


def get_rand_df():
    lat = np.random.randint(-90, 90)
    lon = np.random.randint(-180, 180)
    df = pd.DataFrame({'LAT':[lat], 'LON':[lon]})
    return df

def main():
    df = get_rand_df()
    # c_left, c_right = st.columns(2)
    st.title(f'ENTITY {df["LAT"][0]} {df["LON"][0]}')
    # with c_left:
    btn = st.button('RELOAD')
    # with c_right:
        # btn2 = st.button('RELOAD2')
    map_main = st.map(df)
    map_sub = st.map(df, zoom=0)
    # c_right.map_sub = st.map(df, zoom=0)
    if btn:
        df = get_rand_df()

if __name__ == '__main__':
    main()