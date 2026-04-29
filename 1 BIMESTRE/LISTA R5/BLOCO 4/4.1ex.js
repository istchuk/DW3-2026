class Cliente{
    constructor(nome, email){
        this.nome = nome
        this.email = email
    }

    exibir(){
        return `${this.nome} <${this.email}>`
    }
}

class Pedido {
    constructor(id, cliente) {
        this.id = id;
        this.cliente = cliente
        this.itens = [];
        this.status = "aberto"
    }

    adicionarItem(descricao, valor) {
        this.itens.push({ descricao, valor })
    }

    total() {
        let soma = 0;
        for (let item of this.itens) {
            soma += item.valor;
        }
        return soma;
    }

    fechar() {
        this.status = "fechado"
    }

    exibir() {
        console.log(`Pedido #${this.id}`)
        console.log(`Cliente: ${this.cliente.exibir()}`)
        console.log(`Status: ${this.status}`)
        console.log("Itens:")

        for (let item of this.itens) {
            console.log(`- ${item.descricao}: R$ ${item.valor}`)
        }

        console.log(`Total: R$ ${this.total()}`)
    }
}

const cliente = new Cliente("Ana", "ana@email.com")

const pedido = new Pedido(1, cliente)

pedido.adicionarItem("Notebook", 3500)
pedido.adicionarItem("Mouse", 150)

pedido.fechar()
pedido.exibir()