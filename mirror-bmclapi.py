import os

def replace_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        file_data = file.read()
    
    file_data = file_data.replace(old_text, new_text)
    
    with open(file_path, 'w') as file:
        file.write(file_data)

def process_files(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            process_files(item_path)
        elif item.endswith('.json'):
            replace_in_file(item_path, 'http://dl.liteloader.com/versions', 'https://bmclapi.bangbang93.com/maven/com/mumfrey/liteloader')

            replace_in_file(item_path, 'http://repo.maven.apache.org/maven2', 'https://mirrors.cloud.tencent.com/nexus/repository/maven-public')

            replace_in_file(item_path, 'https://maven.fabricmc.net', 'https://bmclapi2.bangbang93.com/maven')
            replace_in_file(item_path, 'https://maven.modmuss50.me', 'https://bmclapi2.bangbang93.com/maven')

            replace_in_file(item_path, 'https://piston-meta.mojang.com', 'https://bmclapi2.bangbang93.com')
            replace_in_file(item_path, 'https://launchermeta.mojang.com', 'https://bmclapi2.bangbang93.com')
            replace_in_file(item_path, 'https://launcher.mojang.com', 'https://bmclapi2.bangbang93.com')
            replace_in_file(item_path, 'https://piston-data.mojang.com', 'https://bmclapi2.bangbang93.com')
            replace_in_file(item_path, 'https://libraries.minecraft.net', 'https://bmclapi2.bangbang93.com/maven')

            replace_in_file(item_path, 'https://maven.minecraftforge.net', 'https://bmclapi2.bangbang93.com/maven')
            replace_in_file(item_path, 'https://files.minecraftforge.net/maven', 'https://bmclapi2.bangbang93.com/maven')

            replace_in_file(item_path, 'https://maven.neoforged.net/releases', 'https://bmclapi2.bangbang93.com/maven')
            
            # replace_in_file(item_path, 'https://maven.quiltmc.org/repository/release', 'https://bmclapi2.bangbang93.com/maven')


if __name__ == '__main__':
    current_directory = os.getcwd()
    process_files(current_directory)
