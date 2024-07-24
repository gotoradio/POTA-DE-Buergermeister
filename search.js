const CallInput = document.getElementById('callsignInput');
CallInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        search()
    }
});

function search(){
    let mayor = false;

    fetch('https://raw.githubusercontent.com/gotoradio/POTA-DE-Buergermeister/main/buergermeister.json').then(function(response){
        return response.json();
    }).then(function(stats){

        result.innerHTML = `Daten stand: ${stats['date_UTC']} UTC\n\n`;
        const call = document.getElementById('callsignInput').value;

        stats = stats['data'];

        for (let park in stats) {
            if (stats[park]['activations'].includes(call)) {
                mayor = true;
                for (let i = 0; i < stats[park]['activations'].length; i++) {
                    if (stats[park]['activations'][i] === call) {
                        if (i === 0) {
                            if (stats[park]['qsos'].includes(call)) {
                                for (let j = 0; j < stats[park]['qsos'].length; j++) {
                                    if (stats[park]['qsos'][j] === call) {
                                        if (j === 0) {
                                            result.innerHTML += `Bürgermeister per Aktivierungen und QSOs in ${park}\n`;
                                        } else {
                                            result.innerHTML += `Bürgermeister per Aktivierungen und Stellvertretener Bürgermeister per QSOs in ${park}\n`;
                                        }
                                    }
                                }
                            } else {
                                result.innerHTML += `Bürgermeister per Aktivierungen in ${park}\n`;
                            }
                        } else {
                            if (stats[park]['qsos'].includes(call)) {
                                for (let j = 0; j < stats[park]['qsos'].length; j++) {
                                    if (stats[park]['qsos'][j] === call) {
                                        if (j === 0) {
                                            result.innerHTML += `Stellvertretener Bürgermeister per Aktivierungen und Bürgermeister per QSOs in ${park}\n`;
                                        } else {
                                            result.innerHTML += `Stellvertretener Bürgermeister per Aktivierungen und QSOs in ${park}\n`;
                                        }
                                    }
                                }
                            } else {
                                result.innerHTML += `Stellvertretener Bürgermeister per Aktivierungen in ${park}\n`;
                            }
                        }
                    }
                }
            }

            if (stats[park]['qsos'].includes(call) && !stats[park]['activations'].includes(call)) {
                mayor = true;
                for (let i = 0; i < stats[park]['qsos'].length; i++) {
                    if (stats[park]['qsos'][i] === call) {
                        if (i === 0) {
                            result.innerHTML += `Bürgermeister per QSOs in ${park}\n`;
                        } else {
                            result.innerHTML += `Stellvertretener Bürgermeister per QSOs in ${park}\n`;
                        }
                    }
                }
            }
        }

        if (!mayor) {
            result.innerHTML += 'Kein Bürgermeister Status. Ist das Rufzeichen großgeschrieben?\n';
        }
    }).catch(function(error){
        result.innerHTML = `Etwas ist schiefgelaufen!`;
    })
}
