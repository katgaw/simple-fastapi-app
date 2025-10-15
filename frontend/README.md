# Thanksgiving Recipe Frontend

A modern Next.js frontend for the FastAPI Thanksgiving recipe backend.

## Features

- 🦃 Beautiful recipe display with dark theme
- 💬 AI-powered chat interface using GPT-4o
- 🎨 Modern UI with Tailwind CSS and shadcn/ui
- 📱 Fully responsive design
- ⚡ Fast and optimized for Vercel deployment

## Getting Started

1. Install dependencies:
\`\`\`bash
npm install
\`\`\`

2. Create a `.env.local` file:
\`\`\`bash
NEXT_PUBLIC_API_URL=http://localhost:8000
\`\`\`

3. Start the development server:
\`\`\`bash
npm run dev
\`\`\`

4. Make sure your FastAPI backend is running on port 8000

## Deployment to Vercel

1. Push your code to GitHub
2. Import the project in Vercel
3. Add the environment variable:
   - `NEXT_PUBLIC_API_URL`: Your FastAPI backend URL
4. Deploy!

## Environment Variables

- `NEXT_PUBLIC_API_URL`: The URL of your FastAPI backend (default: http://localhost:8000)

## Tech Stack

- Next.js 15
- React 19
- Tailwind CSS v4
- shadcn/ui components
- TypeScript
