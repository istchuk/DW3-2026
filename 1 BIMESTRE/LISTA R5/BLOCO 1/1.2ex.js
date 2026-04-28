class Produto{
    constructor(nome,preco,estoque){
        this._nome = nome
        this._preco = preco
        this._estoque = estoque
    }

    disponivel(){
        if (this._estoque > 0){
            return true
        }
        else {
            return false
        }
    }

    exibir(){
        if (this.disponivel()){
            console.log(`${this._nome} - R$${this._preco.toFixed(2)} - Em estoque`)
        } else {
            console.log(`${this._nome} - R$${this._preco.toFixed(2)} - Fora de estoque`)
        } 
    }

}

const iPad = new Produto('iPad', 8000, 0)
iPad.disponivel()
iPad.exibir()

const notebook = new Produto('Notebook', 10000, 10)
notebook.exibir()