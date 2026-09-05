class TarefaService {
  constructor(repository) {
    this.repository = repository
  }

  async listar(opcoes) {
    console.log("Service: listar chamado")
    const { busca, concluido } = opcoes

    let resultado = await this.repository.buscarTodos()

    if (busca) {
      resultado = resultado.filter(t =>
        t.descricao.toLowerCase().includes(busca.toLowerCase())
      )
    }

    if (concluido !== undefined) {
      const concluidoBool = concluido === 'true'
      resultado = resultado.filter(t => t.concluido === concluidoBool)
    }

    resultado = resultado.map(t => ({
      id: t.id,
      descricao: t.descricao,
      concluido: t.concluido,
      criada_em: t.criada_em,
      projeto: t.projeto_id
        ? {
          id: t.projeto_id,
          nome: t.projeto_nome
        }
        : null
    }))

    return resultado
  }

  async criar(dados) {
    console.log("Service: criar chamado")

    const novaTarefa = await this.repository.salvar({
      descricao: dados.descricao,
      concluido: false,
      projetoId: dados.projetoId
    })

    return novaTarefa
}

   async listarPendentes() {
  console.log("Service: listarPendentes chamado")
  return this.repository.listarPendentes()
}

  async buscarPorId(id) {
    console.log("Service: buscarPorId chamado")
    return this.repository.buscarPorId(id)
  }

  async atualizar(id, dadosAtualizados) {
    console.log("Service: atualizar chamado")
    return this.repository.atualizar(id, dadosAtualizados)
  }

  async alternarConcluido(id) {
    console.log("Service: alternarConcluido chamado")
    const tarefa = await this.repository.buscarPorId(id)
    if (!tarefa) return null
    return this.repository.atualizar(id, { concluido: !tarefa.concluido })
  }

  async remover(id) {
    console.log("Service: remover chamado")
    return this.repository.remover(id)
  }

  async obterResumo() {
    console.log("Service: obterResumo chamado")
    const todas = await this.repository.buscarTodos()
    const total = todas.length
    const concluidas = todas.filter(t => t.concluido).length
    const pendentes = total - concluidas
    return { total, concluidas, pendentes }
  }
 
}

export default TarefaService