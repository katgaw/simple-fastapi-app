import Link from "next/link"
import { RecipeDisplay } from "@/components/recipe-display"
import { Button } from "@/components/ui/button"
import { MessageSquare, Github } from "lucide-react"

export default function Home() {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🦃</span>
            <h1 className="text-xl font-semibold">Thanksgiving Recipe</h1>
          </div>
          <nav className="flex items-center gap-4">
            <Link href="/chat">
              <Button variant="ghost" size="sm" className="gap-2">
                <MessageSquare className="h-4 w-4" />
                AI Chat
              </Button>
            </Link>
            <Button variant="ghost" size="sm" className="gap-2">
              <Github className="h-4 w-4" />
              GitHub
            </Button>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="border-b border-border">
        <div className="container mx-auto px-4 py-20 text-center">
          <div className="inline-block px-3 py-1 mb-6 text-sm font-medium rounded-full bg-accent/10 text-accent border border-accent/20">
            Perfect for Thanksgiving
          </div>
          <h2 className="text-5xl md:text-6xl font-bold mb-6 text-balance">
            Classic Roast Turkey
            <br />
            <span className="text-muted-foreground">with Herb Butter</span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto mb-8 text-pretty">
            A timeless recipe that brings warmth and flavor to your holiday table. Perfectly seasoned and roasted to
            golden perfection.
          </p>
          <div className="flex items-center justify-center gap-4">
            <Button size="lg" className="gap-2">
              View Recipe
            </Button>
            <Link href="/chat">
              <Button size="lg" variant="outline" className="gap-2 bg-transparent">
                <MessageSquare className="h-5 w-5" />
                Ask AI for Help
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Recipe Content */}
      <RecipeDisplay />

      {/* Footer */}
      <footer className="border-t border-border mt-20">
        <div className="container mx-auto px-4 py-8 text-center text-muted-foreground">
          <p>Built with Next.js and FastAPI • Deployed on Vercel</p>
        </div>
      </footer>
    </div>
  )
}
