# Quick Start Guide 🚀

Get the Diet Recipe App running in 2 minutes!

## Prerequisites

- Python 3.13 installed
- Node.js 18+ / npm installed
- OpenAI API key

## Setup Steps

### 1. Backend Setup (Terminal 1)

```bash
# Make sure you're in the project root
cd /Users/katerinag/simple-fastapi-app

# Install Python dependencies
pip install -r requirements.txt

# Make sure .env file exists with your OpenAI API key
# If not, create it:
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Start the backend
uvicorn main:app --reload
```

✅ Backend should be running at `http://localhost:8000`

### 2. Frontend Setup (Terminal 2)

```bash
# Navigate to frontend directory
cd /Users/katerinag/simple-fastapi-app/frontend

# Install dependencies (first time only)
npm install

# Start the frontend
npm run dev
```

✅ Frontend should be running at `http://localhost:3000`

### 3. Open the App

Open your browser and go to: **http://localhost:3000**

## Quick Test

1. Click on one of the diet options (Vegetarian, Vegan, or No Restrictions)
2. Wait a few seconds for GPT-4 to generate your recipe
3. Enjoy your personalized recipe in the beautiful drawer!

## Troubleshooting

### Backend Issues

- **"OpenAI API key not found"**: Make sure your `.env` file exists in the root directory with `OPENAI_API_KEY=your_key`
- **Port 8000 already in use**: Stop any other service running on port 8000, or change the port using `uvicorn main:app --reload --port 8001` (and update frontend `.env.local`)

### Frontend Issues

- **"Failed to fetch recipe"**: Make sure the backend is running on `http://localhost:8000`
- **Port 3000 already in use**: Next.js will automatically suggest port 3001

## Environment Files

### Backend (.env in root)
```
OPENAI_API_KEY=your_api_key_here
```

### Frontend (frontend/.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Both files are already configured and gitignored!

## Running Commands Summary

**Backend:**
```bash
uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend && npm run dev
```

That's it! Happy cooking! 👨‍🍳👩‍🍳

