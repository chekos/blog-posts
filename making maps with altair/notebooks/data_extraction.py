## Extracts zip files from ../data/raw/ into ../data/interim/

from pathlib import Path
from zipfile import ZipFile

raw_data_path = Path("../data/raw/")
interim_data_path = Path("../data/interim/")

for zipped_file in raw_data_path.glob("*.zip"):
    file = ZipFile(zipped_file)
    print("extracting file zipped_file.name")
    file.extractall(path = (interim_data_path / zipped_file.stem))
    print(f"contents extracted to {(interim_data_path / zipped_file.stem)}")