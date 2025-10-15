import { DietSelector } from "@/components/diet-selector"

export default function Home() {
  return (
    <main className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8 md:py-16">
        <div className="mx-auto max-w-3xl">
          <div className="mb-12 text-center">
            <h1 className="mb-4 font-sans text-4xl font-bold tracking-tight text-foreground md:text-5xl lg:text-6xl">
              AI Recipe Generator
            </h1>
            <p className="text-balance text-lg text-muted-foreground md:text-xl">
              Get personalized recipe recommendations based on your dietary preferences
            </p>
          </div>

          <DietSelector />
        </div>
      </div>
    </main>
  )
}
