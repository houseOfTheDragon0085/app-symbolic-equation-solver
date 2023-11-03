import streamlit as st
import sympy as sym

st.title("Algebraic Equation Solver with SymPy")

st.write("Enter algebraic equations with symbolic variables for x, y, and z separately:")

# User input for the equations
equation_input_x = st.text_input("Equation for x:")
equation_input_y = st.text_input("Equation for y:")
equation_input_z = st.text_input("Equation for z:")

# Define symbolic variables
x, y, z, c1 = sym.symbols('x y z c1')

solutions_x, solutions_y, solutions_z = None, None, None

try:
    if equation_input_x:
        eq_x = sym.Eq(*sym.sympify(equation_input_x.split('=')))
        solutions_x = sym.solve(eq_x, x)

    if equation_input_y:
        eq_y = sym.Eq(*sym.sympify(equation_input_y.split('=')))
        solutions_y = sym.solve(eq_y, y)

    if equation_input_z:
        eq_z = sym.Eq(*sym.sympify(equation_input_z.split('=')))
        solutions_z = sym.solve(eq_z, z)

    st.write("Solutions:")
    if solutions_x:
        st.write(f"Solutions for x: {solutions_x}")
    if solutions_y:
        st.write(f"Solutions for y: {solutions_y}")
    if solutions_z:
        st.write(f"Solutions for z: {solutions_z}")

except Exception as e:
    st.error("Invalid Equation")
