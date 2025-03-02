import streamlit as st

st.title("Unit Convertor")
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value  # If units are the same

def main():
    st.title("Unit Converter")
    st.sidebar.header("Choose Conversion Type")
    conversion_type = st.sidebar.selectbox("Conversion Type", ["Length", "Weight", "Temperature"])
    
    if conversion_type == "Length":
        units = ["meters", "kilometers", "miles", "feet", "inches"]
        st.header("Length Converter")
        value = st.number_input("Enter Value:", min_value=0.0)
        from_unit = st.selectbox("From:", units)
        to_unit = st.selectbox("To:", units)
        if st.button("Convert"):
            result = length_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    
    elif conversion_type == "Weight":
        units = ["grams", "kilograms", "pounds", "ounces"]
        st.header("Weight Converter")
        value = st.number_input("Enter Value:", min_value=0.0)
        from_unit = st.selectbox("From:", units)
        to_unit = st.selectbox("To:", units)
        if st.button("Convert"):
            result = weight_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    
    elif conversion_type == "Temperature":
        units = ["Celsius", "Fahrenheit"]
        st.header("Temperature Converter")
        value = st.number_input("Enter Value:")
        from_unit = st.selectbox("From:", units)
        to_unit = st.selectbox("To:", units)
        if st.button("Convert"):
            result = temperature_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()