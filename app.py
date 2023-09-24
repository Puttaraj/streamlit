import streamlit as st

# Define a dictionary with the file names and their corresponding Google Drive links.
files = {
    "Data Exploration": "https://drive.google.com/uc?export=download&id=1et_EG89LAOxsjXCnnr-xcgH6FFHSmBX9",
    "Data Visualization": "https://drive.google.com/uc?export=download&id=1W0llDa2FO-pAwTNnm9Hphww07-n7GT9W",
    "Data Preprocessing": "https://drive.google.com/uc?export=download&id=1RA1jElF_B01Dfp0sl1lZtZ7526dverph",
    "Normalization": "https://drive.google.com/uc?export=download&id=17QMsTrMetOhsmnRBFIamH1ljAJMhz9LM",
    "Standardization": "https://drive.google.com/uc?export=download&id=1EZq6mjdfxs2LkNHjfy6Val4lj43Xy_8L",
    "Data Reduction": "https://drive.google.com/uc?export=download&id=1OZAqHFFojvgQgMnsnaS04X9lejmTM6BG",
    "Binary Logistic": "https://drive.google.com/uc?export=download&id=1fU69gRRYW2EAHtdrhVjWx26vD6rFBkFd"
}

# Streamlit app layout
st.title("My Data Analysis App")

# Display the file names and add a download link for each file
for name, link in files.items():
    st.write(f"{name}:")
    st.markdown(f"[Download {name}]( {link} )")

# Run the Streamlit app
if __name__ == "__main__":
    st.run()
