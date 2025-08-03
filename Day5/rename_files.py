import os

directory = "test_files"
prefix = "renamed_"

if not os.path.exists(directory):
    print(f"❌ Error: Directory '{directory}' not found!")
    exit(1)

for count, filename in enumerate(os.listdir(directory), start=1):
    old_path = os.path.join(directory, filename)
    if os.path.isfile(old_path):
        new_name = f"{prefix}{count}.txt"
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_name}")

print("🎉 Renaming completed!")
