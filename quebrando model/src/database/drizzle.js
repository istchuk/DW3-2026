import { drizzle } from 'drizzle-orm/node-postgres'

import client from './clients.js'

const db = drizzle({ client })

export default db