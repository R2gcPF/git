import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
# st.write('DataFrame')
st.write('Display Image')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```pyhton
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.3273838, 139.3491813],
#     columns=['lat', 'lon']
# )
# # st.area_chart(df)
# # print(df)
# st.map(df)


img = Image.open("4.2.07.tiff")

st.image(img, caption='Sample', use_column_width=True)

