#!/bin/bash

# ✅ 프로그래머스 풀이 자동 커밋 스크립트
# 사용법: ./submit.sh "문제이름" [레벨]
# 예시:  ./submit.sh "두_정수_사이의_합" 1

PROBLEM_NAME=$1
LEVEL=${2:-0}

if [ -z "$PROBLEM_NAME" ]; then
  echo "❌ 문제 이름을 입력하세요."
  echo "   사용법: ./submit.sh \"문제이름\" [레벨]"
  echo "   예시:   ./submit.sh \"두_정수_사이의_합\" 1"
  exit 1
fi

# 레벨별 폴더 경로
FOLDER="Level${LEVEL}"
FILE_PATH="${FOLDER}/${PROBLEM_NAME}.py"

# 폴더 없으면 생성
mkdir -p "$FOLDER"

# 파일 없으면 템플릿 생성
if [ ! -f "$FILE_PATH" ]; then
  cat > "$FILE_PATH" << EOF
# 프로그래머스 - ${PROBLEM_NAME}
# 레벨: ${LEVEL}
# 날짜: $(date +%Y-%m-%d)

def solution():
    pass
EOF
  echo "📄 파일 생성됨: ${FILE_PATH}"
  echo "   풀이 작성 후 다시 ./submit.sh 를 실행하세요!"
  exit 0
fi

# git add & commit & push
DATE=$(date +"%Y-%m-%d %H:%M")
COMMIT_MSG="[Level${LEVEL}] ${PROBLEM_NAME} - ${DATE}"

git add "$FILE_PATH"
git commit -m "$COMMIT_MSG"
git push origin main

echo ""
echo "🌱 잔디 심기 완료!"
echo "   커밋: ${COMMIT_MSG}"
