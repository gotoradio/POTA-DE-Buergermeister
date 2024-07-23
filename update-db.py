import subprocess, json, time

leaders = {'date_UTC': time.strftime('%d.%m.%Y %H:%M', time.gmtime()), 'data': {}}

de_parks = json.loads(subprocess.run(["curl", "https://api.pota.app/program/parks/DE/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout)

for park in de_parks:
    leaders_park = {}
    reference = park['reference']

    stats = json.loads(subprocess.run(["curl", f'https://api.pota.app/park/leaderboard/{reference}?count=9'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout)

    print(reference)

    if len(stats['activations']) > 0:
        activation_bevor = stats['activations'][0]
        activator = [activation_bevor['callsign']]
        del stats['activations'][0]
        for activation in stats['activations']:
            if activation_bevor['count'] != activation['count']:
                break
            activator.append(activation['callsign'])
        leaders_park['activations'] = activator

        activation_bevor = stats['activator_qsos'][0]
        activator = [activation_bevor['callsign']]
        del stats['activator_qsos'][0]
        for activation in stats['activator_qsos']:
            if activation_bevor['count'] != activation['count']:
                break
            activator.append(activation['callsign'])
        leaders_park['qsos'] = activator

        leaders['data'].update({reference: leaders_park})

f = open("buergermeister.json", "w")
f.write(json.dumps(leaders))
f.close()
