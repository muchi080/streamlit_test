import streamlit as st
import time


st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'start!!!!!!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ回答 1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ回答2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ回答3')
expander4 = st.expander('問い合わせ4')
expander4.write('問い合わせ回答4')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# text = st.text_input('あなたの趣味をおしえてください。')
# 'あなたの趣味:', text

# option = st.selectbox(
#     '好きな数字を選択してください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は', option, 'です'

# if st.checkbox('画像を表示する'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='ポッチャマ' , use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
#     )

# st.table(df.style.highlight_max(axis=0))
  #docs_index(api refference display_char)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139,70],
#     columns=['lat','lon']
# )
# st.map(df)
# """"
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

