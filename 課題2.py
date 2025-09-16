import pandas as pd
import numpy as np

def analyze_scores(csv_file_path):
    """
    CSVファイルから参加者のスコアを読み込み、統計情報を計算する
    
    Args:
        csv_file_path (str): CSVファイルのパス
    
    Returns:
        pandas.DataFrame: 分析結果のデータフレーム
    """
    # CSVファイルを読み込み
    df = pd.read_csv(csv_file_path)
    
    # 各参加者のスコア統計を計算
    score_stats = df.groupby('名前')['スコア'].agg([
        ('平均', 'mean'),
        ('最高', 'max'),
        ('最低', 'min'),
        ('受験回数', 'count')
    ]).round(2)
    
    # インデックスをリセットして名前を列に戻す
    score_stats = score_stats.reset_index()
    
    return score_stats

def display_results(stats_df):
    """
    結果を表形式で表示する
    
    Args:
        stats_df (pandas.DataFrame): 統計データのデータフレーム
    """
    print("=" * 60)
    print("参加者スコア分析結果")
    print("=" * 60)
    print(f"{'名前':<10} {'平均':<8} {'最高':<8} {'最低':<8} {'受験回数':<8}")
    print("-" * 60)
    
    for _, row in stats_df.iterrows():
        print(f"{row['名前']:<10} {row['平均']:<8} {row['最高']:<8} {row['最低']:<8} {row['受験回数']:<8}")
    
    print("=" * 60)

def save_results(stats_df, output_file_path):
    """
    結果をCSVファイルとして保存する
    
    Args:
        stats_df (pandas.DataFrame): 統計データのデータフレーム
        output_file_path (str): 出力ファイルのパス
    """
    stats_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
    print(f"\n結果を {output_file_path} に保存しました。")

def main():
    """
    メイン処理
    """
    # ファイルパス
    input_file = "課題2.csv"
    output_file = "スコア分析結果.csv"
    
    try:
        # スコア分析を実行
        print("CSVファイルを読み込み中...")
        stats_df = analyze_scores(input_file)
        
        # 結果を表示
        display_results(stats_df)
        
        # 結果をCSVファイルとして保存
        save_results(stats_df, output_file)
        
        print("\n処理が完了しました。")
        
    except FileNotFoundError:
        print(f"エラー: {input_file} が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
