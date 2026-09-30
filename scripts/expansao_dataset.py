import pandas as pd
import random

# 1. Carregar o dataset original (10 linhas)
df_original = pd.read_csv('dataset_emails_final-1.csv')

# 2. Dicionários de padrões de Phishing (Label 1)
phishing_senders = ['security@banco-alerta.com', 'admin@update-conta.com', 'support@netflix-verify.com', 'alert@paypal-secure.com', 'promo@oferta-relampago.com', 'premio@sorteio-vip.com']
phishing_subjects = ['Sua conta foi suspensa', 'Aviso: Login não reconhecido', 'Você ganhou um iPhone 15!', 'Ação necessária: Atualize seus dados', 'Promoção exclusiva: 90% de desconto', 'Fatura em atraso - Evite negativação']
phishing_bodies = [
    'Caro usuário, detectamos atividades suspeitas. Clique aqui para validar sua conta e evitar o bloqueio permanente.',
    'Sua assinatura expirou hoje. Atualize seus dados de pagamento imediatamente no link em anexo.',
    'Parabéns! Você foi o sorteado do mês. Para resgatar seu prêmio, preencha o formulário clicando no link abaixo.',
    'Por motivos de segurança, sua conta foi temporariamente desativada. Confirme sua identidade para restaurar o acesso.',
    'Aviso de cobrança extrajudicial. Acesse o boleto em anexo para regularizar sua situação em até 24 horas.'
]

# 3. Dicionários de padrões Legítimos (Label 0)
legit_senders = ['sales@empresa.com', 'hr@empresa.com', 'orders@loja.com', 'privacy@empresa.com', 'events@empresa.com', 'newsletter@techblog.com']
legit_subjects = ['Relatório financeiro mensal', 'Lembrete de reunião de equipe', 'Seu recibo da compra #4912', 'Novidades do mês na plataforma', 'Atualização dos termos de serviço', 'Ata da reunião técnica']
legit_bodies = [
    'Segue em anexo o relatório referente aos resultados de vendas deste mês para sua avaliação.',
    'Lembrando que nossa reunião de planejamento ocorrerá amanhã às 14h na sala principal. Compareça.',
    'Obrigado pela sua compra. O recibo da sua transação já está disponível no painel do cliente online.',
    'Confira as últimas novidades e recursos adicionados à nossa plataforma nesta nova atualização de sistema.',
    'Este é um e-mail automático para informar que atualizamos nossos termos de serviço e políticas de privacidade.'
]

# 4. Definir a proporção de forma aleatória para os 90 novos registros
num_novos_registros = 90
# Define aleatoriamente uma quantidade de phishing entre 30 e 60 registros
qtd_phishing = random.randint(30, 60) 
# O restante será de e-mails legítimos
qtd_legit = num_novos_registros - qtd_phishing

print(f"Gerando novos dados de Phishing: {qtd_phishing}")
print(f"Gerando novos dados Legítimos: {qtd_legit}")

novos_dados = []

# Gerando os registros de Phishing (1)
for _ in range(qtd_phishing):
    novos_dados.append({
        'subject': random.choice(phishing_subjects),
        'body': random.choice(phishing_bodies),
        'sender': random.choice(phishing_senders),
        'label': 1
    })

# Gerando os registros Legítimos (0)
for _ in range(qtd_legit):
     novos_dados.append({
        'subject': random.choice(legit_subjects),
        'body': random.choice(legit_bodies),
        'sender': random.choice(legit_senders),
        'label': 0
    })

# 5. Concatenar, embaralhar e exportar
df_expandido = pd.concat([df_original, pd.DataFrame(novos_dados)], ignore_index=True)

# Embaralhar (shuffle) as linhas para que os 0 e 1 fiquem bem distribuídos
df_expandido = df_expandido.sample(frac=1, random_state=42).reset_index(drop=True)

# Salvar o novo arquivo
df_expandido.to_csv('dataset_emails_expandido.csv', index=False)

print(f"\nDataset expandido com sucesso para {df_expandido.shape[0]} registros!")
print("Distribuição final das labels (incluindo as 10 originais):")
print(df_expandido['label'].value_counts())
