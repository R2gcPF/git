import streamlit as st
from PIL import Image

st.title('Streamlit 超入門')
st.write('Display Image')


"""
# 章
## 節
### 項

```pyhton
import streamlit as st
import numpy as np
import pandas as pd
```

"""

img = Image.open("4.2.07.tiff")
st.image(img, caption='Sample', use_column_width=True)

