from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analyze_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentIntelligenceClient(Config.blob_url, credential)
        
        # Iniciar a análise do documento
        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard",  # Corrigido o nome do modelo
            AnalyzeDocumentRequest(url_source=card_url)
        )
        
        result = card_info.result()
        
        # Extrair informações dos documentos analisados
        for document in result.documents:
            fields = document.fields
            
            return {
                "Card_name": fields.get('CardHolderName', {}).get('content'),
                "Card_number": fields.get('CardNumber', {}).get('content'),
                "Expiry_date": fields.get('ExpirationDate', {}).get('content'),  # Corrigido o nome da chave
                "Bank_name": fields.get('IssuingBank', {}).get('content')
            }
    
    except Exception as ex:
        print(f"Erro ao analisar o cartão de crédito: {ex}")
        return None
