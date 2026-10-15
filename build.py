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

    # Copy robots.txt & CNAME
    robots_src = os.path.join(ROOT_DIR, 'robots.txt')
    if os.path.exists(robots_src):
        shutil.copy(robots_src, DIST_DIR)

    cname_src = os.path.join(ROOT_DIR, 'CNAME')
    if os.path.exists(cname_src):
        shutil.copy(cname_src, DIST_DIR)

    # Read default layout template
    layout_path = os.path.join(ROOT_DIR, '_layouts', 'default.html')
    with open(layout_path, 'r', encoding='utf-8') as f:
        layout = f.read()

    md_files = [f for f in os.listdir(ROOT_DIR) if f.endswith('.markdown')]
    md_converter = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'codehilite'])
    default_site_desc = "A curated, open-source knowledge base for Linux system administration, shell scripting, FFmpeg mastery, terminal diagnostics, and power-user workflows."

    for md_file in md_files:
        path = os.path.join(ROOT_DIR, md_file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        title = md_file.replace('.markdown', '').replace('-', ' ').title()
        description = default_site_desc
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
                    elif line.startswith('description:'):
                        raw_desc = line.split('description:', 1)[1].strip()
                        description = raw_desc.strip('"\'')

        out_name = md_file.replace('.markdown', '.html')
        canonical_url = f"https://freewiki.phiannetta.xyz/{out_name}"
        page_full_title = f"{title} | The Free Wiki" if title != "The Free Wiki" else "The Free Wiki - Linux Sysadmin, Terminal & FFmpeg Knowledge Base"

        seo_tags = f"""<!-- Begin FreeWiki SEO -->
<title>{page_full_title}</title>
<meta name="generator" content="FreeWiki" />
<meta property="og:title" content="{title}" />
<meta name="author" content="Philippe Iannetta" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="{description}" />
<meta property="og:description" content="{description}" />
<link rel="canonical" href="{canonical_url}" />
<meta property="og:url" content="{canonical_url}" />
<meta property="og:site_name" content="The Free Wiki" />
<meta property="og:image" content="https://freewiki.phiannetta.xyz/link.png" />
<meta property="og:type" content="{'website' if out_name == 'index.html' else 'article'}" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="https://freewiki.phiannetta.xyz/link.png" />
<meta name="twitter:site" content="@soimuen11" />
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","headline":"{title}","name":"The Free Wiki","description":"{description}","url":"{canonical_url}","author":{{"@type":"Person","name":"Philippe Iannetta"}}}}
</script>
<!-- End FreeWiki SEO -->"""

        md_converter.reset()
        body_html = md_converter.convert(body_md)

        # Replace Jekyll Liquid tags
        page_html = layout
        page_html = page_html.replace('{{ site.lang | default: "en-US" }}', 'en-US')
        page_html = page_html.replace("{{ '/link.png' | relative_url }}", "./link.png")
        page_html = page_html.replace('{% seo %}', seo_tags)
        page_html = page_html.replace("{{ '/assets/css/style.css?v=' | append: site.github.build_revision | relative_url }}", "./assets/css/style.css")
        page_html = page_html.replace('{% include head-custom.html %}', '')
        page_html = page_html.replace('{{ site.title | default: site.github.repository_name }}', 'The Free Wiki')
        page_html = page_html.replace('{{ page.title | default: site.title | default: site.github.repository_name }}', title)
        page_html = page_html.replace('{{ page.description | default: site.description | default: site.github.project_tagline }}', description)
        page_html = page_html.replace('{{ site.description | default: site.github.project_tagline }}', description)
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

        out_path = os.path.join(DIST_DIR, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)

    # Generate sitemap.xml
    sitemap_entries = []
    base_url = "https://freewiki.phiannetta.xyz"
    for md_f in sorted(md_files):
        if md_f == '404.markdown':
            continue
        h_name = md_f.replace('.markdown', '.html')
        loc = f"{base_url}/{h_name}"
        prio = "1.0" if h_name == "index.html" else "0.8"
        sitemap_entries.append(f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>{prio}</priority>\n  </url>")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>"""
    with open(os.path.join(DIST_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

    print("✅ Site generated in _site/ with full SEO & sitemap")

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
