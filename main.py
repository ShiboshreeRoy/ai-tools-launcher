import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import webbrowser
import random
import os
import platform

# Create icons directory if it doesn't exist
if not os.path.exists("icons"):
    os.makedirs("icons")

# List of AI tools with descriptions and icons
AI_TOOLS = [
    {"name": "ChatGPT", "desc": "Advanced conversational AI by OpenAI with multimodal capabilities", "url": "https://chat.openai.com/", "icon": "icons/chatgpt.png", "category": "Conversational"},
    {"name": "Google Gemini", "desc": "Google's powerful AI assistant with image understanding", "url": "https://gemini.google.com/", "icon": "icons/gemini.png", "category": "Multimodal"},
    {"name": "Claude", "desc": "AI assistant focused on helpfulness and harmlessness", "url": "https://claude.ai/", "icon": "icons/claude.png", "category": "Conversational"},
    {"name": "Midjourney", "desc": "AI image generation through Discord prompts", "url": "https://www.midjourney.com/", "icon": "icons/midjourney.png", "category": "Creative"},
    {"name": "DALL-E 3", "desc": "OpenAI's advanced image generation model", "url": "https://openai.com/dall-e-3", "icon": "icons/dalle.png", "category": "Creative"},
    {"name": "Runway ML", "desc": "Creative suite for AI-powered video and image generation", "url": "https://runwayml.com/", "icon": "icons/runway.png", "category": "Creative"},
    {"name": "ElevenLabs", "desc": "AI voice generation and text-to-speech platform", "url": "https://elevenlabs.io/", "icon": "icons/elevenlabs.png", "category": "Audio"},
    {"name": "Suno AI", "desc": "Create music with AI using text prompts", "url": "https://www.suno.ai/", "icon": "icons/suno.png", "category": "Audio"},
    {"name": "Perplexity", "desc": "AI-powered research assistant with citations", "url": "https://www.perplexity.ai/", "icon": "icons/perplexity.png", "category": "Research"},
    {"name": "Anthropic Console", "desc": "Claude's developer platform with API access", "url": "https://console.anthropic.com/", "icon": "icons/anthropic.png", "category": "Development"},
    {"name": "Hugging Face", "desc": "Platform for AI models, datasets, and spaces", "url": "https://huggingface.co/", "icon": "icons/huggingface.png", "category": "Development"},
    {"name": "Leonardo AI", "desc": "AI platform for image generation and editing", "url": "https://leonardo.ai/", "icon": "icons/leonardo.png", "category": "Creative"},
    {"name": "Copy.ai", "desc": "AI writing assistant for content creation", "url": "https://www.copy.ai/", "icon": "icons/copyai.png", "category": "Writing"},
    {"name": "Jasper AI", "desc": "AI writing tool for marketers and content creators", "url": "https://www.jasper.ai/", "icon": "icons/jasper.png", "category": "Writing"},
    {"name": "Writesonic", "desc": "AI writing assistant for blogs, ads, and more", "url": "https://writesonic.com/", "icon": "icons/writesonic.png", "category": "Writing"},
    {"name": "Notion AI", "desc": "AI assistant integrated into Notion for productivity", "url": "https://www.notion.so/product/ai", "icon": "icons/notion.png", "category": "Productivity"},
    {"name": "Zapier AI", "desc": "Automate workflows with AI-powered integrations", "url": "https://zapier.com/ai/", "icon": "icons/zapier.png", "category": "Automation"},
    {"name": "Trello AI", "desc": "AI features in Trello for task management and automation", "url": "https://trello.com/features/automation", "icon": "icons/trello.png", "category": "Productivity"},
    {"name": "Slack GPT", "desc": "AI assistant for Slack to enhance team communication", "url": "https://slack.com/features/gpt-ai-assistant", "icon": "icons/slack.png", "category": "Collaboration"},
    {"name": "Microsoft Copilot", "desc": "AI assistant integrated into Microsoft 365 apps", "url": "https://www.microsoft.com/en-us/microsoft-365/copilot", "icon": "icons/copilot.png", "category": "Productivity"},
    {"name": "Canva Magic Write", "desc": "AI writing assistant integrated into Canva", "url": "https://www.canva.com/features/magic-write/", "icon": "icons/canva.png", "category": "Creative"},
    {"name": "Figma AI", "desc": "AI features in Figma for design automation", "url": "https://www.figma.com/features/ai/", "icon": "icons/figma.png", "category": "Design"},
    {"name": "Adobe Firefly", "desc": "AI-powered creative tools for Adobe products", "url": "https://www.adobe.com/sensei/generative-ai/firefly.html", "icon": "icons/firefly.png", "category": "Creative"},
    {"name": "Synthesia", "desc": "AI video generation platform for creating videos from text", "url": "https://www.synthesia.io/", "icon": "icons/synthesia.png", "category": "Video"},
    {"name": "Descript", "desc": "AI-powered audio and video editing platform", "url": "https://www.descript.com/", "icon": "icons/descript.png", "category": "Audio"},
    {"name": "Pictory", "desc": "AI video creation platform for marketers and content creators", "url": "https://pictory.ai/", "icon": "icons/pictory.png", "category": "Video"},
    {"name": "DeepL Translator", "desc": "AI-powered translation service with high accuracy", "url": "https://www.deepl.com/translator", "icon": "icons/deepl.png", "category": "Language"},
    {"name": "Grammarly", "desc": "AI writing assistant for grammar and style checking", "url": "https://www.grammarly.com/", "icon": "icons/grammarly.png", "category": "Writing"},
    {"name": "QuillBot", "desc": "AI paraphrasing tool for rewriting text", "url": "https://quillbot.com/", "icon": "icons/quillbot.png", "category": "Writing"},
    {"name": "Otter.ai", "desc": "AI transcription service for meetings and lectures", "url": "https://otter.ai/", "icon": "icons/otter.png", "category": "Productivity"},
    {"name": "Replika", "desc": "AI chatbot for companionship and conversation", "url": "https://replika.ai/", "icon": "icons/replika.png", "category": "Conversational"},
    {"name": "Kuki", "desc": "Conversational AI chatbot for entertainment and companionship", "url": "https://www.kuki.ai/", "icon": "icons/kuki.png", "category": "Conversational"},
    {"name": "CopySmith", "desc": "AI writing tool for generating marketing copy", "url": "https://copysmith.ai/", "icon": "icons/copysmith.png", "category": "Writing"},
    {"name": "Rytr", "desc": "AI writing assistant for content creation", "url": "https://rytr.me/", "icon": "icons/rytr.png", "category": "Writing"},
]

# Create placeholder icons with professional styling
def create_placeholder_icon(tool_name, size=(64, 64)):
    """Create a professional placeholder icon with the tool's initial"""
    # Create a gradient background
    base_color = "#6c5ce7"
    img = Image.new('RGB', size, base_color)
    draw = ImageDraw.Draw(img)
    
    # Draw a subtle radial gradient
    center_x, center_y = size[0] // 2, size[1] // 2
    for i in range(0, max(size), 5):
        alpha = int(255 * (1 - i / max(size)))
        color = (108, 92, 231, alpha)
        draw.ellipse([(center_x - i, center_y - i), 
                     (center_x + i, center_y + i)], 
                    outline=color, width=2)
    
    # Add the tool's initial with modern method
    try:
        # Try to use a system font
        if platform.system() == "Windows":
            font_path = "C:/Windows/Fonts/arial.ttf"
        elif platform.system() == "Darwin":  # macOS
            font_path = "/Library/Fonts/Arial.ttf"
        else:  # Linux
            font_path = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
            
        font = ImageFont.truetype(font_path, 24)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Get text bounding box using modern method
    initial = tool_name[0].upper()
    bbox = draw.textbbox((0, 0), initial, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    draw.text(position, initial, fill="white", font=font)
    
    return ImageTk.PhotoImage(img)

class AIToolLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🚀 Premium AI Tools Launcher")
        self.geometry("1200x800")
        self.minsize(1000, 700)
        self.configure(bg="#0f172a")
        
        # Set application icon
        try:
            self.iconbitmap("icons/launcher_icon.ico")
        except:
            pass
        
        # Create a custom style for the application
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        
        # Configure styles with professional color scheme
        self.style.configure("TFrame", background="#0f172a")
        self.style.configure("Header.TFrame", background="#1e293b")
        self.style.configure("Card.TFrame", background="#1e293b", relief="flat", borderwidth=0)
        self.style.configure("HoverCard.TFrame", background="#334155", relief="flat", borderwidth=0)
        self.style.configure("Title.TLabel", background="#1e293b", foreground="#e2e8f0", 
                            font=("Segoe UI", 22, "bold"))
        self.style.configure("Subtitle.TLabel", background="#1e293b", foreground="#94a3b8", 
                            font=("Segoe UI", 11))
        self.style.configure("Category.TLabel", background="#0f172a", foreground="#94a3b8", 
                            font=("Segoe UI", 10, "bold"))
        self.style.configure("Tool.TLabel", background="#1e293b", foreground="#e2e8f0", 
                            font=("Segoe UI", 14, "bold"))
        self.style.configure("Desc.TLabel", background="#1e293b", foreground="#94a3b8", 
                            font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), borderwidth=0,
                            background="#334155", foreground="#e2e8f0")
        self.style.map("TButton", 
                      background=[("active", "#475569")],
                      foreground=[("active", "white")])
        self.style.configure("Accent.TButton", background="#6c5ce7", foreground="white")
        self.style.map("Accent.TButton", 
                      background=[("active", "#857beb")])
        self.style.configure("TEntry", fieldbackground="#1e293b", foreground="#e2e8f0", 
                            font=("Segoe UI", 11))
        
        # Create placeholder icons for tools
        self.icons = {}
        for tool in AI_TOOLS:
            self.icons[tool["name"]] = create_placeholder_icon(tool["name"])
        
        # Setup UI
        self.create_widgets()
        
        # Bind resize event
        self.bind("<Configure>", self.on_window_resize)
        
    def create_widgets(self):
        # Create main container with shadow effect
        self.main_container = ttk.Frame(self, style="TFrame")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header with gradient
        self.header_frame = ttk.Frame(self.main_container, style="Header.TFrame")
        self.header_frame.pack(fill="x", pady=(0, 10))
        
        header_content = ttk.Frame(self.header_frame, style="Header.TFrame")
        header_content.pack(fill="x", padx=30, pady=15)
        
        title_frame = ttk.Frame(header_content, style="Header.TFrame")
        title_frame.pack(side="left", fill="x", expand=True)
        
        self.title_label = ttk.Label(title_frame, text="🚀 Premium AI Tools Launcher", 
                                   style="Title.TLabel")
        self.title_label.pack(anchor="w")
        
        self.subtitle_label = ttk.Label(title_frame, 
                                      text="Access the most powerful AI tools in one place", 
                                      style="Subtitle.TLabel")
        self.subtitle_label.pack(anchor="w")
        
        # Stats frame
        stats_frame = ttk.Frame(header_content, style="Header.TFrame")
        stats_frame.pack(side="right", padx=10)
        
        stats_text = f"{len(AI_TOOLS)} Tools | 8 Categories"
        self.stats_label = ttk.Label(stats_frame, text=stats_text, 
                                   style="Subtitle.TLabel")
        self.stats_label.pack(anchor="e")
        
        # Search and filter section
        self.search_frame = ttk.Frame(self.main_container, style="TFrame")
        self.search_frame.pack(fill="x", padx=10, pady=(10, 20))
        
        # Search bar with icon
        search_container = ttk.Frame(self.search_frame, style="TFrame")
        search_container.pack(fill="x", pady=5)
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_tools)
        self.search_entry = ttk.Entry(search_container, textvariable=self.search_var, 
                                     style="TEntry", font=("Segoe UI", 11))
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=8)
        self.search_entry.insert(0, "Search AI tools...")
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        
        search_icon = ttk.Label(search_container, text="🔍", background="#1e293b", 
                               font=("Segoe UI", 12))
        search_icon.pack(side="left", padx=(10, 0))
        
        # Category filter
        self.categories = sorted(set(tool["category"] for tool in AI_TOOLS if tool["category"]))
        self.category_var = tk.StringVar(value="All")
        
        self.category_frame = ttk.Frame(self.search_frame, style="TFrame")
        self.category_frame.pack(fill="x", pady=(10, 0))
        
        ttk.Label(self.category_frame, text="Filter by category:", 
                 style="Category.TLabel").pack(side="left", padx=(0, 15))
        
        # Create category pills
        for category in ["All"] + self.categories:
            pill = ttk.Frame(self.category_frame, style="Card.TFrame")
            pill.pack(side="left", padx=5, pady=5)
            
            rb = ttk.Radiobutton(pill, text=category, 
                                variable=self.category_var, value=category,
                                command=self.filter_tools,
                                style="Tool.TLabel")
            rb.pack(padx=10, pady=3)
        
        # Tool cards container with shadow effect
        container_frame = ttk.Frame(self.main_container, style="TFrame")
        container_frame.pack(fill="both", expand=True)
        
        self.container = ttk.Frame(container_frame, style="Card.TFrame")
        self.container.pack(fill="both", expand=True, padx=0, pady=0)
        
        self.canvas = tk.Canvas(self.container, bg="#1e293b", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.tools_frame = ttk.Frame(self.canvas, style="TFrame")
        
        self.tools_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.tools_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=2, pady=2)
        self.scrollbar.pack(side="right", fill="y")
        
        # Footer
        self.footer_frame = ttk.Frame(self.main_container, style="Header.TFrame")
        self.footer_frame.pack(fill="x", pady=(10, 0))
        
        button_frame = ttk.Frame(self.footer_frame, style="Header.TFrame")
        button_frame.pack(side="right", padx=20, pady=10)
        
        ttk.Button(button_frame, text="About", 
                  command=self.show_about, style="Accent.TButton").pack(side="left", padx=10)
        ttk.Button(button_frame, text="Exit", 
                  command=self.destroy).pack(side="left", padx=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        self.status_bar = ttk.Label(self.footer_frame, textvariable=self.status_var, 
                                  style="Subtitle.TLabel")
        self.status_bar.pack(side="left", padx=20)
        
        # Load tools
        self.cards = []
        self.load_tools()
        
    def clear_placeholder(self, event):
        if self.search_entry.get() == "Search AI tools...":
            self.search_entry.delete(0, tk.END)
    
    def load_tools(self):
        for tool in AI_TOOLS:
            self.create_card(tool)
        self.layout_tools()
    
    def create_card(self, tool):
        card = ttk.Frame(self.tools_frame, style="Card.TFrame")
        card.bind("<Enter>", lambda e, c=card: self.on_card_enter(c))
        card.bind("<Leave>", lambda e, c=card: self.on_card_leave(c))
        
        # Card content container
        content = ttk.Frame(card, style="Card.TFrame")
        content.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Top section: icon and name
        top_frame = ttk.Frame(content, style="Card.TFrame")
        top_frame.pack(fill="x", pady=(0, 10))
        
        # Tool icon
        icon_label = ttk.Label(top_frame, image=self.icons[tool["name"]], 
                              background="#1e293b")
        icon_label.image = self.icons[tool["name"]]
        icon_label.pack(side="left")
        
        # Tool name and category
        text_frame = ttk.Frame(top_frame, style="Card.TFrame")
        text_frame.pack(side="left", fill="x", expand=True, padx=(15, 0))
        
        name_label = ttk.Label(text_frame, text=tool["name"], style="Tool.TLabel")
        name_label.pack(anchor="w")
        
        category_label = ttk.Label(text_frame, text=tool["category"], 
                                 foreground="#6c5ce7", background="#1e293b",
                                 font=("Segoe UI", 9, "bold"))
        category_label.pack(anchor="w")
        
        # Tool description
        desc_frame = ttk.Frame(content, style="Card.TFrame")
        desc_frame.pack(fill="x", pady=(5, 15))
        
        desc_label = ttk.Label(desc_frame, text=tool["desc"], style="Desc.TLabel", 
                             wraplength=280, justify="left")
        desc_label.pack(anchor="w")
        
        # Open button
        button = ttk.Button(content, text="Launch Tool", style="Accent.TButton",
                           command=lambda url=tool["url"]: self.open_tool(url))
        button.pack(fill="x", pady=(5, 0))
        
        self.cards.append((card, tool))
    
    def on_card_enter(self, card):
        card.configure(style="HoverCard.TFrame")
    
    def on_card_leave(self, card):
        card.configure(style="Card.TFrame")
    
    def open_tool(self, url):
        webbrowser.open(url)
        self.status_var.set(f"Opening tool in browser...")
        self.after(3000, lambda: self.status_var.set("Ready"))
    
    def layout_tools(self):
        # Clear current grid
        for card, _ in self.cards:
            card.grid_forget()
        
        # Get current container width
        container_width = self.container.winfo_width()
        
        # Calculate columns based on container width
        if container_width < 100:
            return  # Skip if container not yet rendered
        
        card_width = 320
        spacing = 20
        columns = max(1, container_width // (card_width + spacing))
        
        # Layout cards in grid
        for i, (card, _) in enumerate(self.cards):
            row = i // columns
            col = i % columns
            card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        
        # Configure grid columns
        for col in range(columns):
            self.tools_frame.grid_columnconfigure(col, weight=1)
    
    def filter_tools(self, *args):
        search_term = self.search_var.get().lower()
        category = self.category_var.get()
        
        # Hide all cards first
        for card, _ in self.cards:
            card.grid_forget()
        
        # Show matching cards
        visible_cards = 0
        for i, (card, tool) in enumerate(self.cards):
            name_match = search_term in tool["name"].lower() if search_term not in ["", "search ai tools..."] else True
            desc_match = search_term in tool["desc"].lower() if search_term not in ["", "search ai tools..."] else True
            category_match = (category == "All") or (tool["category"] == category)
            
            if (name_match or desc_match) and category_match:
                visible_cards += 1
                card.grid(row=i, column=0, padx=15, pady=15, sticky="nsew")
        
        # Update layout
        self.layout_tools()
        
        # Update status
        self.status_var.set(f"Showing {visible_cards} of {len(AI_TOOLS)} tools")
    
    def on_window_resize(self, event):
        if event.widget == self:
            self.layout_tools()
    
    def show_about(self):
        about_window = tk.Toplevel(self)
        about_window.title("About AI Tools Launcher")
        about_window.geometry("500x400")
        about_window.configure(bg="#0f172a")
        about_window.resizable(False, False)
        
        # Center the about window
        window_width = about_window.winfo_reqwidth()
        window_height = about_window.winfo_reqheight()
        position_right = int(self.winfo_x() + (self.winfo_width()/2 - window_width/2))
        position_down = int(self.winfo_y() + (self.winfo_height()/2 - window_height/2))
        about_window.geometry(f"+{position_right}+{position_down}")
        
        # About content
        header = ttk.Frame(about_window, style="Header.TFrame")
        header.pack(fill="x", pady=(0, 20))
        
        title = ttk.Label(header, text="🚀 Premium AI Tools Launcher", 
                        style="Title.TLabel", font=("Segoe UI", 18, "bold"))
        title.pack(padx=20, pady=20)
        
        content = ttk.Frame(about_window, style="TFrame")
        content.pack(fill="both", expand=True, padx=30, pady=(0, 20))
        
        version = ttk.Label(content, text="Version: 2.1.0", 
                          foreground="#94a3b8", background="#0f172a",
                          font=("Segoe UI", 10))
        version.pack(anchor="w", pady=(0, 10))
        
        dev = ttk.Label(content, text="Developed by: Shiboshree Roy", 
                      foreground="#94a3b8", background="#0f172a",
                      font=("Segoe UI", 10))
        dev.pack(anchor="w", pady=(0, 20))
        
        desc = ttk.Label(content, 
                       text="This application provides quick access to the most powerful\n"
                            "AI tools available today. Easily launch your favorite AI\n"
                            "platforms with a single click.",
                       foreground="#94a3b8", background="#0f172a",
                       font=("Segoe UI", 10), justify="left")
        desc.pack(anchor="w", pady=(0, 20))
        
        features = ttk.Label(content, 
                          text="Features:\n"
                               "- Modern, responsive interface\n"
                               "- Search and filter tools by name or category\n"
                               "- Professional card design with hover effects\n"
                               "- One-click access to AI platforms",
                          foreground="#94a3b8", background="#0f172a",
                          font=("Segoe UI", 10), justify="left")
        features.pack(anchor="w", pady=(0, 20))
        
        note = ttk.Label(content, 
                      text="All tools featured in this launcher are available for free\n"
                           "or offer free tiers. Some may require account creation.",
                      foreground="#94a3b8", background="#0f172a",
                      font=("Segoe UI", 9), justify="left")
        note.pack(anchor="w", pady=(0, 20))
        
        close_btn = ttk.Button(about_window, text="Close", 
                             command=about_window.destroy, style="Accent.TButton",
                             width=15)
        close_btn.pack(pady=(0, 20))

if __name__ == "__main__":
    app = AIToolLauncher()
    app.mainloop()