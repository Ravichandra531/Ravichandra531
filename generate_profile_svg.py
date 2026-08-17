#!/usr/bin/env python3
"""
GitHub Profile Neofetch SVG Generator for Ravichandra Shinde (@Ravichandra531)
Inspired by Jitmisra's Neofetch terminal design.
"""

import os
import xml.sax.saxutils as saxutils

# 33 Lines of high-detail developer ASCII art (48 chars wide)
ASCII_ART = [
    r"               ====++*++*#+*                           ",
    r"            -:::==+***#*****+===                       ",
    r"          +=---+*+*%%*+====++==**+=--                  ",
    r"         +++=-**#*%%****=+**=+*#*=*##*++               ",
    r"        +++++****%%#*+***#%##**#####@@@#               ",
    r"        ***+*%#*+#@@%#%@#+*#%@@%@%*##@@*               ",
    r"        -+%@@@%*%%%#@@@%##%@@@@%%%*#%@@*+=             ",
    r"        =*%@@@@@@@%###+++@@@@@@%##*#@@%##*             ",
    r"        -+##%@@@%=*++=-::+%@@@@@@@@@@@@@@              ",
    r"         =+#%@@@#=+*##*+=+*##**%#%@@@@@@@              ",
    r"         **#%@@%+-=+*++*=*++=+===-+#=-%@               ",
    r"         *=%%#@#-:.:::=- .=-:::.:.-*:.=                ",
    r"           ---**:::::==:..-=-::...-=-:                 ",
    r"            :-:=:..:::=*+++-::....---                  ",
    r"              ==-::::-=+**+=--:..:@@#                  ",
    r"                 :::-+++++++=-:::*@                    ",
    r"                 +-:::-=+=-::::-=+                     ",
    r"                  :=-:.:::::-==--@#                    ",
    r"                  -=-+****+++=-=%@@%*                  ",
    r"                  -=:-+*+++=--#@%%%%%#++               ",
    r"                  .#=:----::*@@%#%#%#####**+           ",
    r"              +**:.##=-:. -#@%%#%%%###########*+       ",
    r"          =***+*+.:+*=:. :*######@@###******##%%%%*    ",
    r"      +==+*****##+-:..:.-*#****#@@#***++*******###%%*+ ",
    r"    *++++****+*#*%=..:::*##**+#@%**++=+++********#%%## ",
    r"   =#*##*++******#-...:*%##*+#@%*+===*#*###*******%@%# ",
    r"  =*#+*##*++*+++*#=.  +%%#*+#@#*=-:=#@%%#*+*******#%%%+",
    r"  +#%*###***++=++*+. -%%#**%@*+=::=#@*===*##*****##%*  ",
    r" =**%%%#******=++++.:#%#*#@%#+-:-+#@@***+=+++*######   ",
    r" +#%%@%***###%*++++.*#*+*%#*+-:=*%@@#++==+**#####*%*   ",
    r"=+*%%@%**####%%++=++#*+*%#*+--+#@@@@++*##%%%%%#***#    ",
    r"-++++##*#*++*#@*==+#+=#%*+=--+%@@@@#**+====+*#####**   ",
    r"    %%@##****%@#+=+%+#%*+=--*%@@@@*+--===++***##**     ",
]

def escape(s: str) -> str:
    return saxutils.escape(s)

def generate_svg(theme="dark") -> str:
    is_dark = theme == "dark"

    # Theme colors
    border_color = "#30363d" if is_dark else "#d0d7de"
    header_text_color = "#8b949e" if is_dark else "#57606a"
    sep_color = "#3f4c57" if is_dark else "#d0d7de"
    
    # Text colors
    user_color = "#7ee88a" if is_dark else "#1a7f37"
    at_color = "#8b949e" if is_dark else "#57606a"
    host_title_color = "#5ad3e0" if is_dark else "#0969da"
    subtitle_color = "#8b949e" if is_dark else "#57606a"
    
    label_color = "#5ad3e0" if is_dark else "#0969da"
    value_color = "#c9d1d9" if is_dark else "#24292f"
    accent_green = "#7ee88a" if is_dark else "#1a7f37"
    accent_gold = "#ecc86e" if is_dark else "#9a6700"
    
    grad_id = "pgd" if is_dark else "pgl"
    grad_start = "#2FBF71" if is_dark else "#0a7d3b"
    grad_end = "#5ad3e0" if is_dark else "#0e7490"

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="841" height="583" viewBox="0 0 841 583" font-family="\'JetBrains Mono\',\'SFMono-Regular\',Consolas,\'Liberation Mono\',monospace">',
        f'<defs><linearGradient id="{grad_id}" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="{grad_start}"/><stop offset="1" stop-color="{grad_end}"/></linearGradient></defs>',
        f'<rect x="1" y="1" width="839" height="581" rx="14" fill="none" stroke="{border_color}" stroke-width="1.4"/>',
        '<circle cx="24" cy="22.0" r="6" fill="#ff5f56"/>',
        '<circle cx="44" cy="22.0" r="6" fill="#ffbd2e"/>',
        '<circle cx="64" cy="22.0" r="6" fill="#27c93f"/>',
        f'<line x1="1" y1="41" x2="840" y2="41" stroke="{border_color}" stroke-width="1.2"/>',
        f'<text x="420.5" y="25.0" fill="{header_text_color}" font-size="13" text-anchor="middle">ravi@ravichandra — neofetch</text>',
    ]

    # Render left-side ASCII art lines
    start_y = 75.0
    line_step = 15.2

    for i, line in enumerate(ASCII_ART):
        y = start_y + i * line_step
        # Escape line for XML
        esc_line = escape(line)
        svg_lines.append(
            f'<text xml:space="preserve" x="20" y="{y:.1f}" font-size="13" fill="url(#{grad_id})">{esc_line}</text>'
        )

    # Right-side spec content mapping (index -> content)
    # Line 0 (y=75.0): ravi@ravichandra
    svg_lines.append(
        f'<text y="75.0" font-size="13">'
        f'<tspan xml:space="preserve" x="456.0" fill="{user_color}" font-weight="700">ravi</tspan>'
        f'<tspan xml:space="preserve" x="488.0" fill="{at_color}">@</tspan>'
        f'<tspan xml:space="preserve" x="496.0" fill="{host_title_color}" font-weight="700">ravichandra</tspan>'
        f'</text>'
    )

    # Line 1 (y=90.2): Subtitle
    svg_lines.append(
        f'<text y="90.2" font-size="13">'
        f'<tspan xml:space="preserve" x="456.0" fill="{subtitle_color}">Full Stack &amp; Systems Engineer · Builder</tspan>'
        f'</text>'
    )

    # Line 2 (y=105.4): Separator
    svg_lines.append(
        f'<text y="105.4" font-size="13">'
        f'<tspan xml:space="preserve" x="456.0" fill="{sep_color}">  ────────────────────────────────────────</tspan>'
        f'</text>'
    )

    def spec_row(y_val, label, value, val_color=value_color, val_bold=False):
        b_attr = ' font-weight="700"' if val_bold else ''
        return (
            f'<text y="{y_val:.1f}" font-size="13">'
            f'<tspan xml:space="preserve" x="456.0" fill="{label_color}" font-weight="700">  {label:<11}</tspan>'
            f'<tspan xml:space="preserve" x="551.5" fill="{val_color}"{b_attr}>{escape(value)}</tspan>'
            f'</text>'
        )

    def section_header(y_val, title):
        line_chars = "─" * (39 - len(title))
        return (
            f'<text y="{y_val:.1f}" font-size="13">'
            f'<tspan xml:space="preserve" x="456.0" fill="{accent_gold}" font-weight="700">  {title} </tspan>'
            f'<tspan xml:space="preserve" x="{456.0 + (len(title)+3)*7.8:.1f}" fill="{sep_color}">{line_chars}</tspan>'
            f'</text>'
        )

    # Spec lines
    # Line 3 (120.6)
    svg_lines.append(spec_row(120.6, "OS", "macOS · Linux (Ubuntu / Arch)"))
    # Line 4 (135.8)
    svg_lines.append(spec_row(135.8, "Uptime", "~3 yrs · 0 → Production Engineer", val_color=accent_green))
    # Line 5 (151.0)
    svg_lines.append(spec_row(151.0, "Host", "100xDevs Cohort · Full Stack Dev"))
    # Line 6 (166.2)
    svg_lines.append(spec_row(166.2, "Kernel", "B.Tech Computer Science & Eng."))
    # Line 7 (181.4)
    svg_lines.append(spec_row(181.4, "Shell", "/bin/zsh · fullstack-artisan", val_color=accent_green))
    
    # Line 9 (211.8)
    svg_lines.append(spec_row(211.8, "Ecosystem", "Full-Stack · Systems · Realtime", val_color=accent_green, val_bold=True))
    # Line 10 (227.0)
    svg_lines.append(spec_row(227.0, "Lang.Core", "TypeScript · Rust · JavaScript · Python · C++"))
    # Line 11 (242.2)
    svg_lines.append(spec_row(242.2, "Lang.Web", "Next.js 14 · React · Node.js · Express"))
    # Line 12 (257.4)
    svg_lines.append(spec_row(257.4, "Lang.Ops", "Docker · AWS · Terraform · Kafka · K8s"))
    # Line 13 (272.6)
    svg_lines.append(spec_row(272.6, "Databases", "PostgreSQL · MongoDB · Redis · Prisma"))

    # Line 15 (303.0)
    svg_lines.append(spec_row(303.0, "Now", "Building Scalable Realtime & Web3 Apps", val_color=accent_gold, val_bold=True))
    # Line 16 (318.2)
    svg_lines.append(spec_row(318.2, "Focus", "Distributed Systems · Low-Latency Infra"))

    # Line 18 (348.6): Contact Header
    svg_lines.append(section_header(348.6, "Contact"))
    # Line 19 (363.8)
    svg_lines.append(spec_row(363.8, "Email", "ruchitrshinde@gmail.com"))
    # Line 20 (379.0)
    svg_lines.append(spec_row(379.0, "LinkedIn", "in/ravichandrashinde", val_color=accent_green, val_bold=True))
    # Line 21 (394.2)
    svg_lines.append(spec_row(394.2, "GitHub", "@Ravichandra531", val_color=accent_green))
    # Line 22 (409.4)
    svg_lines.append(spec_row(409.4, "Portfolio", "ravichandrashinde.dev"))
    # Line 23 (424.6)
    svg_lines.append(spec_row(424.6, "Location", "India 🇮🇳 · Remote Open"))

    # Line 25 (455.0): Highlights Header
    svg_lines.append(section_header(455.0, "Highlights"))
    # Line 26 (470.2)
    svg_lines.append(spec_row(470.2, "Drawlify", "Realtime collab canvas & whiteboard", val_color=accent_green, val_bold=True))
    # Line 27 (485.4)
    svg_lines.append(spec_row(485.4, "Muzer", "Interactive collaborative music room", val_color=accent_green, val_bold=True))
    # Line 28 (500.6)
    svg_lines.append(spec_row(500.6, "EasePay", "Modern payment wallet & webhook flow"))
    # Line 29 (515.8)
    svg_lines.append(spec_row(515.8, "OpenSrc", "11+ Repos · Microservices & TurboRepo"))

    svg_lines.append("</svg>")
    return "\n".join(svg_lines)

def main():
    os.makedirs("assets", exist_ok=True)
    
    dark_svg = generate_svg(theme="dark")
    with open("assets/dark_mode.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
    print("✅ Generated assets/dark_mode.svg")

    light_svg = generate_svg(theme="light")
    with open("assets/light_mode.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
    print("✅ Generated assets/light_mode.svg")

if __name__ == "__main__":
    main()
