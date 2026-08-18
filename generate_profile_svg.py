#!/usr/bin/env python3
"""
generate_profile_svg.py
Generates dark_mode.svg and light_mode.svg terminal cards for Ravichandra Shinde's GitHub profile.
"""

import os

# 33-line custom ASCII portrait
ASCII_PORTRAIT = [
    "                   .-=+**+=:                    ",
    "               :=#%@@@@@@@@@@#=:                ",
    "            :#@@@@@@@@@@@@@@@@@@%*              ",
    "          -#@@@@@@@@@@@@@@@@@@@@@@%-            ",
    "         *@@@@@@@@@@@@@@@@@@@@@@@@@@#           ",
    "       .%@@@@@@@@@@@@%%%@@@@@@@@@@@@@@-         ",
    "       @@@@@@@@@%#*++++++++===*%@@@@@@@*        ",
    "      :@@@@@@@%#**+++++====--==+*@@@@@@@#       ",
    "      =%@@@@@%#**+++++=========++*%@@@@@@       ",
    "       *@@@@#****++++=====----==+++%@@@@*       ",
    "        @@@*%@@@@@@%**++====++***#*+@@@@        ",
    "       +%@**@@@@@@@@@@%***%@@@@@@@@#%@%         ",
    "      -@%@+*%@@@@@@@@@%+=#@@@@@%%@%*%@#:        ",
    "      .#%%+**#%%@@#%%@*==**##@@%%%*+##*=        ",
    "       +@#+++=+++++*##+-=+++=++++==+#%+         ",
    "       .%%*##*+++++#*+=--=++===--=++*#-         ",
    "        -##%%%#*++*#*+=-:=++=--=+**##+          ",
    "          =@%%%#**#%@@%#*%#+===+**##-           ",
    "           %@%%%#***%@%%##*==++**#%-            ",
    "           =@@%%%%%####********##%*             ",
    "            *@@@@@@@%####*##%%##@%              ",
    "             #@@@@@@@%###%%##%%@%               ",
    "             +@@@@@@@%%%#%%%%@@%                ",
    "             #@@@@@@@%%%#%%@@@%#-               ",
    "            =%%%@@@@@@@@@@@%#*###+=.            ",
    "        .+%@#%%%%@@@@@@@%#******+*@@@%-         ",
    "   .-+#@@@@@%#%%%%%%%####********%@@@@@@%+=-.   ",
    ":+@@@@@@@@@@@%####********+++++*@@@@@@@@@@@@@#+:",
    "@@@@@@@@@@@@@%*++++====+++++++*@@@@@@@@@@@@@@@@@",
    "@@@@@@@@@@@@@@+=+++++++++++=+%@@@@@@@@@@@@@@@@@@",
    "@@@@@@@@@@@@@@@#+========++#@@@@@@@@@@@@@@@@@@@@",
    "@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@",
    "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
]

def build_svg(theme="dark"):
    is_dark = (theme == "dark")
    
    # Palette
    if is_dark:
        stroke_card = "#30363d"
        title_fill = "#8b949e"
        grad_id = "pgd"
        grad_stops = '<stop offset="0" stop-color="#2FBF71"/><stop offset="1" stop-color="#5ad3e0"/>'
        user_color = "#7ee88a"
        at_color = "#8b949e"
        host_color = "#5ad3e0"
        sub_color = "#8b949e"
        divider_color = "#3f4c57"
        key_color = "#5ad3e0"
        val_default = "#c9d1d9"
        val_accent = "#7ee88a"
        val_highlight = "#ecc86e"
        sec_header = "#ecc86e"
    else:
        stroke_card = "#d0d7de"
        title_fill = "#57606a"
        grad_id = "pgl"
        grad_stops = '<stop offset="0" stop-color="#0a7d3b"/><stop offset="1" stop-color="#0e7490"/>'
        user_color = "#1a7f37"
        at_color = "#57606a"
        host_color = "#0969da"
        sub_color = "#57606a"
        divider_color = "#d0d7de"
        key_color = "#0969da"
        val_default = "#24292f"
        val_accent = "#1a7f37"
        val_highlight = "#9a6700"
        sec_header = "#9a6700"

    width = 860
    height = 585
    start_y = 75.0
    line_step = 15.2
    
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="\'JetBrains Mono\',\'SFMono-Regular\',Consolas,\'Liberation Mono\',monospace">')
    svg_lines.append(f'<defs><linearGradient id="{grad_id}" x1="0" y1="0" x2="0.4" y2="1">{grad_stops}</linearGradient></defs>')
    svg_lines.append(f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="14" fill="none" stroke="{stroke_card}" stroke-width="1.4"/>')
    svg_lines.append('<circle cx="24" cy="22.0" r="6" fill="#ff5f56"/>')
    svg_lines.append('<circle cx="44" cy="22.0" r="6" fill="#ffbd2e"/>')
    svg_lines.append('<circle cx="64" cy="22.0" r="6" fill="#27c93f"/>')
    svg_lines.append(f'<line x1="1" y1="41" x2="{width-1}" y2="41" stroke="{stroke_card}" stroke-width="1.2"/>')
    svg_lines.append(f'<text x="{width/2:.1f}" y="25.0" fill="{title_fill}" font-size="13" text-anchor="middle">ravi@ravichandra — neofetch</text>')

    # ASCII portrait lines (left side)
    for i, line in enumerate(ASCII_PORTRAIT):
        y = start_y + i * line_step
        svg_lines.append(f'<text xml:space="preserve" x="20" y="{y:.1f}" font-size="13" fill="url(#{grad_id})">{line}</text>')

    # Right side lines definition: (line_idx, type, data)
    # type "header": (user, host, subtitle)
    # type "divider": ()
    # type "sec_divider": (title, line_len)
    # type "kv": (key, val, val_type) -> val_type in ['default', 'accent', 'highlight']
    
    right_items = [
        (0, "header", ("ravi", "ravichandra", "Full-Stack Engineer · 1800+ LeetCode")),
        (2, "divider", ()),
        (3, "kv", ("OS", "macOS · Linux (Ubuntu)", "default")),
        (4, "kv", ("Education", "B.Tech CSE @ Rishihood / NST ('28)", "accent")),
        (5, "kv", ("LeetCode", "1800+ Rating · Contest Knight", "highlight")),
        (6, "kv", ("Focus", "Scalable Systems & Realtime Eng.", "default")),
        (7, "kv", ("Shell", "/bin/zsh · Turborepo Monorepos", "accent")),
        (9, "kv", ("Ecosystem", "Full-Stack · Realtime · Microservices", "accent")),
        (10, "kv", ("Lang.Core", "TypeScript · JavaScript · Python · SQL", "default")),
        (11, "kv", ("Frontend", "Next.js · React · Tailwind CSS · Canvas", "default")),
        (12, "kv", ("Backend.RT", "Node.js · Express · WebSockets · Prisma", "default")),
        (13, "kv", ("DevOps.DB", "PostgreSQL · Docker · AWS · CI/CD", "default")),
        (15, "kv", ("Now", "Realtime Whiteboards & Stream Engines", "highlight")),
        (16, "kv", ("Architecture", "Sub-50ms Latency · Clean Monorepos", "default")),
        (18, "sec_divider", ("Contact", 32)),
        (19, "kv", ("Email", "ravichandra.shinde2024@nst.rishihood.edu.in", "default")),
        (20, "kv", ("LinkedIn", "in/ravichandrashinde", "accent")),
        (21, "kv", ("GitHub", "@Ravichandra531", "accent")),
        (22, "kv", ("LeetCode", "leetcode.com/u/Ravichandra531", "accent")),
        (23, "kv", ("Location", "India 🇮🇳 · Open for Internships/Roles", "default")),
        (25, "sec_divider", ("Projects", 31)),
        (26, "kv", ("Drawlify", "Realtime collab canvas · <50ms WS sync", "accent")),
        (27, "kv", ("Muzer", "Live stream room & YouTube vote queue", "accent")),
        (28, "kv", ("HireHub", "Full-stack job portal · RBAC & Prisma", "default")),
        (29, "kv", ("EasePay", "ACID digital wallet & webhook pipelines", "default")),
    ]

    x_key = 456.0
    x_val = 558.0

    for item in right_items:
        line_idx = item[0]
        itype = item[1]
        y = start_y + line_idx * line_step
        
        if itype == "header":
            user, host, subtitle = item[2]
            y_sub = start_y + (line_idx + 1) * line_step
            svg_lines.append(f'<text y="{y:.1f}" font-size="13"><tspan xml:space="preserve" x="{x_key}" fill="{user_color}" font-weight="700">{user}</tspan><tspan xml:space="preserve" x="{x_key+32:.1f}" fill="{at_color}">@</tspan><tspan xml:space="preserve" x="{x_key+40:.1f}" fill="{host_color}" font-weight="700">{host}</tspan></text>')
            svg_lines.append(f'<text y="{y_sub:.1f}" font-size="13"><tspan xml:space="preserve" x="{x_key}" fill="{sub_color}">{subtitle}</tspan></text>')
        
        elif itype == "divider":
            svg_lines.append(f'<text y="{y:.1f}" font-size="13"><tspan xml:space="preserve" x="{x_key}" fill="{divider_color}">  ──────────────────────────────────────────</tspan></text>')
            
        elif itype == "sec_divider":
            title, num_dashes = item[2]
            dashes = "─" * num_dashes
            # calculate offset for dashes based on title length
            x_dash = x_key + (len(title) + 3) * 7.8
            svg_lines.append(f'<text y="{y:.1f}" font-size="13"><tspan xml:space="preserve" x="{x_key}" fill="{sec_header}" font-weight="700">  {title} </tspan><tspan xml:space="preserve" x="{x_dash:.1f}" fill="{divider_color}">{dashes}</tspan></text>')
            
        elif itype == "kv":
            key, val, val_type = item[2]
            padded_key = f"  {key}".ljust(11)
            
            if val_type == "accent":
                vf = val_accent
                fw = ' font-weight="700"'
            elif val_type == "highlight":
                vf = val_highlight
                fw = ' font-weight="700"'
            else:
                vf = val_default
                fw = ''
                
            # For longer email, use slightly smaller font size or custom styling if needed
            if key == "Email":
                svg_lines.append(f'<text y="{y:.1f}" font-size="12.5"><tspan xml:space="preserve" x="{x_key}" fill="{key_color}" font-weight="700">{padded_key}</tspan><tspan xml:space="preserve" x="{x_val}" fill="{vf}"{fw}>{val}</tspan></text>')
            else:
                svg_lines.append(f'<text y="{y:.1f}" font-size="13"><tspan xml:space="preserve" x="{x_key}" fill="{key_color}" font-weight="700">{padded_key}</tspan><tspan xml:space="preserve" x="{x_val}" fill="{vf}"{fw}>{val}</tspan></text>')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)

def main():
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    dark_svg = build_svg("dark")
    dark_path = os.path.join(assets_dir, "dark_mode.svg")
    with open(dark_path, "w", encoding="utf-8") as f:
        f.write(dark_svg)
    print(f"Generated {dark_path} ({len(dark_svg)} bytes)")
    
    light_svg = build_svg("light")
    light_path = os.path.join(assets_dir, "light_mode.svg")
    with open(light_path, "w", encoding="utf-8") as f:
        f.write(light_svg)
    print(f"Generated {light_path} ({len(light_svg)} bytes)")

if __name__ == "__main__":
    main()
