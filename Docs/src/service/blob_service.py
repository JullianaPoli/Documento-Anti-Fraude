import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
import requests
from utils.Config import Config 

def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        
        blob_client.upload_blob(file, overwrite=True)
        
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {ex}")
        return None

def show_image_and_validation(blob_url):
    if blob_url:
        try:
            response = requests.get(blob_url)
            if response.status_code == 200:
                st.image(blob_url, caption="Imagem enviada!", use_container_width=True)
            else:
                st.error("Não foi possível acessar a imagem na URL fornecida.")
        except Exception as e:
            st.error(f"Ocorreu um erro ao tentar acessar a imagem: {e}")
    else:
        st.error("URL do blob não está disponível.")

def main():
    st.title("Upload de Imagem para Azure Blob Storage")
    
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_name = uploaded_file.name
        blob_url = upload_blob(uploaded_file, file_name)
        show_image_and_validation(blob_url)

if __name__ == "__main__":
    main()
