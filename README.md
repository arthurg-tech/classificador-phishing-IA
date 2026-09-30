# Sistema de Classificação de E-mails com IA (Detecção de Phishing)

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido como o desafio final do Bootcamp "Analista em Segurança da Informação e Cibersegurança AI Expert". O objetivo principal é consolidar e aplicar os conhecimentos adquiridos em Processamento de Linguagem Natural (NLP) e Machine Learning para criar um sistema capaz de identificar e-mails de phishing e separá-los de e-mails legítimos.

## 🏢 O Cenário (Enunciado)
O desenvolvimento simulou a atuação profissional para a empresa fictícia **SecureMail Corp.**, que é especializada em soluções de segurança para e-mails corporativos. Devido a um aumento significativo em ataques de phishing direcionados aos clientes da empresa nos últimos meses, a missão foi arquitetar um sistema automatizado de classificação utilizando Inteligência Artificial para proteger os usuários contra possíveis ataques cibernéticos.

## 🗂️ Estrutura do Repositório
*   `notebook_classificacao_emails.ipynb`: Arquivo principal executado no Google Colab contendo todo o pipeline de Machine Learning (ingestão, pré-processamento, treinamento e avaliação).
*   `expansao_dataset.py`: Script Python desenvolvido para realizar *Data Augmentation*, expandindo a base de dados inicial (de 10 registros para 100) de forma automatizada e randomizada para garantir volume suficiente para o treinamento da IA.
*   `dataset_emails_expandido.csv`: Base de dados final gerada pelo script, contendo colunas como `subject`, `body`, `sender` e `label` (onde 0 indica e-mail legítimo e 1 indica phishing).
*   `Relatorio_Tecnico.pdf`: Documentação detalhada explicando as razões por trás das escolhas técnicas de pré-processamento, seleção de modelo, métricas de avaliação e possíveis aplicações práticas.

## ⚙️ Metodologia e Tecnologias Aplicadas

**1. Pré-processamento de Dados (NLP)**
Utilizando a biblioteca `spaCy` (modelo `pt_core_news_sm`), o texto dos e-mails passou por limpeza estrutural, remoção de *stopwords* e lematização. A conversão do texto em matrizes numéricas foi realizada através da técnica **TF-IDF** (`TfidfVectorizer`). Os dados foram separados em conjuntos de treino e teste de forma estratificada para evitar vazamento de dados (*data leakage*).

**2. Desenvolvimento do Modelo**
O algoritmo escolhido para a tarefa de classificação textual foi o **Naive Bayes** (`MultinomialNB`), altamente eficiente para análise probabilística de vocabulário em detecção de spam e phishing.

**3. Avaliação de Performance**
O modelo foi avaliado com base nas seguintes métricas estipuladas pelo desafio:
*   **Acurácia:** Percentual de previsões corretas feitas pelo modelo.
*   **Precisão:** Proporção de verdadeiros positivos entre as previsões positivas.
*   **Recall:** Proporção de verdadeiros positivos entre todos os casos positivos (foco principal do projeto para evitar falsos negativos).
*   **F1-Score:** Média harmônica entre precisão e recall.
*   **Matriz de Confusão:** Visualização gráfica da performance em termos de acertos e erros.

## 🚀 Resultados Alcançados
O modelo final obteve uma **Acurácia de 96%** e um **Recall de 100%** na identificação de tentativas de phishing na carga de teste. O sistema provou ser altamente seguro para integração em *gateways* de e-mail corporativo, barrando todas as ameaças com uma margem mínima e aceitável de falsos positivos (2 e-mails legítimos enviados para verificação manual).

## 🛠️ Como Executar
1. Clone este repositório.
2. Caso deseje gerar novos dados de treinamento, execute `python expansao_dataset.py`.
3. Faça o upload do arquivo `dataset_emails_expandido.csv` para a pasta `/content` no Google Colab.
4. Execute as células do notebook para visualizar o pipeline de limpeza, vetorização e o gráfico final da Matriz de Confusão.
