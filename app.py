# streamlit_app.py
import streamlit as st
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    st.title("Rajendra : Random Number Generator App (trial)")
    
    # Generate a random number
    random_number = generate_random_number()

    # Display the random number
    st.write(f"Your random number is: {random_number}")

if __name__ == "__main__":
    main()
