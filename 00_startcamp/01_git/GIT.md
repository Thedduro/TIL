<details>
<summary><strong>GIT</strong></summary>
<div markdown="1">
    
1. **git의 3가지 영역**
    - **`Working Directory`**: 실제 작업 중인 파일들이 위치하는 영역
    - **`Staging Area`**: `working directory`에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가 및 제외할 수 있는 중간 준비 영역
    - **`Repository`**: 버전 `commit` 이력과 파일들이 영구적으로 저장되는 영역 *(모든 버전과 변경 이력이 기록)*
2. **git 명령어**
    - **`git init`**: 해당 디렉토리가 *(숨김 항목에 `.git` 폴더 추가)*
    - **`git add`** [상대경로(~/Desktop/)]: Staging Area에 추가
    - **`git status`**:
    - **`git commit -m '마크다운 연습(변동)'`**: git 버전 생성
        - **`git config --global user.email "you@example.com"`** 
        - **`git config --global user.name "Your Name"`**
    - **`code ~/.gitconfig`**: VScode에서 열기
    - **`git log`**:
</div>
</details>