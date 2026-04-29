class Carrinho{
    constructor(){
        this.itens = []
    }

    adicionar(nome, preco, quantidade){
        this.itens.push({
            nome: nome,
            preco: preco,
            quantidade: quantidade
        })
    }

    remover(nome){
        this.itens = this.itens.filter(item => item.nome !== nome)
    }

    total(){
        let soma = 0
        for (let i = 0; i < this.itens.length; i++) {
            soma += this.itens[i].preco * this.itens[i].quantidade
        }
        return `Total: R$${soma.toFixed(2)}`
    }

    exibir(){
        let resultado = ''

        for(let i = 0; i < this.itens.length; i++){
            resultado += `${this.itens[i].quantidade}x ${this.itens[i].nome} - R$${this.itens[i].preco.toFixed(2)}\n`
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
