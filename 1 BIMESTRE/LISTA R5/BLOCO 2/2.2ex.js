class Placar{
    constructor(timeCasa, timeVisitante, golsCasa, golsVisitante){
        this._timeCasa = timeCasa
        this._timeVisitante = timeVisitante
        this._golsCasa = 0
        this._golsVisitante = 0
    }

    marcarGol(time){
        if (time === this._timeVisitante) {
            this._golsVisitante += 1
            return this._golsVisitante
        } else if (time === this._timeCasa) {
            this._golsCasa += 1
            return this._golsCasa
        } else {
            return console.log('Time inválido.')
        }
    }

    exibir(){
        return `${this._timeCasa} ${this._golsCasa} x ${this._golsVisitante} ${this._timeVisitante}`
    }

    resultado(){
        if (this._golsCasa > this._golsVisitante){
            return `Vitória do ${this._timeCasa}!`  
        } else if ((this._golsCasa) == (this._golsVisitante)){
            return 'Empate!'
        } else {
            return `Viória do ${this._timeVisitante}`
        }
    }
}

const jogo1 = new Placar('Midnight Fangs', 'Retrobots')

jogo1.marcarGol('Midnight Fangs')
jogo1.marcarGol('Midnight Fangs')

console.log(jogo1.exibir())
console.log(jogo1.resultado())