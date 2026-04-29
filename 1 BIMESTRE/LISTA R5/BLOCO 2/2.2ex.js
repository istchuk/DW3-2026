class Placar{
    constructor(timeCasa, timeVisitante, golsCasa, golsVisitante){
        this.timeCasa = timeCasa
        this.timeVisitante = timeVisitante
        this.golsCasa = 0
        this.golsVisitante = 0
    }

    marcarGol(time){
        if (time === this.timeVisitante) {
            this.golsVisitante += 1
            return this.golsVisitante
        } else if (time === this.timeCasa) {
            this.golsCasa += 1
            return this.golsCasa
        } else {
            return console.log('Time inválido.')
        }
    }

    exibir(){
        return `${this.timeCasa} ${this.golsCasa} x ${this.golsVisitante} ${this.timeVisitante}`
    }

    resultado(){
        if (this.golsCasa > this.golsVisitante){
            return `Vitória do ${this.timeCasa}!`  
        } else if ((this.golsCasa) == (this.golsVisitante)){
            return 'Empate!'
        } else {
            return `Viória do ${this.timeVisitante}`
        }
    }
}

const jogo1 = new Placar('Midnight Fangs', 'Retrobots')

jogo1.marcarGol('Midnight Fangs')
jogo1.marcarGol('Midnight Fangs')

console.log(jogo1.exibir())
console.log(jogo1.resultado())