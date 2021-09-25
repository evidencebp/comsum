
import requests

def get_commit_patch(repo_name : str
                     , commit : str) -> str:
    patch_url = "https://github.com/{repo_name}/commit/{commit}.patch".format(repo_name=repo_name
                                                                              , commit=commit)
    patch_read = requests.get(patch_url)

    return patch_read.text

if __name__ == "__main__":
    repo_name = "00-Evan/shattered-pixel-dungeon"
    commit = "0077e36c17ad06573a7eca3c2d63c03b98cfec06"

    # Generates the follofing url and fetches its content
    # https://github.com/00-Evan/shattered-pixel-dungeon/commit/0077e36c17ad06573a7eca3c2d63c03b98cfec06.patch
    print(get_commit_patch(repo_name
                           , commit))
