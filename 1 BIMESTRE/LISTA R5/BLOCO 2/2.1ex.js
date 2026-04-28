class Carrinho{
    constructor(){
        this._itens = []
    }

    adicionar(nome, preco, quantidade){
        this._itens.push({
            nome: nome,
            preco: preco,
            quantidade: quantidade
        })
    }

    remover(nome){
        this._itens = this._itens.filter(item => item.nome !== nome)
    }

    total(){
        let soma = 0
        for (let i = 0; i < this._itens.length; i++) {
            soma += this._itens[i].preco * this._itens[i].quantidade
        }
        return `Total: R$${soma.toFixed(2)}`
    }

    exibir(){
        let resultado = ''

        for(let i = 0; i < this._itens.length; i++){
            resultado += `${this._itens[i].quantidade}x ${this._itens[i].nome} - R$${this._itens[i].preco.toFixed(2)}\n`
        }

        return resultado
    }
}

const carrinho1 = new Carrinho

carrinho1.adicionar('Mentos', 10, 10)
carrinho1.adicionar('Pirulito', 8, 10)
carrinho1.adicionar('Trident', 3.5, 5)

carrinho1.remover('Pirulito')

console.log(carrinho1.exibir())
console.log(carrinho1.total())
