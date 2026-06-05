import { AppError } from '../shared/errors/app-error.js'

export class TarefaService {
  constructor(repository) {
    this.repository = repository
  }

  async listarTarefas(filtros = {}) {
    const tarefas = await this.repository.listarTodos()

    let tarefasFiltradas = tarefas

    if (filtros.busca) {
      const termoBusca = filtros.busca.toLowerCase()

      tarefasFiltradas = tarefasFiltradas.filter(tarefa =>
        tarefa.titulo.toLowerCase().includes(termoBusca)
      )
    }

    if (filtros.status) {
      tarefasFiltradas = tarefasFiltradas.filter(
        tarefa => tarefa.status === filtros.status
      )
    }

    return tarefasFiltradas
  }

  async buscarPorId(id) {
    const tarefa = await this.repository.buscarPorId(id)

    if (!tarefa) {
      throw new AppError('Tarefa não encontrada', 404)
    }

    return tarefa
  }

  async criarTarefa(dados) {
    this.validarTitulo(dados.titulo)

    const tarefas = await this.repository.listarTodos()
    const tituloNormalizado = dados.titulo.trim().toLowerCase()

    const tarefaExistente = tarefas.some(
      tarefa => tarefa.titulo.toLowerCase() === tituloNormalizado
    )

    if (tarefaExistente) {
      throw new AppError('Já existe uma tarefa com esse título', 400)
    }

    return this.repository.salvar({
      ...dados,
      status: 'pendente'
    })
  }

  async atualizarTarefa(id, dados) {
    const tarefa = await this.buscarPorId(id)

    // Não permite alterar tarefas já concluídas
    if (tarefa.status === 'concluida') {
      throw new AppError(
        'Não é possível atualizar uma tarefa já concluída',
        400
      )
    }

    return this.repository.atualizar(id, dados)
  }

  async concluirTarefa(id) {
    const tarefa = await this.buscarPorId(id)

    const novoStatus =
      tarefa.status === 'concluida'
        ? 'pendente'
        : 'concluida'

    return this.repository.atualizar(id, {
      status: novoStatus
    })
  }

  async removerTarefa(id) {
    const tarefa = await this.buscarPorId(id)

    // Apenas tarefas pendentes podem ser removidas
    if (tarefa.status === 'concluida') {
      throw new AppError(
        'Não é possível remover uma tarefa já concluída',
        400
      )
    }

    return this.repository.remover(id)
  }

  validarTitulo(titulo) {
    if (!titulo || titulo.trim() === '') {
      throw new AppError('O título é obrigatório', 400)
    }
  }
}