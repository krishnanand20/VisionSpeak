import streamlit as st
import pandas as pd
import numpy as np

st.write("Got lots of data? Great! Streamlit can show [dataframes](https://docs.streamlit.io/develop/api-reference/data) with hundred thousands of rows, images, sparklines – and even supports editing! ✍️")

num_rows = st.slider("Number of rows", 1, 10000, 500)
np.random.seed(42)
data = []
for i in range(num_rows):
    data.append(
        {
            "Preview": f"https://picsum.photos/400/200?lock={i}",
            "Views": np.random.randint(0, 1000),
            "Active": np.random.choice([True, False]),
            "Category": np.random.choice(["🤖 LLM", "📊 Data", "⚙️ Tool"]),
            "Progress": np.random.randint(1, 100),
        }
    )
data = pd.DataFrame(data)

# Display the data with appropriate formatting
if st.checkbox("Enable editing"):
    edited_data = st.experimental_data_editor(data, use_container_width=True)
else:
    # Render the dataframe with HTML for the "Preview" column
    def render_html_table(df):
        html = df.to_html(
            escape=False,
            formatters={
                "Preview": lambda x: f'<img src="{x}" width="100">',
                "Progress": lambda x: f'{x}%',
            },
        )
        return html

    st.write(render_html_table(data), unsafe_allow_html=True)