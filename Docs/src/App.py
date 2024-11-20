import streamlit as st
from service.blob_service import upload_blob
from service.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivos - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["pdf", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Aqui você deve implementar a lógica para enviar o arquivo para o Azure Blob Storage
        blob_url = upload_to_azure(uploaded_file)  # Função fictícia para upload
        
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage!")
            credit_card_info = analyze_credit_card(blob_url)  # Função fictícia para detecção
            show_image_and_validation(blob_url, credit_card_info)
        
        else: 
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage!")
    
def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada!", use_container_width=True)
    st.write("Resultado de validação")
    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown(f"<h1 style='color: green;'>Cartão Válido<h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular do Cartão: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")        
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido<h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido, consulte seu Emissor do cartão!")

def upload_to_azure(uploaded_file):
    # Implementar a lógica de upload para o Azure Blob Storage
    return "blob_url"  # Retornar o URL do blob após o upload

def danalyze_credit_card(blob_url):
    # Implementar a lógica de detecção de informações do cartão de crédito
    return {"card_name": "Nome Exemplo", "bank_name": "Banco Exemplo", "expiry_date": "12/25"}

if __name__ == "__main__":
    configure_interface()
