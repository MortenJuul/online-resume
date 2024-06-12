import streamlit as st
import extra_streamlit_components as stx
from pages import home

# Import the homepage module

# Create the app
def main():
    return stx.Router({"Home": home.main})

# # Add the homepage route
# app.add_route("/", home)

# Run the app
if __name__ == "__main__":
    app = main()