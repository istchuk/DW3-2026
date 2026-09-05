import client from '../database/clients.js'

class TarefaRepository {
  constructor() {
    this.tarefas = [
      { id: 1, descricao: "Fazer compras", concluido: false },
      { id: 2, descricao: "Lavar o carro", concluido: false },
      { id: 3, descricao: "Estudar Fastify", concluido: true }
    ]
  }

  async buscarTodos() {
  const resultado = await client.query(`
    SELECT
      t.id,
      t.descricao,
      t.concluido,
      t.criada_em,
      t.projeto_id,
      p.nome AS projeto_nome
    FROM tarefas t
    LEFT JOIN projetos p
      ON p.id = t.projeto_id
    ORDER BY t.id
  `)

  return resultado.rows
  }
  
  async listarPendentes() {
  return this.tarefas.filter(t => !t.concluido)
  }

  async buscarPorId(id) {
  const resultado = await client.query(`
    SELECT
      t.id,
      t.descricao,
      t.concluido,
      t.criada_em,
      t.projeto_id,
      tg.nome AS tag_nome
    FROM tarefas t
    LEFT JOIN tarefas_tags tt
      ON tt.tarefa_id = t.id
    LEFT JOIN tags tg
      ON tg.id = tt.tag_id
    WHERE t.id = $1
  `, [id])

  if (resultado.rows.length === 0) return null

  return {
    id: resultado.rows[0].id,
    descricao: resultado.rows[0].descricao,
    concluido: resultado.rows[0].concluido,
    criada_em: resultado.rows[0].criada_em,
    projeto_id: resultado.rows[0].projeto_id,
    tags: resultado.rows
      .filter(r => r.tag_nome)
      .map(r => r.tag_nome)
  }
}
  async salvar(tarefa) {
    const resultado = await client.query(
      `
      INSERT INTO tarefas (descricao, concluido, projeto_id)
      VALUES ($1, $2, $3)
      RETURNING id, descricao, concluido, criada_em, projeto_id
    `,
      [tarefa.descricao, tarefa.concluido, tarefa.projetoId]
    )

    return resultado.rows[0]
  }

  async atualizar(id, dadosAtualizados) {
    console.log("Repository: atualizar chamado")
    const index = this.tarefas.findIndex(t => t.id === id)
    if (index === -1) return null
    this.tarefas[index] = { ...this.tarefas[index], ...dadosAtualizados, id }
    return this.tarefas[index]
  }

  async remover(id) {
    console.log("Repository: remover chamado")
    const index = this.tarefas.findIndex(t => t.id === id)
    if (index === -1) return false
    this.tarefas.splice(index, 1)
    return true
  }

   
}

export default TarefaRepository