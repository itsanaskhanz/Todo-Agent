const express = require('express');
const router = express.Router();
const {
  getTodos,
  createTodo,
  updateTodo,
  deleteTodo
} = require('../controller/todoController');

const protect = require('../middleware/authMiddleware');

router.get('/get', protect, getTodos);
router.post('/create', protect, createTodo);
router.put('/update/:id', protect, updateTodo);
router.delete('/delete/:id', protect, deleteTodo);

module.exports = router;
