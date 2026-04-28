class Aluno{
    constructor(nome, notas){
        this._nome = nome
        this._notas = []
    }

    adicionarNota(nota){
        this._notas.push(nota)
    }

    calcularMedia(){
        let soma = 0    
        for (let i = 0; i < this._notas.length; i++){
            soma += this._notas[i]
        }

        const media = soma / this._notas.length

        return media
    }

    situacao(){
        const media = this.calcularMedia()

        if (this._notas.length === 0) return 0
        if (media >= 6){
            return 'Aprovado'
        } else {
            return 'Reprovado'
        }
    }

    exibir(){
        console.log(`${this._nome} | Média: ${this.calcularMedia().toFixed(2)} | Situação: ${(this.situacao())}`)
    }

}

const gabriel = new Aluno('Gabriel')

gabriel.adicionarNota(3)
gabriel. adicionarNota(6)
gabriel.adicionarNota(10)

gabriel.exibir()