"use client"

import { useEffect, useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Clock, Users, ChefHat, Lightbulb } from "lucide-react"
import { Skeleton } from "@/components/ui/skeleton"
import { fetchRecipe } from "@/lib/api"

interface Recipe {
  name: string
  servings: string
  prep_time: string
  cook_time: string
  ingredients: string[]
  instructions: string[]
  tips: string[]
}

export function RecipeDisplay() {
  const [recipe, setRecipe] = useState<Recipe | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchRecipe()
      .then((data) => {
        setRecipe(data)
        setLoading(false)
      })
      .catch((err) => {
        setError("Failed to load recipe")
        setLoading(false)
      })
  }, [])

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-4xl mx-auto space-y-6">
          <Skeleton className="h-32 w-full" />
          <Skeleton className="h-64 w-full" />
          <Skeleton className="h-96 w-full" />
        </div>
      </div>
    )
  }

  if (error || !recipe) {
    return (
      <div className="container mx-auto px-4 py-12">
        <Card className="max-w-4xl mx-auto">
          <CardContent className="py-12 text-center">
            <p className="text-destructive">{error || "Recipe not found"}</p>
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Meta Information */}
        <Card>
          <CardContent className="pt-6">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="flex items-center gap-3">
                <div className="p-3 rounded-lg bg-secondary">
                  <Users className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Servings</p>
                  <p className="font-semibold">{recipe.servings}</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <div className="p-3 rounded-lg bg-secondary">
                  <Clock className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Prep Time</p>
                  <p className="font-semibold">{recipe.prep_time}</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <div className="p-3 rounded-lg bg-secondary">
                  <ChefHat className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Cook Time</p>
                  <p className="font-semibold">{recipe.cook_time}</p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Ingredients */}
        <Card>
          <CardHeader>
            <CardTitle className="text-2xl">Ingredients</CardTitle>
            <CardDescription>Everything you'll need for this recipe</CardDescription>
          </CardHeader>
          <CardContent>
            <ul className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {recipe.ingredients.map((ingredient, index) => (
                <li key={index} className="flex items-start gap-2">
                  <span className="text-accent mt-1">•</span>
                  <span className="text-foreground">{ingredient}</span>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>

        {/* Instructions */}
        <Card>
          <CardHeader>
            <CardTitle className="text-2xl">Instructions</CardTitle>
            <CardDescription>Follow these steps for perfect results</CardDescription>
          </CardHeader>
          <CardContent>
            <ol className="space-y-4">
              {recipe.instructions.map((instruction, index) => (
                <li key={index} className="flex gap-4">
                  <Badge variant="secondary" className="h-7 w-7 rounded-full flex items-center justify-center shrink-0">
                    {index + 1}
                  </Badge>
                  <p className="text-foreground pt-0.5">{instruction}</p>
                </li>
              ))}
            </ol>
          </CardContent>
        </Card>

        {/* Pro Tips */}
        <Card className="border-accent/20 bg-accent/5">
          <CardHeader>
            <div className="flex items-center gap-2">
              <Lightbulb className="h-5 w-5 text-accent" />
              <CardTitle className="text-2xl">Pro Tips</CardTitle>
            </div>
            <CardDescription>Expert advice for the best results</CardDescription>
          </CardHeader>
          <CardContent>
            <ul className="space-y-3">
              {recipe.tips.map((tip, index) => (
                <li key={index} className="flex items-start gap-2">
                  <span className="text-accent mt-1">✓</span>
                  <span className="text-foreground">{tip}</span>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
