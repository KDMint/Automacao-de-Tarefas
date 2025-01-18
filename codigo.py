#pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.7

#ABRIR O NAVEGADOR
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3)

#PESQUISAR O SITE E ENTRAR
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(1)

#FAZER LOGIN
pyautogui.click(x=811, y=510)
pyautogui.write('email_exemplo@gmail.com')
pyautogui.press('tab')
pyautogui.write('123123')
pyautogui.press('tab')
pyautogui.press('enter')

#pip install pandas openpyxl
import pandas

#armazenando a base de dados na variavel 'tabela'
tabela = pandas.read_csv('produtos.csv')
print(tabela)

time.sleep(1)

for linha in tabela.index:
    #clica no primeiro campo
    pyautogui.click(x=745, y=368)

    #codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    #categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    #preço unitário
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    #custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #observação
    obs = str(tabela.loc[linha, 'obs'])

    #nan = não preenchido
    if obs != 'nan': 
        pyautogui.write(obs)

    pyautogui.press('tab')

    #clica no botão enviar
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')


    pyautogui.press('PageUp')
    