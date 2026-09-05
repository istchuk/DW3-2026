import db from '../database/drizzle.js'
import client from '../database/clients.js'
import { projetos } from '../database/schema.js'

try {
  await client.connect()

  const listaProjetos = await db.select().from(projetos).orderBy(projetos.id)
  console.log('Projetos cadastrados:')
  console.table(listaProjetos)
} finally {
  await client.end()
}