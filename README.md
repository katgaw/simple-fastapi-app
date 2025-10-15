# Diet Recipe App 🍽️

A full-stack application that generates personalized dinner recipes using OpenAI's GPT-4. Built with FastAPI (backend) and Next.js (frontend).

## Features

- 🥗 Generate vegetarian recipes
- 🌱 Generate vegan recipes
- 🍽️ Generate recipes with no dietary restrictions
- 🎨 Beautiful, modern web interface with drawer component (vaul)
- ⚡ Fast API powered by FastAPI
- 🤖 AI-powered recipes using GPT-4
- 📱 Responsive design

## Tech Stack

### Backend
- Python 3.13
- FastAPI 0.115.4
- OpenAI 1.54.3
- Uvicorn 0.32.0

### Frontend
- Next.js 15.1.4
- React 18.3.1
- TypeScript
- Tailwind CSS
- Vaul 1.1.1 (drawer component)
- Lucide React (icons)

## Requirements

- Python 3.13
- Node.js 18+ / npm
- OpenAI API Key

## Setup

### Backend Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

3. Run the backend server:
```bash
uvicorn main:app --reload
```

The backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. The `.env.local` file is already configured to connect to `http://localhost:8000`

4. Run the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:3000`

## Running the Full Application

1. **Terminal 1** - Start the backend:
```bash
uvicorn main:app --reload
```

2. **Terminal 2** - Start the frontend:
```bash
cd frontend
npm run dev
```

3. Open your browser to `http://localhost:3000`

## API Endpoints

- `GET /` - API info and health check
- `POST /recipe` - Generate a recipe (accepts JSON with `diet_type`: "vegetarian", "vegan", or "no_restrictions")
- `GET /health` - Health check endpoint

## Example API Usage

```bash
curl -X POST "http://localhost:8000/recipe" \
  -H "Content-Type: application/json" \
  -d '{"diet_type": "vegan"}'
```

Response format:
```json
{
  "name": "Recipe Name",
  "description": "Brief description",
  "prep_time": "30 minutes",
  "servings": "4 servings",
  "ingredients": ["ingredient 1", "ingredient 2"],
  "instructions": ["step 1", "step 2"]
}
```

## Python 3.13 Compatibility

All backend libraries are compatible with Python 3.13:
- fastapi 0.115.4
- uvicorn 0.32.0
- openai 1.54.3
- python-dotenv 1.0.1
- pydantic 2.9.2

## Project Structure

```
simple-fastapi-app/
├── main.py              # FastAPI backend
├── requirements.txt     # Python dependencies
├── .env                 # Backend environment variables
├── README.md            # This file
└── frontend/
    ├── app/             # Next.js app directory
    ├── components/      # React components
    ├── lib/             # Utilities
    ├── package.json     # Frontend dependencies
    └── .env.local       # Frontend environment variables
```

