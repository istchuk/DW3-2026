export class TarefaController {
  constructor(service) {
    this.service = service
  }

  async listar(request, reply) {
    const { busca, status } = request.query

    const listaTarefas = await this.service.listarTarefas({
      busca,
      status
    })

    return reply.send(listaTarefas)
  }

  async buscar(request, reply) {
    const { id } = request.params

    // Caso a tarefa não exista, o Service lança uma exceção.
    const tarefaEncontrada = await this.service.buscarPorId(id)

    return reply.send(tarefaEncontrada)
  }

  async criar(request, reply) {
    const novaTarefa = await this.service.criarTarefa(
      request.body
    )

    return reply.status(201).send(novaTarefa)
  }

  async atualizar(request, reply) {
    const { id } = request.params

    const tarefaAtualizada = await this.service.atualizarTarefa(
      id,
      request.body
    )

    return reply.send(tarefaAtualizada)
  }

  async concluir(request, reply) {
    const { id } = request.params

    const tarefaAtualizada = await this.service.concluirTarefa(id)

    return reply.send(tarefaAtualizada)
  }

  async remover(request, reply) {
    const { id } = request.params

    await this.service.removerTarefa(id)

    return reply.status(204).send()
  }
}