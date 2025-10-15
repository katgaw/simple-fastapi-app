# Diet Recipe App - Frontend

Modern Next.js frontend for the Diet Recipe App with a beautiful UI and drawer component.

## Tech Stack

- **Next.js 15.1.4** - React framework
- **React 18.3.1** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS 4** - Styling
- **Vaul 1.1.1** - Drawer component
- **Lucide React** - Icons

## Getting Started

1. Install dependencies:

```bash
npm install
```

2. Make sure the `.env.local` file exists with:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. Run the development server:

```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) with your browser.

## Important Note

Make sure the backend is running on `http://localhost:8000` before using the app. See the main README in the root directory for backend setup instructions.

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## Components

- `DietSelector` - Main component with three diet options
- `RecipeDrawer` - Vaul drawer component that displays recipes
- UI components - Button, Card (from shadcn/ui style)

## Features

- 🎨 Beautiful, responsive design
- 🌊 Smooth drawer animations using Vaul
- ⚡ Fast loading states
- 🔄 Generate multiple recipes
- 📱 Mobile-friendly
