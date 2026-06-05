import { TarefaRepository } from './tarefa.repository.js'
import { TarefaService } from './tarefa.service.js'
import { TarefaController } from './tarefa.controller.js'

export default async function tarefaRoutes(server) {
  // Instancia as camadas da funcionalidade
  const tarefaRepository = new TarefaRepository()
  const tarefaService = new TarefaService(tarefaRepository)
  const tarefaController = new TarefaController(tarefaService)

  // Rotas da API de tarefas
  server.get('/tarefas', (req, res) =>
    tarefaController.listar(req, res)
  )

  server.post('/tarefas', (req, res) =>
    tarefaController.criar(req, res)
  )

  server.get('/tarefas/:id', (req, res) =>
    tarefaController.buscar(req, res)
  )

  server.patch('/tarefas/:id', (req, res) =>
    tarefaController.atualizar(req, res)
  )

  server.patch('/tarefas/:id/concluir', (req, res) =>
    tarefaController.concluir(req, res)
  )

  server.delete('/tarefas/:id', (req, res) =>
    tarefaController.remover(req, res)
  )
}