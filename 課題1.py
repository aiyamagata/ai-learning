import random

def number_guessing_game():
    """
    1～100の数当てゲーム
    コンピューターが選んだ数字をユーザーが当てるゲーム
    """
    print("=== 数当てゲーム ===")
    print("コンピューターが1～100の間の数字を選びました。")
    print("その数字を当ててみてください！")
    print("-" * 40)
    
    # 1～100のランダムな数字を生成
    target_number = random.randint(1, 100)
    attempts = 0  # 試行回数をカウント
    
    while True:
        try:
            # ユーザーからの入力を取得
            guess = int(input("あなたの予想を入力してください (1-100): "))
            attempts += 1
            
            # 入力値の範囲チェック
            if guess < 1 or guess > 100:
                print("エラー: 1～100の間の数字を入力してください。")
                attempts -= 1  # 無効な入力は試行回数にカウントしない
                continue
            
            # 正解かどうかチェック
            if guess == target_number:
                print(f"\n🎉 正解です！おめでとうございます！")
                print(f"答えは {target_number} でした。")
                print(f"試行回数: {attempts}回")
                break
            elif guess < target_number:
                print("💡 もっと大きい数字です。")
            else:
                print("💡 もっと小さい数字です。")
                
        except ValueError:
            print("エラー: 数字を正しく入力してください。")
        except KeyboardInterrupt:
            print("\n\nゲームを中断しました。")
            print(f"答えは {target_number} でした。")
            break

def main():
    """
    メイン関数
    ゲームの実行を制御します
    """
    while True:
        number_guessing_game()
        
        # もう一度プレイするかどうか確認
        play_again = input("\nもう一度プレイしますか？ (y/n): ").lower()
        if play_again != 'y':
            print("ゲームを終了します。ありがとうございました！")
            break

if __name__ == "__main__":
    main()
