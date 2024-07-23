import subprocess, json

mayor = False

stats = json.loads(subprocess.run(["curl", "https://raw.githubusercontent.com/gotoradio/POTA-DE-Buergermeister/main/buergermeister.json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout)
print(f'''Daten stand: {stats['date_UTC']} UTC''')
stats = stats['data']
call = input('Zu suchendes Rufzeichen: ')

for park in stats:
    if call in stats[park]['activations']:
        mayor = True
        for i in range(len(stats[park]['activations'])):
            if stats[park]['activations'][i] == call:
                if i == 0:
                    if call in stats[park]['qsos']:
                        for i in range(len(stats[park]['qsos'])):
                            if stats[park]['qsos'][i] == call:
                                if i == 0:
                                    print(f'Bürgermeister per Aktivierungen und QSOs in {park}')
                                else:
                                    print(f'Bürgermeister per Aktivierungen und Stellvertretener Bürgermeister per QSOs in {park}')
                    else:
                        print(f'Bürgermeister per Aktivierungen in {park}')
                else:
                    if call in stats[park]['qsos']:
                        for i in range(len(stats[park]['qsos'])):
                            if stats[park]['qsos'][i] == call:
                                if i == 0:
                                    print(f'Stellvertretener Bürgermeister per Aktivierungen und Bürgermeister per QSOs in {park}')
                                else:
                                    print(f'Stellvertretener Bürgermeister per Aktivierungen und QSOs in {park}')
                    else:
                        print(f'Stellvertretener Bürgermeister per Aktivierungen in {park}')


    if call in stats[park]['qsos'] and not call in stats[park]['activations']:
        mayor = True
        for i in range(len(stats[park]['qsos'])):
            if stats[park]['qsos'][i] == call:
                if i == 0:
                    print(f'Bürgermeister per QSOs in {park}')
                else:
                    print(f'Stellvertretener Bürgermeister per QSOs in {park}')

if mayor == False:
    print('Kein Bürgermeister Status. Ist das Rufzeichen großgeschrieben?')
