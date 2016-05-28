success() {
    tput setaf 2
    echo "$@"
    tput setaf 0
    return 0
}

success 'Hello, World!'
