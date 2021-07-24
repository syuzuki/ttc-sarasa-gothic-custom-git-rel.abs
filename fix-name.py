#!/usr/bin/env python3

import sys

import fontforge


def main(family, style, in_file, out_file):
    font = fontforge.open(in_file)

    font.appendSFNTName("English (US)", "Family", f"Sarasa Nerd {family} J")
    font.appendSFNTName("Japanese", "Family", f"Sarasa Nerd {family} J")
    font.appendSFNTName("English (US)", "Preferred Family", f"Sarasa Nerd {family} J")
    font.appendSFNTName("Japanese", "Preferred Family", f"Sarasa Nerd {family} J")

    if style:
        style_full = f" {style}"
    else:
        style_full = ""
    font.appendSFNTName(
        "English (US)", "Fullname", f"Sarasa Nerd {family} J{style_full}"
    )
    font.appendSFNTName("Japanese", "Fullname", f"Sarasa Nerd {family} J{style_full}")
    font.appendSFNTName(
        "English (US)", "Compatible Full", f"Sarasa Nerd {family} J{style_full}"
    )
    font.appendSFNTName(
        "Japanese", "Compatible Full", f"Sarasa Nerd {family} J{style_full}"
    )

    if style:
        style_unique = style
    else:
        style_unique = "Regular"
    font.appendSFNTName(
        "English (US)", "UniqueID", f"Sarasa Nerd {family} J {style_unique}"
    )
    font.appendSFNTName(
        "Japanese", "UniqueID", f"Sarasa Nerd {family} J {style_unique}"
    )

    if style:
        style_ps = style.replace(" ", "-")
    else:
        style_ps = "Regular"
    font.appendSFNTName(
        "English (US)",
        "PostScriptName",
        f"Sarasa-Nerd-{family}-J-{style_ps}",
    )

    font.generate(out_file, flags=("opentype", "PfEd-comments"))


if __name__ == "__main__":
    main(*sys.argv[1:5])
