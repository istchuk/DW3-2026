import Fastify from 'fastify'
import cors from '@fastify/cors'

import tarefaRoutes from './routes/tarefa.routes.js'
import TarefaRepository from './repositories/tarefa.repository.js'
import TarefaService from './services/tarefa.service.js'
import TarefaController from './controllers/tarefa.controller.js'

import client from './database/clients.js'

const server = Fastify()

server.get('/laboratorio/tarefas-concluidas', async (request, reply) => {
  const resultado = await client.query(`
    SELECT *
    FROM tarefas
    WHERE concluido = true
    ORDER BY id
  `)

  return reply.send(resultado.rows)
})

server.register(cors, {
  origin: '*',
  methods: ['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS']
})

// Composition Root: criação e conexão das dependências
const repository = new TarefaRepository()
const service = new TarefaService(repository)
const controller = new TarefaController(service)

// Registra as rotas, passando o controller via options
server.register(tarefaRoutes, { controller })

server.get('/laboratorio/tarefas-db', async (request, reply) => {
  const resultado = await client.query(`
    SELECT *
    FROM tarefas
    ORDER BY id
  `)

  return reply.send(resultado.rows)
})

server.post('/laboratorio/tarefas-db', async (request, reply) => {
  const { descricao, concluido } = request.body

  const resultado = await client.query(
    `
      INSERT INTO tarefas (descricao, concluido)
      VALUES ($1, $2)
      RETURNING *
    `,
    [descricao, concluido]
  )

  return reply.status(201).send(resultado.rows[0])
})

const PORT = 3000

const start = async () => {
  try {
    await client.connect()
    console.log('Conectado ao PostgreSQL')

    await server.listen({ port: PORT })

    console.log(`Servidor rodando em http://localhost:${PORT}`)
  } catch (erro) {
    console.error(erro)
    process.exit(1)
  }
}

start()