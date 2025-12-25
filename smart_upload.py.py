import os, subprocess

REPO_URL = "https://github.com/MKNETID/Gemesak.git" 
STAGING_BRANCH = "update-manifest"

def run_git(command):
    return subprocess.run(command, check=True, shell=True)

# 1. Inisialisasi jika belum ada
if not os.path.exists(".git"):
    run_git("git init")
    run_git(f"git remote add origin {REPO_URL}")

# 2. Buat branch staging yang BENAR-BENAR KOSONG (Orphan)
# Ini memastikan kita tidak mendownload 60rb file ke laptop
run_git(f"git checkout --orphan {STAGING_BRANCH}")

# 3. Masukkan file baru Anda
run_git("git add .")
run_git('git commit -m "Kirim batch file baru"')

# 4. Force Push (Menimpa isi branch staging yang lama agar selalu bersih)
run_git(f"git push origin {STAGING_BRANCH} --force")

print("Berhasil! File baru sudah di GitHub. Sekarang biarkan GitHub Action bekerja.")