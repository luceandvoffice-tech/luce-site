import streamlit as st

# 1. ページの設定
st.set_page_config(page_title="Luce and v", page_icon="🌿", layout="centered")

# ★右下の赤いバー、右上のメニュー、Forkボタンなどを完全に隠す設定
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}
    input[class^="st-"] { pointer-events: none; }
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
"""
st.markdown(hide_style, unsafe_markdown=True)


# 2. メインの挨拶（移動中に練り上げた素晴らしい文章です！）
st.title("🌿 Luce and v（ルーチェ アンド ブイ）")

st.markdown("""
経営に悩む社長さんのお話や、日々の実務を支える社員の皆さんのお話を聞いてきました。
そこで強く実感したのは、**「IT化がもたらす素晴らしい効率化」**と、同時に**「Face to Face（対面）で交わす温かいコミュニケーションの大切さ」**です。

いくら大掛かりなシステムを導入したところで、導入した意図の共有や社員さんの意識次第で使い方が違ったり、なかなか上手くいかないことがあります。

**「現場の温かみを残したまま、身の回りの『めんどくさい』をスマートに解決することはできないか？」**

私は常に、ITと人の温かみのギャップを埋めることはできないかを考えています。テクノロジーをただの冷たい自動化で終わらせず、皆さんのビジネスに本当の「ゆとり」と「安心」を生み出すためのバックオフィス・パートナーです。
""")

st.divider()


# 3. 提供サービス
st.header("🛠️ 提供サービス")
st.markdown("""
**PythonやGoogle GAS（Google Apps Script）を使った、身近な小さな自動化をお手伝いします。**

大掛かりなシステムに頼るのではなく、日々の業務のなかにあるちょっとした「めんどくさい」をスマートに解決し、現場と事務のギャップを埋めるサポートをいたします。

* **現場の記録用システム構築**
  （現場でパッと入力できて、写真やデータがバラバラにならない仕組みを作ります）
* **バックオフィス業務の自動化ツール開発**
  （毎日の繰り返しのデータ入力や、書類作成の時間をガラリと減らします）
* **日々の帳簿・経費データの整理、正確な報告書作成・実務代行**
""")

st.divider()


# 4. 事業者概要
st.header("📋 事業者概要")
st.markdown("""
* **屋号（事業者名）：** Luce and v（ルーチェ アンド ブイ）
* **代表者：** 代表 Midori
* **事業形態：** 個人事業主
* **活動拠点：** 千葉県
* **事業内容：** バックオフィス業務の自動化・効率化システム構築、実務代行
""")

st.divider()


# 5. お問い合わせ
st.header("📩 お問い合わせ")
st.write("ご相談や、「こういう身の回りの業務、自動化できる？」という小さなお悩みなど、気軽にお声がけください。")

# ★重要：下の "your-email@example.com" を、代表の本番用メールアドレスに書き換えてください！
st.link_button("メールで相談してみる", "luce.and.v.office@gmail.com")
