# Core Pkgs
import streamlit as st 
import pandas as pd
from PIL import Image

# DB Mgmt
import sqlite3 
#conn = sqlite3.connect('data/world.sqlite')
conn = sqlite3.connect('data/chinook.db')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 




def main():
	# Use the full page instead of a narrow central column
	st.set_page_config(layout="wide")
	html_temp = """
	<div style='background-color:orangered;'>
	<p style='color:white;font-size:50px;padding:10px'>SQL Playground</p></div>
	"""
	st.markdown(html_temp, True)

	menu = ['Home', 'About']
	choice = st.sidebar.radio("Menu",menu)

	if choice == "Home":
		st.header("HomePage")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			
			# Schema Diagram
			with st.expander("Schema Diagram"):
				image = Image.open("data/schema_diagram.JPG")
				st.image(image, caption="Schema Diagram")
			
			
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)

				with st.expander("Display Result"):
					query_df = pd.DataFrame(query_results, columns=[x[0] for x in c.description])
					st.dataframe(query_df)


	else:
		st.header("About")
		st.markdown("A simple app to play and experiment with SQL commands")
		st.markdown("Built with :heart: by Soumya Banerjee")
		st.markdown(":email:*banerjeesoumya15@gmail.com*")





if __name__ == '__main__':
	main()