from llama_index.core.tools import FunctionTool
import os


notes_dir = os.path.join('data', 'notes.txt')

def save_notes(notes: str) -> str:
    if not os.path.exists(notes_dir):
        open(notes_dir, 'w').close()

    with open(notes_dir, 'a') as f:
        f.writelines(notes + '\n')

    return "Notes saved successfully."


notes_tool = FunctionTool.from_defaults(
    fn=save_notes,
    name="save_notes",
    description="Save notes to a file for the user.",
)