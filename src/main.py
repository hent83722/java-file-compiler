import os
import subprocess

SRC_DIR = 'src'
OUT_DIR = 'out'
JAR_NAME = 'program.jar'
MAIN_CLASS = 'com.example.Main' 


JAVA_HOME = "/usr/lib/jvm/java-24-openjdk/bin"
env = os.environ.copy()
env["PATH"] += os.pathsep + JAVA_HOME

def compile_java():
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    java_files = []
    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))

    if not java_files:
        print("No Java files found.")
        return

    subprocess.run(['javac', '-d', OUT_DIR] + java_files, check=True, env=env)

def create_manifest():
    manifest = f"Main-Class: {MAIN_CLASS}\n"
    with open("manifest.txt", "w") as f:
        f.write(manifest)

def package_jar():
    create_manifest()
    subprocess.run(['jar', 'cfm', JAR_NAME, 'manifest.txt', '-C', OUT_DIR, '.'], check=True, env=env)
    print(f"\nCreated JAR: {JAR_NAME}")

def clean_up():
    os.remove('manifest.txt')

if __name__ == "__main__":
    compile_java()
    package_jar()
    clean_up()
