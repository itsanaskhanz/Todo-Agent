require('dotenv').config()
const mongoose = require('mongoose');

const connectDB = async () => {
  console.log('eh')
  try {
    const conn = await mongoose.connect(process.env.MONGO_URI);
    console.log(`📦 MongoDB connected`);
  } catch (error) {
    console.error('❌ MongoDB connection failed:', error.message);
  }
};

module.exports = connectDB;
