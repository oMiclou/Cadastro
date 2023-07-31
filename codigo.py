#Entrar no sistema
#Fazer login
#Importar base de produtos
#Cadastrar um produto
#Repetir o processo

import pyautogui as pa
import pandas as pd
import time

pa.PAUSE = 0.35

pa.press("win")
pa.write("chrome")
pa.press("enter")
time.sleep(1)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(5)

pa.click(x=912, y=391)

pa.write("vitortosse@gmail.com")
pa.press("tab")
pa.write("M1nh4S3nh4")
pa.click(x=940, y=553)
time.sleep(3.5)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
  print (linha)
  pa.click(x=702, y=278)
  pa.PAUSE = 0.3
  codigo = tabela.loc[linha, "codigo"]

  pa.write(str(codigo))
  pa.press("tab")

  pa.write(str(tabela.loc[linha, "marca"]))
  pa.press("tab")
  pa.write(str(tabela.loc[linha, "tipo"]))
  pa.press("tab")
  pa.write(str(tabela.loc[linha, "categoria"]))
  pa.press("tab")
  pa.write(str(tabela.loc[linha, "preco_unitario"]))
  pa.press("tab")
  pa.write(str(tabela.loc[linha, "custo"]))
  pa.press("tab")

  obs = tabela.loc[linha, "obs"]
  if not pd.isna(obs):
    pa.write(str(tabela.loc[linha, "obs"]))
  pa.press("tab")
  pa.press("enter")

  pa.scroll(5000)

