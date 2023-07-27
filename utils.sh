function hard-push-to-repo {
    # Push the content of a folder to the main branch of a repo, resetting the git history, leaving one single commit.
	# Args:
	# 1. directory to push to the repo
    # 2. repo URL (with credentials, e.g. https://gitlab-ci-token:TOKEN@git.eon-cds.de/repos/project.git)

    SRC_DIR="${1}"
    REPO_URL="${2}"

    pushd "${SRC_DIR}"

    git config --global user.name "automated"
    git config --global user.email "automated@eon.com"

    git init --initial-branch=main

    git remote add origin "${REPO_URL}"
    git add .
    git commit -m "Hard push [skip ci]"
    git push -f --set-upstream origin main

    popd
}
