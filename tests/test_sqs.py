import boto3
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

# Configura o cliente SQS
sqs = boto3.client(
    'sqs',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION")
)

def test_sqs_connection():
    try:
        # Obtém a URL da fila (opcional, apenas para teste)
        queue_url = os.getenv("SQS_QUEUE_URL")
        print("URL da fila:", queue_url)

        # Envia uma mensagem de teste
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody="{\"test\": \"Conexão com SQS funcionando!\"}"
        )
        print("Mensagem enviada! ID:", response['MessageId'])

        # Verifica se a fila existe (teste adicional)
        sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=['All']
        )
        print("✅ Conexão com SQS bem-sucedida!")

    except Exception as e:
        print("❌ Erro na conexão com SQS:", str(e))

if __name__ == "__main__":
    test_sqs_connection()