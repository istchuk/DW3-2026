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
            console.log(`${this._nome} - ${this._preco} - estoque disponível`)
        } else {
            console.log(`${this._nome} - ${this._preco} - estoque indisponível`)
        } 
    }

}

const iPad = new Produto('iPad', 'R$8000', 0)
console.log(iPad.disponivel())
console.log(iPad.exibir())

const notebook = new Produto('Notebook', 'R$10000', 10)
console.log(notebook.exibir())