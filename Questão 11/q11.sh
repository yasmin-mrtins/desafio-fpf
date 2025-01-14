
USER_NAME="YasminAndrade"

mkdir -p "$USER_NAME/resultado"

FILE_URL="https://vanilton.net/v1/download/zip.zip"

FILE_NAME="$USER_NAME/zip.zip"

wget -O "$FILE_NAME" "$FILE_URL"

unzip "$FILE_NAME" -d "$USER_NAME/resultado"

rm "$FILE_NAME"

echo "Arquivos processados e salvos em: $USER_NAME/resultado"
