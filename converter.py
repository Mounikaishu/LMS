from pathlib import Path
from docling.document_converter import DocumentConverter

converter = DocumentConverter()


def convert_to_markdown(input_file: Path, output_file: Path):
    """
    Converts a supported document (PDF, DOCX, PPTX, etc.)
    into Markdown using Docling.
    """

    result = converter.convert(str(input_file))

    markdown = result.document.export_to_markdown()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    return output_file