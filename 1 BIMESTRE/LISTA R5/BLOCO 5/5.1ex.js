// 1. O erro acontece porque foi usada uma função normal dentro do setInterval. 
// Nesse caso, o this não aponta para a instância da classe Timer, mas sim
// para outro contexto (como window ou undefined), então this.segundos e this.nome 
// não funcionam.

// 2.Ao usar uma arrow function, o this não muda conforme a execução; 
// ele é herdado do contexto onde a função foi criada. Assim, continua 
// apontando para a instância do Timer, funcionando corretamente.

// CORREÇÃO
class Timer {
  constructor(nome) {
    this.nome = nome
    this.segundos = 0
  }

  iniciar() {
    setInterval(() => {
      this.segundos++
      console.log(`${this.nome}: ${this.segundos}s`)
    }, 1000)
  }
}

const t = new Timer('Cronômetro')
t.iniciar()