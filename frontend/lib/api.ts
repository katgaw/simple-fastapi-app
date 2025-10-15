// API Configuration
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

// API Helper Functions
export async function fetchRecipe() {
  const response = await fetch(`${API_BASE_URL}/recipe`)
  if (!response.ok) {
    throw new Error("Failed to fetch recipe")
  }
  return response.json()
}

export async function sendChatMessage(messages: Array<{ role: string; content: string }>, apiKey: string) {
  const response = await fetch(`${API_BASE_URL}/api/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages,
      api_key: apiKey,
    }),
  })

  const data = await response.json()

  if (!response.ok) {
    throw new Error(data.detail || "Failed to get response")
  }

  return data
}

