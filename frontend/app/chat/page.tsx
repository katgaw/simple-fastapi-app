import { ChatInterface } from "@/components/chat-interface"
import { Button } from "@/components/ui/button"
import { ArrowLeft } from "lucide-react"
import Link from "next/link"

export default function ChatPage() {
  return (
    <div className="min-h-screen bg-background flex flex-col">
      {/* Header */}
      <header className="border-b border-border">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Link href="/">
              <Button variant="ghost" size="sm" className="gap-2">
                <ArrowLeft className="h-4 w-4" />
                Back to Recipe
              </Button>
            </Link>
            <div className="flex items-center gap-2">
              <span className="text-2xl">💬</span>
              <h1 className="text-xl font-semibold">AI Chat Assistant</h1>
            </div>
          </div>
          <div className="text-sm text-muted-foreground">Powered by GPT-4o</div>
        </div>
      </header>

      {/* Chat Interface */}
      <ChatInterface />
    </div>
  )
}
