import pyautogui as pa
import time
import pandas as pd

df = pd.read_excel('CADASTRAR.xlsx', dtype=str)

pa.PAUSE = 1

pa.hotkey('win', 't')
pa.press('ENTER')
time.sleep(5)

for index, row in df.iterrows():
    pa.hotkey('alt', 'n')
    pa.press('tab') 
    pa.write(str(row['CPF']).zfill(11))
    pa.press('ENTER')
    pa.write(row['Promotor'])
    pa.press('tab')
    pa.press('3')
    pa.press('tab')
    pa.write(str(row['CPF']).zfill(11))
    pa.press('tab')
    pa.write(str(row['Nome Fantasia']))
    pa.press('tab', presses=4)
    pa.write(str(row['CEP']).zfill(8))
    pa.press('tab')
    pa.write(str(row['Endereço']))
    pa.press('tab')
    pa.write(str(row['Bairro']))
    pa.press('tab', presses=2)
    pa.write(str(row['Cidade']))
    pa.press('tab')
    pa.write(str(row['UF']))
    pa.press('tab')
    pa.write(str(row['Telefone']))
    pa.press('tab', presses=2)
    pa.write(str(row['Email']))
    pa.press('tab', presses=12)
    pa.write(str(row['BANCK']))
    pa.press('tab')
    pa.write('c')
    pa.press('tab')
    pa.write(str(row['Agencia']))
    pa.press('tab')
    pa.write(str(row['Conta+Digito']))
    pa.press('tab', presses=19)
    pa.write('070002')
    pa.press('tab', presses=21)
    pa.press('right')
    pa.click(x=400, y=410)
    pa.write('2110200001')
    pa.hotkey('alt', 's')

 
        