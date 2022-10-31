const db = require('./queries')
const bodyParser = require('body-parser')
const port = 3000
const express = require('express')
const app = express()


app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)

app.get('/', (request, response) => {
  response.json({ info: 'Node.js, Express, and Postgres API' })
})

app.get('/users', db.getUsers)
app.get('/users/:username', db.getUserByUserName)
app.post('/users', db.createUser)
app.put('/users/:username', db.updateUser)


app.listen(port, () => {
  console.log(`App running on port ${port}.`)
})