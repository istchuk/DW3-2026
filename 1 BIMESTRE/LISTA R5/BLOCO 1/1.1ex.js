class ContaBancaria{
    constructor(nome, saldoInicial){
        this._titular = nome
        this._saldo = saldoInicial
    }

    depositar(valor){
        this._saldo += valor
    }

    sacar(valor){
        if (valor > this._saldo){
            console.log("Saldo insuficiente")
            return
        }
        else{
           this._saldo -= valor
        }
    }

    exibirSaldo(){
        return `Titular: ${this._titular} | Saldo: ${this._saldo.toFixed(2)}`
    }
}

const joao = new ContaBancaria('João',100)
joao.depositar(5000)


const gabriel = new ContaBancaria('Gabriel', 1000)
gabriel.sacar(10000)


console.log(gabriel.exibirSaldo())
console.log(joao.exibirSaldo())