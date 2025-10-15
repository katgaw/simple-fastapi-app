"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { RecipeDrawer } from "@/components/recipe-drawer"
import { Leaf, Salad, Utensils } from "lucide-react"

type DietType = "vegetarian" | "vegan" | "no_restrictions"

interface DietOption {
  value: DietType
  label: string
  description: string
  icon: React.ReactNode
}

const dietOptions: DietOption[] = [
  {
    value: "vegetarian",
    label: "Vegetarian",
    description: "No meat, but includes dairy and eggs",
    icon: <Leaf className="h-8 w-8" />,
  },
  {
    value: "vegan",
    label: "Vegan",
    description: "Plant-based only, no animal products",
    icon: <Salad className="h-8 w-8" />,
  },
  {
    value: "no_restrictions",
    label: "No Restrictions",
    description: "All ingredients welcome",
    icon: <Utensils className="h-8 w-8" />,
  },
]

export function DietSelector() {
  const [selectedDiet, setSelectedDiet] = useState<DietType | null>(null)
  const [isDrawerOpen, setIsDrawerOpen] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  const handleDietSelect = async (diet: DietType) => {
    setSelectedDiet(diet)
    setIsLoading(true)
    setIsDrawerOpen(true)
  }

  return (
    <>
      <div className="grid gap-4 md:grid-cols-3">
        {dietOptions.map((option) => (
          <Card
            key={option.value}
            className="group cursor-pointer transition-all hover:border-primary hover:shadow-lg"
            onClick={() => handleDietSelect(option.value)}
          >
            <div className="flex flex-col items-center gap-4 p-6 text-center">
              <div className="rounded-full bg-primary/10 p-4 text-primary transition-colors group-hover:bg-primary group-hover:text-primary-foreground">
                {option.icon}
              </div>
              <div>
                <h3 className="mb-2 font-sans text-xl font-semibold text-card-foreground">{option.label}</h3>
                <p className="text-sm text-muted-foreground">{option.description}</p>
              </div>
              <Button
                variant="outline"
                className="mt-2 w-full group-hover:border-primary group-hover:bg-primary group-hover:text-primary-foreground bg-transparent"
              >
                Get Recipe
              </Button>
            </div>
          </Card>
        ))}
      </div>

      <RecipeDrawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        dietType={selectedDiet}
        isLoading={isLoading}
        setIsLoading={setIsLoading}
      />
    </>
  )
}
