const Pool = require('pg').Pool
require('dotenv').config();

const pool = new Pool({
    host: process.env.HOST_URL,
    user: process.env.USER,
    port: process.env.PORT,
    password: process.env.PASS,
    database: process.env.DATABASE
})

const getUsers = (request, response) => {
  pool.query('SELECT * FROM ecouserdata', (error, results) => {
    if (error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}

const getUserByUserName = (request, response) => {
  const username = request.params.username

  pool.query('SELECT * FROM ecouserdata WHERE username = $1', [username], (error, results) => {
    if (error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}

const createUser = (request, response) => {
  const { username, password } = request.body

  pool.query('INSERT INTO ecouserdata (username, password) VALUES ($1, $2)', [username, password], (error, results) => {
    if (error) {
      throw error
    }
    response.status(201).send(`User added`)
  })
}

const updateUser = (request, response) => {
  const username = request.params.username
  const ecoscore = parseInt(request.body.ecoscore)

  pool.query(
    'UPDATE ecouserdata SET ecoscore = $1 WHERE username = $2',
    [ecoscore, username],
    (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).send(`Ecoscore of user ${username} modified`)
    }
  )
}


module.exports = {
  getUsers,
  getUserByUserName,
  createUser,
  updateUser
}