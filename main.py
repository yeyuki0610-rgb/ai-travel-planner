
from ollama import chat
from pydantic import BaseModel


# 定義每天的旅遊行程
class DayPlan(BaseModel):
    day: int
    title: str
    attractions: list[str]
    food: str
    tips: str


# 定義完整旅遊計畫
class TravelPlan(BaseModel):
    destination: str
    summary: str
    days: list[DayPlan]
    budget_advice: str


def main():
    print("================================")
    print("       AI 旅遊規劃助手")
    print("================================")

    destination = input("請輸入旅遊地點：")
    days = input("請輸入旅遊天數：")
    budget = input("請輸入旅遊預算（台幣）：")
    interests = input("請輸入旅遊喜好：")

    print("\nAI 正在幫你規劃行程，請稍候...\n")

    prompt = f"""
    請幫使用者規劃旅遊行程。

    旅遊地點：{destination}
    旅遊天數：{days}
    預算：{budget} 台幣
    旅遊喜好：{interests}

    請使用繁體中文。
    請依照天數安排每天的景點、美食及旅遊建議。
    預算建議請考慮使用者提供的預算。
    """

    try:
        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            format=TravelPlan.model_json_schema()
        )

        result = TravelPlan.model_validate_json(
            response.message.content
        )

        print("========== AI 旅遊規劃結果 ==========")
        print("目的地：", result.destination)
        print("行程摘要：", result.summary)

        for day in result.days:
            print(f"\n第 {day.day} 天：{day.title}")

            print("景點：")
            for attraction in day.attractions:
                print("-", attraction)

            print("推薦美食：", day.food)
            print("旅遊提醒：", day.tips)

        print("\n預算建議：", result.budget_advice)

        # 儲存 JSON 結果
        with open("result.json", "w", encoding="utf-8") as file:
            file.write(result.model_dump_json(indent=2))

        print("\n行程已儲存至 result.json！")

    except Exception as e:
        print("執行發生錯誤：", e)


if __name__ == "__main__":
    main()
