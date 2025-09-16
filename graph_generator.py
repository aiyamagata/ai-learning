#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt

# --- 日本語フォント対策（簡単） ---
try:
    import japanize_matplotlib  # pip install japanize-matplotlib
except Exception:
    # japanize が無い場合は rcParams でフォールバック（環境に応じてフォント名を変えてください）
    import matplotlib as mpl
    mpl.rcParams['font.family'] = ['Noto Sans CJK JP', 'Meiryo', 'IPAPGothic', 'sans-serif']

def find_column(df, candidates):
    """候補リストから最初に見つかった列名を返す"""
    low = {c.lower(): c for c in df.columns}
    for cand in candidates:
        for k,v in low.items():
            if cand in k:
                return v
    return None

def main(csv_path='課題3.csv'):
    df = pd.read_csv(csv_path, encoding='utf-8-sig')
    # 列名の空白トリム
    df.columns = [c.strip() for c in df.columns]

    # カラム推定（'所属' と 'スコア' に当たる列を自動検出）
    aff_col = find_column(df, ['所属','section','group','department','affiliation'])
    score_col = find_column(df, ['score','スコア','点','点数','score'])

    # フォールバック
    if aff_col is None:
        # 非数値の最初の列を所属と判断
        for c in df.columns:
            if not pd.api.types.is_numeric_dtype(df[c]):
                aff_col = c
                break
    if score_col is None:
        # 数値列の中で最もらしいものを採用
        for c in df.columns:
            if pd.api.types.is_numeric_dtype(df[c]):
                score_col = c
                break

    if aff_col is None or score_col is None:
        print("エラー: 所属列またはスコア列が見つかりません。CSVのヘッダを確認してください。")
        print("検出された列:", df.columns.tolist())
        return

    # スコアを数値に変換（不正な値は NaN に）
    df[score_col] = pd.to_numeric(df[score_col], errors='coerce')

    # --- 円グラフ: 所属ごとの参加者数割合 ---
    counts = df[aff_col].fillna("(不明)").value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90, counterclock=False)
    plt.title('所属ごとの参加者割合')
    plt.axis('equal')  # 真円にする
    plt.tight_layout()
    plt.savefig('pie_chart.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("saved pie_chart.png")

    # --- 棒グラフ: 所属ごとの平均スコア ---
    avg_by_aff = df.groupby(aff_col)[score_col].mean().dropna().sort_values(ascending=False)
    plt.figure(figsize=(10,6))
    plt.bar(avg_by_aff.index.astype(str), avg_by_aff.values)
    plt.xlabel('所属')
    plt.ylabel('平均スコア')
    plt.title('所属ごとの平均スコア')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('bar_chart.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("saved bar_chart.png")

    # --- ヒストグラム: スコアの分布 ---
    scores = df[score_col].dropna()
    plt.figure(figsize=(8,5))
    plt.hist(scores.values, bins=10, edgecolor='black')  # ← ここがヒストグラム。棒グラフではない
    plt.xlabel('スコア')
    plt.ylabel('人数（度数）')
    plt.title('スコアの分布（ヒストグラム）')
    plt.tight_layout()
    plt.savefig('histogram.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("saved histogram.png")

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '課題3.csv'
    main(path)
