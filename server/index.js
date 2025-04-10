const express = require('express');
const cors = require('cors');
const { loadUserData, incrementUser } = require('./data/database');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// Проверка сервера
app.get('/', (req, res) => {
    res.send('Сервер работает!');
});

// Получить данные пользователя
app.get('/api/user/:id', (req, res) => {
    const userId = req.params.id;
    const data = loadUserData(userId);
    res.json(data);
});

// Увеличить счётчик
app.post('/api/user/:id/increment', (req, res) => {
    const userId = req.params.id;
    const data = incrementUser(userId);
    res.json(data);
});

app.listen(PORT, () => {
    console.log(`🔥 Сервер работает на http://localhost:${PORT}`);
});
