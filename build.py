#!/usr/bin/env python3
import os
import shutil
import http.server
import socketserver
import markdown

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(ROOT_DIR, '_site')

def build_site():
    print("🔨 Generating FreeWiki preview site...")
    os.makedirs(DIST_DIR, exist_ok=True)

    # Copy assets & favicon
    assets_src = os.path.join(ROOT_DIR, 'assets')
    assets_dst = os.path.join(DIST_DIR, 'assets')
    if os.path.exists(assets_src):
        if os.path.exists(assets_dst):
            shutil.rmtree(assets_dst)
        shutil.copytree(assets_src, assets_dst)

    icon_src = os.path.join(ROOT_DIR, 'link.png')
    if os.path.exists(icon_src):
        shutil.copy(icon_src, DIST_DIR)

    # Read default layout template
    layout_path = os.path.join(ROOT_DIR, '_layouts', 'default.html')
    with open(layout_path, 'r', encoding='utf-8') as f:
        layout = f.read()

    md_files = [f for f in os.listdir(ROOT_DIR) if f.endswith('.markdown')]
    md_converter = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'codehilite'])

    for md_file in md_files:
        path = os.path.join(ROOT_DIR, md_file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        title = md_file.replace('.markdown', '').replace('-', ' ').title()
        body_md = content

        # Parse front matter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = parts[1]
                body_md = parts[2]
                for line in fm.splitlines():
                    if line.startswith('title:'):
                        title = line.split('title:', 1)[1].strip()

        md_converter.reset()
        body_html = md_converter.convert(body_md)

        # Replace Jekyll Liquid tags
        page_html = layout
        page_html = page_html.replace('{{ site.lang | default: "en-US" }}', 'en-US')
        page_html = page_html.replace("{{ '/link.png' | relative_url }}", "./link.png")
        page_html = page_html.replace('{% seo %}', '')
        page_html = page_html.replace("{{ '/assets/css/style.css?v=' | append: site.github.build_revision | relative_url }}", "./assets/css/style.css")
        page_html = page_html.replace('{% include head-custom.html %}', '')
        page_html = page_html.replace('{{ site.title | default: site.github.repository_name }}', 'The Free Wiki')
        page_html = page_html.replace('{{ page.title | default: site.title | default: site.github.repository_name }}', title)
        page_html = page_html.replace('{{ site.description | default: site.github.project_tagline }}', 'A collection of Linux tips, tricks, and fixes.')
        page_html = page_html.replace("{{ site.github.owner_url | default: 'https://github.com/soimuen11' }}", "https://github.com/soimuen11")
        page_html = page_html.replace("{{ site.github.owner_name | default: 'soimuen11' }}", "soimuen11")
        page_html = page_html.replace("{{ site.github.repository_url | default: 'https://github.com/soimuen11/FreeWiki' }}", "https://github.com/soimuen11/FreeWiki")
        page_html = page_html.replace("{{ '/index.html' | relative_url }}", "./index.html")
        page_html = page_html.replace("{{ '/issues.html' | relative_url }}", "./issues.html")
        page_html = page_html.replace("{{ '/tips-and-tricks.html' | relative_url }}", "./tips-and-tricks.html")
        page_html = page_html.replace("{{ '/ffmpeg.html' | relative_url }}", "./ffmpeg.html")
        page_html = page_html.replace("{{ '/resources.html' | relative_url }}", "./resources.html")
        page_html = page_html.replace("{{ '/scripts.html' | relative_url }}", "./scripts.html")
        page_html = page_html.replace('{{ content }}', body_html)
        page_html = page_html.replace('{{ \'now\' | date: "%Y" }}', '2026')

        out_name = md_file.replace('.markdown', '.html')
        out_path = os.path.join(DIST_DIR, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)

    print("✅ Site generated in _site/")

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.exists('404.html'):
            with open('404.html', 'rb') as f:
                content = f.read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            super().send_error(code, message, explain)

def serve_site(default_port=8000):
    os.chdir(DIST_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    port = default_port
    
    for attempt in range(10):
        try:
            with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
                print(f"🚀 Serving FreeWiki preview at http://localhost:{port}")
                print("Press Ctrl+C to stop.")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\n👋 Server stopped.")
                break
        except OSError as e:
            if e.errno == 98: # Address already in use
                port = default_port + attempt + 1
            else:
                raise e

if __name__ == "__main__":
    build_site()
    serve_site()
