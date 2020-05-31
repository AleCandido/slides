# -*- coding: utf-8 -*-
"""
Use this script to update the submodule `reveal.js` with the proper
customization.

- update package.json
- add custom themes
"""
import pathlib
import shutil
import json
import sys
import subprocess
import logging
import logging.config

import toml
import click


def main(here, root):
    logging.config.fileConfig(here / "logging.conf")

    logger = logging.getLogger("make")

    misc = root / "misc"
    my_reveal = root / "my-reveal"

    # make a copy
    # -----------

    shutil.rmtree(my_reveal, ignore_errors=True)
    shutil.copytree(
        root / "reveal.js",
        my_reveal,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".git", ".github"),
    )

    # update package.json
    # -------------------

    package_json = my_reveal / "package.json"
    with open(package_json) as f:
        package_json_content = json.load(f)

    with open(misc / "rm-package.json") as f:
        rm = json.load(f)
    with open(misc / "add-package.json") as f:
        add = json.load(f)

    for d in rm:
        del package_json_content[d]
    package_json_content.update(add)

    with open(package_json, "w") as f:
        json.dump(package_json_content, f, indent=2)

    # load and add configs
    # --------------------

    presentation_toml = "presentation.toml"

    with open(presentation_toml) as f:
        configs = toml.load(f)

    __import__("pprint").pprint(configs)

    shutil.copy2(presentation_toml, my_reveal)

    # add structures
    # --------------

    structure = root / "structures" / configs["structure"]["name"]
    requirements = structure / "requirements.txt"
    structure_configs = structure / "structure.yaml"
    template = structure / "template.html"
    build_script = structure / "build_template.py"

    if click.confirm(
        "Do you want to install the required dependencies?", default=False
    ):
        print("Installing required packages:")
        with open(requirements) as f:
            for line in f.readlines():
                if not line or line[0] == "#":
                    continue
                print(f"  - {line}")

        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements.resolve())]
        )
        # TODO add logs

    # TODO manage configs

    shutil.copy2(build_script, my_reveal)
    shutil.copy2(template, my_reveal)

    # TODO hardcoded files tree, this should depend on the structure chosen
    slides = my_reveal / "src" / "slides"
    slides.mkdir(parents=True, exist_ok=True)
    (slides / "1.html").touch(exist_ok=True)

    # add themes
    # ----------

    # MISSING


if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parent
    root = here / ".."

    main(here, root)
