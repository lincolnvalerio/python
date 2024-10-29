import pyautogui
from time import sleep

pyautogui.click(680,441,duration=0.1)

pyautogui.click(702, 386, duration=0.1)
pyautogui.write('lin')

# 2 - Clica e digita a senha
pyautogui.click(694, 411, duration=0.1)
pyautogui.write('123456')

# 3 - Clica no botão de entrar
pyautogui.click(593, 443, duration=0.1)

# Passos manuais
# 1 - Clica e digita o usuário
pyautogui.click(702, 386, duration=0.1)
pyautogui.write('lin')

# 2 - Clica e digita a senha
pyautogui.click(694, 411, duration=0.1)
pyautogui.write('123456')

# 3 - Clica no botão de entrar
pyautogui.click(593, 443, duration=0.1)

# 4 - Extrair e registrar cada produto do arquivo
with open('produtos.txt', 'r') as file:
    for linha in file:
        produto, quantidade, preco = linha.strip().split(',')

        # 1 - Clica no campo de produto e digita o nome
        pyautogui.click(422, 370, duration=0.1)
        pyautogui.write(produto)

        # 2 - Clica no campo de quantidade e digita a quantidade
        pyautogui.click(411, 399, duration=0.1)
        pyautogui.write(quantidade)

        # 3 - Clica no campo de preço e digita o valor
        pyautogui.click(409, 425, duration=0.1)
        pyautogui.write(preco)

        # 4 - Clica no botão para registrar o produto
        pyautogui.click(306, 578, duration=0.1)

        # Espera um pouco antes de registrar o próximo produto
        sleep(0.1)
