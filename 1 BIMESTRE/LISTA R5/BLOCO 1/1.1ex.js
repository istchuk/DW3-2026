class ContaBancaria{
    constructor(nome){
        this._titular = nome
        this._saldo = 0
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
        return `Titular: ${this._titular} | Saldo ${this._saldo}`
    }
}

const joao = new ContaBancaria('João')

joao.depositar(5000)
console.log(joao.exibirSaldo())

joao.sacar(6000)
console.log(joao.exibirSaldo())