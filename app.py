import streamlit as st

# Set up the title for the calculator
st.title("Simple Calculator")

# Input fields for numbers
number1 = st.number_input("Enter the first number:", value=0.0)
number2 = st.number_input("Enter the second number:", value=0.0)

# Dropdown for selecting an operation
operation = st.selectbox("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = number1 + number2
        st.write(f"The result of addition is: {result}")
    elif operation == "Subtract":
        result = number1 - number2
        st.write(f"The result of subtraction is: {result}")
    elif operation == "Multiply":
        result = number1 * number2
        st.write(f"The result of multiplication is: {result}")
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
            st.write(f"The result of division is: {result}")
        else:
            st.write("Error: Division by zero is not allowed.")
