

\# ✈️ AI 旅遊規劃助手



\## 一、專案介紹



本專案使用 Python 搭配 Ollama 與 Qwen2.5:3b 模型，製作一個 AI 旅遊規劃助手。



使用者輸入旅遊地點、旅遊天數、預算及個人喜好後，AI 會自動產生旅遊計畫，包含每日景點、推薦美食、旅遊提醒及預算建議。



\## 二、主要功能



\- 輸入旅遊地點及旅遊天數

\- 根據使用者預算提供規劃建議

\- 依照個人喜好安排每日旅遊景點

\- 提供推薦美食及旅遊提醒

\- 將 AI 產生的結果儲存為 JSON 檔案



\## 三、使用工具與技術



| 工具 | 用途 |

|---|---|

| Python | 撰寫程式及處理使用者輸入 |

| uv | Python 專案及套件管理 |

| Ollama | 在本機執行 AI 模型 |

| Qwen2.5:3b | 理解使用者需求並產生旅遊計畫 |

| Pydantic | 定義資料格式及驗證 AI 輸出 |

| GitHub | 儲存程式碼及管理版本 |

| GitHub Actions | 自動部署作品集網站 |

| GitHub Pages | 公開展示專案作品集 |



\## 四、使用的 AI 功能



本專案使用 Structured Output（結構化輸出）。



透過 Pydantic 建立資料模型，定義旅遊計畫需要的欄位，例如目的地、行程摘要、每日景點、美食及旅遊建議。



程式使用 Pydantic 產生 JSON Schema，傳送給 Ollama，限制 AI 回傳的資料格式，再透過 Pydantic 驗證結果，最後儲存成 JSON 檔案。



\## 五、安裝與執行方式



\### 1. 安裝 Ollama



前往 Ollama 官方網站下載並安裝：



https://ollama.com/



\### 2. 下載 AI 模型



在終端機輸入：



```bash

ollama pull qwen2.5:3b

```



\### 3. 下載專案



```bash

git clone https://github.com/yeyuki0610-rgb/ai-travel-planner.git

cd ai-travel-planner

```



\### 4. 安裝 Python 套件



```bash

uv sync

```



\### 5. 執行程式



```bash

uv run python main.py

```



依照畫面輸入旅遊地點、天數、預算及喜好，即可取得 AI 產生的旅遊規劃。



執行完成後，結果會儲存在 `result.json`。



\## 六、專案檔案結構



```text

ai-travel-planner/

├── .github/

│   └── workflows/

│       └── deploy.yml

├── docs/

│   ├── index.html

│   └── result.json

├── src/

│   └── ai\_travel\_planner/

│       └── \_\_init\_\_.py

├── main.py

├── result.json

├── pyproject.toml

├── uv.lock

└── README.md

```



\## 七、作品集網站



GitHub Pages：



https://yeyuki0610-rgb.github.io/ai-travel-planner/



GitHub Repository：



https://github.com/yeyuki0610-rgb/ai-travel-planner



\## 八、AI 使用與修改說明



開發過程中使用 ChatGPT 協助理解程式架構、產生部分程式碼、解釋錯誤訊息及提供除錯建議。



開發者自行安裝 Python 專案工具、Ollama 及 AI 模型，建立專案環境、安裝套件，並實際執行及測試程式。



開發過程中也依照執行結果調整程式，確認 AI 能夠依照指定的資料格式產生旅遊規劃，並成功儲存 JSON 結果。



\## 九、專案限制



本專案使用 Ollama 在本機執行 AI 模型，因此需要在已安裝 Ollama 及指定模型的電腦上執行。



GitHub Pages 僅負責展示專案介紹及範例執行結果，無法直接執行本機 AI 模型。



