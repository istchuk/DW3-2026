export class TarefaRepository {
  constructor() {
    this.tarefas = [
      { id: 1, titulo: 'Fazer compras', status: 'pendente' },
      { id: 2, titulo: 'Lavar o carro', status: 'pendente' },
      { id: 3, titulo: 'Estudar Fastify', status: 'concluida' }
    ]
  }

  async listarTodos() {
    console.log('Repository: listando tarefas')
    return this.tarefas
  }

  async buscarPorId(id) {
    console.log('Repository: buscando tarefa por ID')

    const idNumerico = Number(id)

    return this.tarefas.find(
      tarefa => tarefa.id === idNumerico
    ) || null
  }

  async salvar(dadosTarefa) {
    console.log('Repository: salvando tarefa')

    const ultimoId =
      this.tarefas.length > 0
        ? this.tarefas[this.tarefas.length - 1].id
        : 0

    const novaTarefa = {
      id: ultimoId + 1,
      ...dadosTarefa
    }

    this.tarefas.push(novaTarefa)

    return novaTarefa
  }

  async atualizar(id, dadosAtualizados) {
    console.log('Repository: atualizando tarefa')

    const idNumerico = Number(id)

    const indice = this.tarefas.findIndex(
      tarefa => tarefa.id === idNumerico
    )

    if (indice < 0) {
      return null
    }

    this.tarefas[indice] = {
      ...this.tarefas[indice],
      ...dadosAtualizados,
      id: idNumerico
    }

    return this.tarefas[indice]
  }

  async remover(id) {
    console.log('Repository: removendo tarefa')

    const idNumerico = Number(id)

    const indice = this.tarefas.findIndex(
      tarefa => tarefa.id === idNumerico
    )

    if (indice < 0) {
      return false
    }

    this.tarefas.splice(indice, 1)

    return true
  }
}