import streamlit as st
# import pandas as pd
from PIL import Image
import time

st.title('test2')
img = Image.open('https://github.com/R2gcPF/git/blob/main/app/4.2.07.tiff')

'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done'
st.image(img)