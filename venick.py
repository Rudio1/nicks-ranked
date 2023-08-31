import os as o
import requests as r
import psutil as u 
import json as j
import base64 as b
import keyboard
from colorama import Fore, init
import webview

init(convert=True)
dodge = []

with open('dodgelist.txt', 'r') as f:
    nigs = f.readlines()
    for x in nigs:
        x = x.strip('\n').upper()
        dodge.append(x)

dodgelist = ', '.join(dodge).upper()

o.system('cls')
print(f'{Fore.BLUE}----- / Nicks no Lobby - Guizao / -----{Fore.RESET}\n\nPressione {Fore.RED}"F9"{Fore.RESET} para fechar o programa.\nPressione {Fore.GREEN}"F6"{Fore.RESET} para abrir o OPGG dos membros. \n\nDodgelist carregada: {Fore.RED}{dodgelist}{Fore.RESET}')

def nomeschampselect():
    [x]=[[i.cmdline()[2].split('=')[1],i.cmdline()[1].split('=')[1]] for i in u.process_iter() if i.name() == 'LeagueClient.exe']
    e=list(r.get(url=f'https://127.0.0.1:{x[0]}/chat/v5/participants/champ-select',headers={'Authorization':f"Basic {b.b64encode(f'riot:{x[1]}'.encode()).decode()}",'Accept': 'application/json'},verify=r"{}\riotgames.pem".format(o.getcwd())))
    return [ i['name'] for i in j.loads(''.join(s.decode() for s in e))['participants']]

nicks_anteriores = []


while True:
    nicks_atuais = nomeschampselect()
    if keyboard.is_pressed('f9'):
        break
    else:

        try:
            nicks_str = ', '.join(nicks_atuais)
            

            if nicks_atuais != nicks_anteriores: 
                print(f'\n{Fore.YELLOW}----------------------/ NOVA QUEUE /------------------------{Fore.RESET}\n')
                for i in dodge:
                    if i in nicks_str.upper():
                        print(f'\n{Fore.RED}*Possível dodge avistado:{Fore.RESET} {i}\n')    
                    else:
                        pass
                nicks_anteriores = nicks_atuais
                print(nicks_str, '\n')

                if len(nicks_str) == 0:
                    print('Esperando a próxima champ select...\n')

                if len(nicks_str) != 0:
                    webview.create_window('OPGG dos membros do time', f'https://www.op.gg/multisearch/br?summoners={nicks_str}')
                    webview.start()

            if keyboard.is_pressed('f6'):
                if len(nicks_str) == 0:
                    print('Erro: Você não está numa champ select para abrir o OPGG.')
                    pass
                else:
                    print(f'Carregando op.gg de: {nicks_str}.')
                    webview.create_window('OPGG dos membros do time', f'https://www.op.gg/multisearch/br?summoners={nicks_str}')
                    webview.start()

        except ValueError:
            print('Client não aberto.')
            input('')