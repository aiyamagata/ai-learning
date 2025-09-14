def calculator():
    """
    簡単な計算機プログラム
    ユーザーから2つの数値と四則演算子を入力させ、結果を表示します
    """
    print("=== 簡単な計算機プログラム ===")
    
    try:
        # 最初の数値を入力
        num1 = float(input("最初の数値を入力してください: "))
        
        # 演算子を入力
        operator = input("演算子を入力してください (+, -, *, /): ")
        
        # 有効な演算子かチェック
        if operator not in ['+', '-', '*', '/']:
            print("エラー: 無効な演算子です。+, -, *, / のいずれかを入力してください。")
            return
        
        # 2番目の数値を入力
        num2 = float(input("2番目の数値を入力してください: "))
        
        # 計算を実行
        if operator == '+':
            result = num1 + num2
            operation = "足し算"
        elif operator == '-':
            result = num1 - num2
            operation = "引き算"
        elif operator == '*':
            result = num1 * num2
            operation = "掛け算"
        elif operator == '/':
            if num2 == 0:
                print("エラー: ゼロで割ることはできません。")
                return
            result = num1 / num2
            operation = "割り算"
        
        # 結果を表示
        print(f"\n=== 計算結果 ===")
        print(f"{num1} {operator} {num2} = {result}")
        print(f"操作: {operation}")
        
    except ValueError:
        print("エラー: 数値を正しく入力してください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def main():
    """
    メイン関数
    プログラムの実行を制御します
    """
    while True:
        calculator()
        
        # 続行するかどうか確認
        continue_calc = input("\n別の計算を行いますか？ (y/n): ").lower()
        if continue_calc != 'y':
            print("計算機を終了します。ありがとうございました！")
            break

if __name__ == "__main__":
    main()
