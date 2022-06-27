from pathlib import Path
from textwrap import dedent
from collections import defaultdict
from unicodedata import category
import yaml

PROJECT_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = PROJECT_DIR / "docs"
COMPONENTS_DIR = PROJECT_DIR / "components"
CONFIG_YML = PROJECT_DIR / "mkdocs.yml"


def page_content(flows: list[Path]) -> str:
    content = dedent(
        """
        hide:
            -toc

        ```mermaid
        flowchart LR
        {! styles.md !}
    """
    )
    for flow in flows:
        content += f"{{! {flow.relative_to(COMPONENTS_DIR)} !}}\n"
    content += "```\n"
    return content.lstrip()


def flows_list(search_string: str) -> list[Path]:
    return [
        file
        for file in COMPONENTS_DIR.joinpath("flows").iterdir()
        if search_string in file.read_text()
    ]


def ensure_output_directory(path: str, base: Path = DOCS_DIR) -> Path:
    output_dir = base / path
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def update_config(nav: defaultdict, config_file: Path = CONFIG_YML):
    config = yaml.load(config_file.read_text(), Loader=yaml.Loader)

    config["nav"] = [{} for _ in range(len(nav) + 1)]
    config["nav"][0] = {"Home": "index.md"}

    for i, (category, pages) in enumerate(nav.items(), 1):
        config["nav"][i] = {
            category: sorted(
                [
                    {
                        page.stem.replace("_", " ").title(): str(
                            page.relative_to(DOCS_DIR)
                        )
                    }
                    for page in pages
                ],
                key=lambda d: list(d.keys())[0],
            )
        }
    config_file.write_text(yaml.dump(config))


def main():
    nav = defaultdict(list)
    for component_type in ["events", "forms", "sheets"]:
        output_dir = ensure_output_directory(component_type)

        for file in COMPONENTS_DIR.joinpath(component_type).glob("*.md"):
            output_file = output_dir / file.name
            output_file.touch(exist_ok=True)

            output_file.write_text(page_content(flows_list(file.stem)))

            nav[component_type].append(output_file)

    update_config(nav)


if __name__ == "__main__":
    main()
