import Fastify from 'fastify'
import cors from '@fastify/cors'

import client from './database/client.js'
import tarefaRoutes from './tarefas/tarefa.routes.js'

import { TarefaRepository } from './tarefas/tarefa.repository.js'
import { TarefaService } from './tarefas/tarefa.service.js'
import { TarefaController } from './tarefas/tarefa.controller.js'

const server = Fastify()

server.register(cors, {
  origin: '*',
  methods: ['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS']
})

// Composition Root
const repository = new TarefaRepository()
const service = new TarefaService(repository)
const controller = new TarefaController(service)

server.register(tarefaRoutes, { controller })

// ===== ROTAS DE LABORATÓRIO (ROTEIRO 10) =====

server.get('/laboratorio/tarefas-db', async (request, reply) => {
  const resultado = await client.query(`
    SELECT id, descricao, concluido, criada_em
    FROM tarefas
    ORDER BY id
  `)

  return reply.send(resultado.rows)
})

server.post('/laboratorio/tarefas-db', async (request, reply) => {
  const { descricao } = request.body

  if (!descricao || descricao.trim() === '') {
    return reply.status(400).send({
      status: 'error',
      message: 'A descrição da tarefa é obrigatória'
    })
  }

  const resultado = await client.query(
    `
      INSERT INTO tarefas (descricao)
      VALUES ($1)
      RETURNING id, descricao, concluido, criada_em
    `,
    [descricao.trim()]
  )

  return reply.status(201).send(resultado.rows[0])
})

// Exercício 2
server.get('/laboratorio/tarefas-concluidas', async (request, reply) => {
  const resultado = await client.query(`
    SELECT *
    FROM tarefas
    WHERE concluido = true
    ORDER BY id
  `)

  return reply.send(resultado.rows)
})

// ============================================

server.setNotFoundHandler((request, reply) => {
  reply.code(404).send({
    status: 'error',
    message: 'O recurso solicitado não existe nesta API.'
  })
})

const PORT = 3000

const start = async () => {
  try {
    await client.connect()
    console.log('Conectado ao PostgreSQL com sucesso')

    await server.listen({ port: PORT })

    console.log(`Servidor rodando em http://localhost:${PORT}`)
  } catch (erro) {
    console.error('Falha ao iniciar a aplicação:', erro)
    process.exit(1)
  }
}

start()