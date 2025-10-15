# Thanksgiving Recipe FastAPI App 🦃

A beautiful, simple FastAPI application that displays a delicious Thanksgiving turkey recipe and includes a chat interface powered by GPT-4o. Ready to deploy to Vercel!

## Features

- 🍗 Classic Roast Turkey recipe with herb butter
- 💬 Chat with GPT-4o (bring your own API key)
- 🎨 Beautiful, responsive UI with warm Thanksgiving colors
- 📱 Mobile-friendly design
- 🔌 RESTful API endpoints
- 📚 Auto-generated API documentation

## Local Development

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn main:app --reload
```

3. Open your browser to:
- Home page: http://localhost:8000
- Chat interface: http://localhost:8000/chat
- Recipe JSON: http://localhost:8000/recipe
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## API Endpoints

- `GET /` - Beautiful HTML page with the recipe
- `GET /chat` - Chat interface with GPT-4o
- `POST /api/chat` - Chat API endpoint (requires OpenAI API key)
- `GET /recipe` - Get the recipe as JSON
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## Chat Feature

The app includes a chat interface that allows users to chat with GPT-4o:

1. Navigate to `/chat`
2. Enter your OpenAI API key (starts with `sk-`)
3. Start chatting!

**Security Note:** Your API key is sent directly to OpenAI and is never stored on our servers. Each request uses your API key client-side.

## Deploy to Vercel

### Option 1: Deploy with Vercel CLI

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Follow the prompts to complete deployment

### Option 2: Deploy with GitHub

1. Push this repository to GitHub
2. Go to [Vercel](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will automatically detect the configuration
6. Click "Deploy"

### Option 3: Deploy via Vercel Dashboard

1. Create a ZIP file of this directory
2. Go to [Vercel](https://vercel.com)
3. Drag and drop the ZIP file
4. Vercel will handle the rest!

## Project Structure

```
simple-fastapi-app/
├── main.py           # FastAPI application
├── requirements.txt  # Python dependencies
├── vercel.json      # Vercel deployment configuration
└── README.md        # This file
```

## Configuration

The `vercel.json` file configures Vercel to:
- Build the Python application using `@vercel/python`
- Route all requests to the FastAPI app

## Customization

To customize the recipe, edit the `recipe` dictionary in `main.py`. You can change:
- Recipe name
- Ingredients
- Instructions
- Cooking times
- Pro tips

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **OpenAI GPT-4o** - State-of-the-art language model for chat
- **Vercel** - Serverless deployment platform

## License

MIT License - Feel free to use this for your Thanksgiving celebration!

---

Made with ❤️ for Thanksgiving

