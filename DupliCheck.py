import os
import hashlib
from collections import defaultdict

def calculate_hash(file_path: str, block_size: int = 65536) -> str:
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def find_duplicates(folder_path: str) -> List[List[str]]:
    hash_map = defaultdict(list)
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)
            hash_map[file_hash].append(file_path)

    for hash_value, file_paths in hash_map.items():
        if len(file_paths) > 1:
            duplicates.append(file_paths)

    return duplicates

def delete_files(file_paths: List[str]) -> None:
    archivo_a_mantener = file_paths[0]  # Mantén el primer archivo de la lista
    for file_path in file_paths:
        if file_path != archivo_a_mantener:
            os.remove(file_path)
            print(f"Eliminado: {file_path}")

if __name__ == "__main__":
    folder_to_scan = "./imagen_fusionada"
    duplicate_groups = find_duplicates(folder_to_scan)

    if not duplicate_groups:
        print("No se encontraron imágenes duplicadas.")
    else:
        print("Imágenes duplicadas encontradas.")
        # print(duplicate_groups)
        for group in duplicate_groups:
            delete_files(group)
            # print("\n".join(group))
            # print("-" * 30)
        
