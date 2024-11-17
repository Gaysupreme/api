from flask import Flask, jsonify, request

app = Flask(__name__)

# Função para validar CPF manualmente
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remover caracteres especiais
    
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Validar CPF com números repetidos (exemplo: 11111111111)
    if cpf == cpf[0] * len(cpf):
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0

    # Comparar os dígitos verificadores com os informados
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

@app.route('/consultar', methods=['GET'])
def consultar():
    cpf = request.args.get('cpf')

    # Valida o CPF
    if not cpf or not validar_cpf(cpf):
        return jsonify({"error": "CPF inválido ou não fornecido"}), 400

    # Simulação de dados reais (mas fictícios para exemplo)
    if cpf == "09944069400":
        resposta = {
            "consulta": {
                "dados_pessoais": {
                    "cpf": "💳 09944069400",
                    "data_nascimento": "🎂 1992-10-01",
                    "grau_qualidade": "⭐ 83",
                    "nome": "👤 ARTHUR ANTENOR BASTOS DOS SANTOS",
                    "nome_mae": "👩‍👦 SOLANGE BASTOS DOS SANTOS",
                    "nome_pai": "👨‍👦 SEBASTIAO MUNIZ DOS SANTOS",
                    "obito": "⚰️ NÃO",
                    "parto_gemelar": "👶 NÃO",
                    "raca_cor": "🎨 02",
                    "sexo": "🚻 M",
                    "vip": "💎 NÃO"
                },
                "endereco": {
                    "bairro": "🏘️ PONTAL DA BARRA",
                    "cep": "📫 57010850",
                    "logradouro": "🛣️ R DR ERNANDES BASTOS",
                    "municipio": "🌆 270430",
                    "numero": "🏠 165",
                    "uf": "🇧🇷 AL"
                },
                "nacionalidade": {
                    "municipio_nascimento": "🏙️ 270430",
                    "nacionalidade": "🌍 1",
                    "pais_nascimento": "🌏 1"
                },
                "telefones": [
                    {
                        "numero": "📱 (82) 33125507",
                        "tipo": "Tipo: 4"
                    }
                ],
                "tipo": "🔍 CPF"
            },
            "metadata": {
                "source": "🤖 @agenciei"
            }
        }
        return jsonify(resposta)
    
    return jsonify({"error": "CPF não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
