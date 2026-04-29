class ContaBancaria{
    constructor(nome, saldoInicial){
        this.titular = nome
        this.saldo = saldoInicial
    }

    depositar(valor){
        this.saldo += valor
    }

    sacar(valor){
        if (valor > this.saldo){
            console.log("Saldo insuficiente")
            return
        }
        else{
           this.saldo -= valor
        }
    }

    exibirSaldo(){
        return `Titular: ${this.titular} | Saldo: ${this.saldo.toFixed(2)}`
    }
}

const joao = new ContaBancaria('João',100)
joao.depositar(5000)


const gabriel = new ContaBancaria('Gabriel', 1000)
gabriel.sacar(10000)


console.log(gabriel.exibirSaldo())
console.log(joao.exibirSaldo())