{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyMqpFtcCWa5snaYMLbph0Qb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Patrickcard/Imersao_IA_Alura_Google/blob/main/Chatbot_Para_Artistas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "D7H9FZz5kfwh"
      },
      "outputs": [],
      "source": [
        "!pip install -q -U google-generativeai\n",
        "\n",
        "\n",
        "import google.generativeai as genai\n",
        "\n",
        "GOOGLE_API_KEY='AIzaSyChFkaWPj6hf4TqG1UC_zSYk6QzRaqh2CU'\n",
        "genai.configure(api_key=GOOGLE_API_KEY)\n",
        "\n",
        "generation_config = {\n",
        "    \"candidate_count\": 1,\n",
        "    \"temperature\": 0.5,\n",
        "}\n",
        "\n",
        "\n",
        "safety_settings = {\n",
        "    \"HARASSMENT\": \"BLOCK_NONE\",\n",
        "    \"HATE\": \"BLOCK_NONE\",\n",
        "    \"SEXUAL\": \"BLOCK_NONE\",\n",
        "    \"DANGEROUS\": \"BLOCK_NONE\",\n",
        "}\n",
        "\n",
        "\n",
        "model = genai.GenerativeModel(model_name=\"gemini-1.0-pro\",\n",
        "                              generation_config=generation_config,\n",
        "                              safety_settings= safety_settings)\n",
        "\n",
        "#Iniciar a conversa\n",
        "def start_chat():\n",
        "  chat = model.start_chat(history = [])\n",
        "  return chat\n",
        "\n",
        "\n",
        "#Entrada do usuário e obter a resposta do chatbot\n",
        "def get_response(chat, user_input):\n",
        "  response = chat.send_message(user_input)\n",
        "  return response.text\n",
        "\n",
        "\n",
        "#função principal do chatbot\n",
        "def main():\n",
        "  print(\"Seja bem vindo! Serei seu amigo em suas criações artisticas. Vamos começar.\",\"\\n\")\n",
        "  print(\"Digite 'sair' a qualquer momento para encerrar a conversa.\",\"\\n\")\n",
        "  print(\"Como posso ajuda-lo hoje?\",\"\\n\")\n",
        "\n",
        "chat = start_chat()\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  main()\n",
        "\n",
        "\n",
        "while True:\n",
        "  user_input= input(\"Você: \")\n",
        "  if user_input.lower() == \"sair\":\n",
        "    print(\"Espero ter ajudado em sua jornada artistica. Até mais!\")\n",
        "    break\n",
        "\n",
        "  response = get_response(chat, user_input)\n",
        "\n",
        "  print(\"Chatbot: \", response)\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}