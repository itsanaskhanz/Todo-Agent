const express = require('express');
const router = express.Router();
const protect = require('../middleware/authMiddleware');
const { signUp, login, deleteUser } = require('../controller/authController');

router.post('/signup', signUp);
router.post('/login', login);
router.delete('/deleteUser', protect, deleteUser);

module.exports = router;
