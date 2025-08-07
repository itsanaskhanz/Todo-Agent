const Todo = require('../models/Todo');

const getTodos = async (req, res) => {
  try {
    const todos = await Todo.find({ user: req.user.id });
    res.status(200).json(todos);
  } catch (error) {
    res.status(500).json({ message: 'Failed to fetch todos', error: error.message });
  }
};

const createTodo = async (req, res) => {
  const { name, desc, completed } = req.body;
  try {
    const todo = new Todo({
      name,
      desc,
      completed: completed || false,
      user: req.user.id
    });
    const savedTodo = await todo.save();
    res.status(201).json(savedTodo);
  } catch (error) {
    res.status(500).json({ message: 'Failed to create todo', error: error.message });
  }
};

const updateTodo = async (req, res) => {
  const { id } = req.params;
  const { name, desc, completed } = req.body;
  try {
    const updatedTodo = await Todo.findOneAndUpdate(
      { _id: id, user: req.user.id },
      { name, desc, completed },
      { new: true }
    );
    if (!updatedTodo) return res.status(404).json({ message: 'Todo not found' });
    res.status(200).json(updatedTodo);
  } catch (error) {
    res.status(500).json({ message: 'Failed to update todo', error: error.message });
  }
};

const deleteTodo = async (req, res) => {
  const { id } = req.params;
  try {
    const deleted = await Todo.findOneAndDelete({ _id: id, user: req.user.id });
    if (!deleted) return res.status(404).json({ message: 'Todo not found' });
    res.status(200).json({ message: 'Todo deleted' });
  } catch (error) {
    res.status(500).json({ message: 'Failed to delete todo', error: error.message });
  }
};

module.exports = {
  getTodos,
  createTodo,
  updateTodo,
  deleteTodo
};
