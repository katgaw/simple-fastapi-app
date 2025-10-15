"use client"

import { useEffect, useState } from "react"
import { Drawer } from "vaul"
import { Button } from "@/components/ui/button"
import { Loader2, ChefHat, Clock, Users, X } from "lucide-react"

interface RecipeDrawerProps {
  isOpen: boolean
  onClose: () => void
  dietType: "vegetarian" | "vegan" | "no_restrictions" | null
  isLoading: boolean
  setIsLoading: (loading: boolean) => void
}

interface Recipe {
  name: string
  description?: string
  ingredients?: string[]
  instructions?: string[]
  prep_time?: string
  servings?: string
  [key: string]: any
}

export function RecipeDrawer({ isOpen, onClose, dietType, isLoading, setIsLoading }: RecipeDrawerProps) {
  const [recipe, setRecipe] = useState<Recipe | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (isOpen && dietType) {
      fetchRecipe()
    }
  }, [isOpen, dietType])

  const fetchRecipe = async () => {
    if (!dietType) return

    setIsLoading(true)
    setError(null)
    setRecipe(null)

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL
      if (!apiUrl) {
        throw new Error("API URL not configured")
      }

      const response = await fetch(`${apiUrl}/recipe`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          diet_type: dietType,
        }),
      })

      if (!response.ok) {
        throw new Error(`Failed to fetch recipe: ${response.statusText}`)
      }

      const data = await response.json()
      setRecipe(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch recipe")
      console.error("[v0] Error fetching recipe:", err)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <Drawer.Root open={isOpen} onOpenChange={onClose}>
      <Drawer.Portal>
        <Drawer.Overlay className="fixed inset-0 bg-black/40" />
        <Drawer.Content className="fixed bottom-0 left-0 right-0 mt-24 flex max-h-[90vh] flex-col rounded-t-xl bg-card">
          <div className="flex-1 overflow-y-auto rounded-t-xl bg-card p-6">
            <div className="mx-auto mb-6 h-1.5 w-12 flex-shrink-0 rounded-full bg-muted" />

            <div className="mx-auto max-w-2xl">
              <div className="mb-6 flex items-start justify-between">
                <div className="flex items-center gap-3">
                  <div className="rounded-full bg-primary/10 p-3">
                    <ChefHat className="h-6 w-6 text-primary" />
                  </div>
                  <div>
                    <Drawer.Title className="text-2xl font-bold text-card-foreground">Your Recipe</Drawer.Title>
                    <p className="text-sm text-muted-foreground">
                      {dietType?.replace("_", " ").replace(/\b\w/g, (l) => l.toUpperCase())}
                    </p>
                  </div>
                </div>
                <Button
                  variant="ghost"
                  size="icon"
                  onClick={onClose}
                  className="text-muted-foreground hover:text-foreground"
                >
                  <X className="h-5 w-5" />
                </Button>
              </div>

              {isLoading && (
                <div className="flex flex-col items-center justify-center py-12">
                  <Loader2 className="mb-4 h-12 w-12 animate-spin text-primary" />
                  <p className="text-lg text-muted-foreground">Generating your recipe...</p>
                </div>
              )}

              {error && (
                <div className="rounded-lg bg-destructive/10 p-4 text-destructive">
                  <p className="font-semibold">Error</p>
                  <p className="text-sm">{error}</p>
                  <Button variant="outline" size="sm" onClick={fetchRecipe} className="mt-4 bg-transparent">
                    Try Again
                  </Button>
                </div>
              )}

              {recipe && !isLoading && (
                <div className="space-y-6">
                  <div>
                    <h2 className="mb-2 text-3xl font-bold text-card-foreground">{recipe.name}</h2>
                    {recipe.description && <p className="text-pretty text-muted-foreground">{recipe.description}</p>}
                  </div>

                  {(recipe.prep_time || recipe.servings) && (
                    <div className="flex flex-wrap gap-4">
                      {recipe.prep_time && (
                        <div className="flex items-center gap-2 text-sm">
                          <Clock className="h-4 w-4 text-primary" />
                          <span className="text-muted-foreground">{recipe.prep_time}</span>
                        </div>
                      )}
                      {recipe.servings && (
                        <div className="flex items-center gap-2 text-sm">
                          <Users className="h-4 w-4 text-primary" />
                          <span className="text-muted-foreground">{recipe.servings}</span>
                        </div>
                      )}
                    </div>
                  )}

                  {recipe.ingredients && recipe.ingredients.length > 0 && (
                    <div>
                      <h3 className="mb-3 text-xl font-semibold text-card-foreground">Ingredients</h3>
                      <ul className="space-y-2">
                        {recipe.ingredients.map((ingredient, index) => (
                          <li key={index} className="flex items-start gap-3 text-muted-foreground">
                            <span className="mt-1.5 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-primary" />
                            <span>{ingredient}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {recipe.instructions && recipe.instructions.length > 0 && (
                    <div>
                      <h3 className="mb-3 text-xl font-semibold text-card-foreground">Instructions</h3>
                      <ol className="space-y-4">
                        {recipe.instructions.map((instruction, index) => (
                          <li key={index} className="flex gap-4">
                            <span className="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-full bg-primary/10 font-semibold text-primary">
                              {index + 1}
                            </span>
                            <span className="pt-0.5 text-muted-foreground">{instruction}</span>
                          </li>
                        ))}
                      </ol>
                    </div>
                  )}

                  <div className="flex gap-3 pt-4">
                    <Button onClick={fetchRecipe} className="flex-1">
                      Generate Another Recipe
                    </Button>
                    <Button variant="outline" onClick={onClose}>
                      Close
                    </Button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </Drawer.Content>
      </Drawer.Portal>
    </Drawer.Root>
  )
}
