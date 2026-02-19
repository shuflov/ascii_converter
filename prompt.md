
Build a terminal ASCII art streaming animation service (like parrot.live or ascii.live).

Backend:

Create a streaming HTTP endpoint (/cat or similar) that serves ASCII art frames as a text/plain StreamingResponse
Each frame is preceded by ANSI escape codes (33[H33[2J) to clear the terminal screen, creating smooth animation
Use an async generator that loops infinitely through 4-8 ASCII art frames with ~0.3s delay between frames
Hide/show cursor with 33[?25l / 33[?25h
Also create a /frames JSON endpoint returning all frames + delay for web preview use
ASCII Art:

Design a [githbub_catE — e.g. "sitting cat with a wagging tail", "dancing robot", "swimming fish"] using 4-8 frames
Keep the main body static, only animate the moving part (e.g. tail position changes per frame)
Use raw strings to preserve backslashes
Frontend (landing page):

Dark terminal-themed page (monospace font, black/dark background, green accent text)
Live preview: fetch /frames JSON and cycle through them in a fake terminal window component
Prominent copyable curl command: curl -sL <YOUR_URL>/cat
Minimal — just the preview, the command, and a short description
Usage: Users run curl -sL <url>/cat in their terminal and see an infinitely looping ASCII animation. Ctrl+C to stop.
