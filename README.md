# Todo Agent

A powerful, agent-based Todo application that leverages a modern tech stack to provide seamless task management through AI-driven agents. Organize, create, update, and delete your tasks efficiently with an intelligent assistant interface.

## Technologies Used

- Node.js  
- Express.js  
- MongoDB  
- React.js  
- FastAPI  
- Python  
- OpenAI agents SDK

## Setup Guide

### Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### Backend Setup

1. Navigate to the backend folder and install dependencies:

```bash
cd backend
npm install
```

2. Create a `.env` file in the backend root directory with the following variables:

```env
PORT=port
JWT_SECRET=jwt_secret
MONGO_URI=mongodb_connection_string
CORS_ORIGIN=agent-base-url
```

3. Start the backend server:

```bash
npm run start
```

### Frontend Setup

1. Navigate to the frontend folder and install dependencies:

```bash
cd frontend
npm install
```

2. Create a `.env` file in the frontend root directory with:

```env
VITE_API_URL=agent-base-url
```

3. Start the React development server:

```bash
npm run dev
```
Access app: [http://localhost:5173](http://localhost:5173)


### Agent Setup

1. Add environment variables for the agent (in your shell or `.env`):

```env
MODEL=model-name
API_KEY=gemini-api-key
BASE_URL=backend-base-url
CORS_ORIGIN=frontend-base-url
```

2. Run the agent server with `uvicorn` (adjust path if needed):

```bash
uvicorn src.agent.main:app --reload --port=5000 --host 0.0.0.0
```

Or using your `uv` CLI tool:

```bash
uv run cli
```

