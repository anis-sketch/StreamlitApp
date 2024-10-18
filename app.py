import streamlit as st
import pandas as pd

st.markdown("### Hello, this my first streamlit exemple")

cols_dict = {'names' : ['snail', 'pig', 'elephant', 'rabbit',
                        'giraffe', 'coyote', 'horse'],
             'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
             'lifespan' : [2, 8, 70, 1.5, 25, 12, 28], }

source = pd.DataFrame(cols_dict)

st.write(source)

