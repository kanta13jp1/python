import os
import json
import re
import sys
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

API_KEY = "AIzaSyCDxizTbIEY1O_fLVx4mj5hCGx1i7RkM7k"
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)
PREV_FILE = "subs_prev.json"

# ★ チャンネルリスト（省略可能） ★
channels = [
    {"name": "たまきチャンネル", "id": "UCLJNZ7osIjNix4bbkM-rj5w", "url": "https://www.youtube.com/@tamaki-channel"},
    {"name": "国民民主党", "id": "UCJc_jL0yOBGychLgiTCGtPw", "url": "https://www.youtube.com/@DPFPofficial"},
    {"name": "あだチャン 足立康史チャンネル", "id": "UC_Xy01OxP3iYzT2PrLVIfrg", "url": "https://www.youtube.com/@adc83"},
    {"name": "しんばかづやチャンネル", "id": "UC88peYfCbtZD_J1DnkV57Rw", "url": "https://www.youtube.com/channel/UC88peYfCbtZD_J1DnkV57Rw"},
    {"name": "伊藤たかえちゃんねる", "id": "UCMG5j9U1wI2m_fH3ThLhVZw", "url": "https://www.youtube.com/channel/UCMG5j9U1wI2m_fH3ThLhVZw"},
    {"name": "深作ヘスス", "id": "UCzYiBNKmAWioIDUxLeTUO-Q", "url": "https://www.youtube.com/channel/UCzYiBNKmAWioIDUxLeTUO-Q"},
    {"name": "国民民主党 就職氷河期チャンネル", "id": "UC58xKa3nBQZJld_eQ-1E1qA", "url": "https://www.youtube.com/@DPFP_sub"},
    {"name": "森ようすけチャンネル", "id": "UCtddZo9oH5aBAW_Ax26WBew", "url": "https://www.youtube.com/@mori-yosuke"},
    # {"name": "山尾志桜里チャンネル", "id": "UChhZSOjONLdFSlGAx1dKTBw", "url": "https://www.youtube.com/@YamaoShiori"},
    {"name": "はまぐち誠チャンネル", "id": "UCn5YaIkKPivHCvnITBzOYcg", "url": "https://www.youtube.com/channel/UCn5YaIkKPivHCvnITBzOYcg"},
    {"name": "浅野さとし公式チャンネル", "id": "UCPyFaCFzmr4UXlJmg4RJBnQ", "url": "https://www.youtube.com/@asano__satoshi"},
    # {"name": "参議院議員 梅村みずほの【梅チャン♪】", "id": "UCgT4cadhDNmvOPMyICglacA", "url": "https://www.youtube.com/@%E5%8F%82%E8%AD%B0%E9%99%A2%E8%AD%B0%E5%93%A1%E6%A2%85%E6%9D%91%E3%81%BF%E3%81%9A%E3%81%BB%E3%81%AE%E6%A2%85"},
    {"name": "田村まみちゃんねる", "id": "UCdeZ9kSZBi38z_BgWCFbx3w", "url": "https://www.youtube.com/@%E7%94%B0%E6%9D%91%E3%81%BE%E3%81%BF%E3%81%A1%E3%82%83%E3%82%93%E3%81%AD%E3%82%8B"},
    # {"name": "やたわかチャンネル", "id": "UCmPZG_kOdGb7XAI7J0JBeMQ", "url": "https://www.youtube.com/@yatawakako"},
    {"name": "かわいたかのり事務所", "id": "UC2iT6lhfuIEK23R1LFuLbkw", "url": "https://www.youtube.com/@%E3%81%8B%E3%82%8F%E3%81%84%E3%81%9F%E3%81%8B%E3%81%AE%E3%82%8A%E4%BA%8B%E5%8B%99%E6%89%80"},
    {"name": "教えて! やすえちゃん", "id": "UCgX_iJmfXY8H8q803NTqWKA", "url": "https://www.youtube.com/@yasuechan"},
    {"name": "いそざき哲史 ちゃんねる", "id": "UC29Vz-CJneDCQZHlcxAit-A", "url": "https://www.youtube.com/@IsozakiTetsuji"},
    {"name": "ゴシゴシかごしまちゃんねる", "id": "UCkWxcxYvigRoGoqg10kRRJA", "url": "https://www.youtube.com/@kagoshimammoth"},
    # {"name": "竹詰ひとしの『たけちゃんねる』", "id": "UCuXrocorVtSXcodJ8P0aHrQ", "url": "https://www.youtube.com/@%E7%AB%B9%E8%A9%B0%E3%81%B2%E3%81%A8%E3%81%97%E3%81%AE%E3%81%9F%E3%81%91%E3%81%A1%E3%82%83%E3%82%93%E3%81%AD%E3%82%8B"},
    {"name": "おだけチャンネル", "id": "UCd_hNdnFB7R2Y43r-VLpr0g", "url": "https://www.youtube.com/@odake_kokumin"},
    {"name": "ひのさりチャンネル", "id": "UC2z2VDOBZAgWogPsthObavw", "url": "https://www.youtube.com/channel/UC2z2VDOBZAgWogPsthObavw"},
    {"name": "浜野よしふみチャンネル", "id": "UCJCXqehY85HuNJGYXqw4IdA", "url": "https://www.youtube.com/@%E6%B5%9C%E9%87%8E%E3%82%88%E3%81%97%E3%81%B5%E3%81%BF%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB"},
    {"name": "岡野純子の『おかじゅんチャンネル』", "id": "UC2muVzDIr-2XSq6AAHu4e5w", "url": "https://www.youtube.com/@DPFPokano"},
    {"name": "あおすぎチャンネル【杉本あおい-国民民主党】", "id": "UCLC3ZkreGcLEweUfLkiYD2A", "url": "https://www.youtube.com/@aoisgmt639"},
    {"name": "政治が分かるぱにゃちゃん", "id": "UCQ9bHJe19GCbDwMKBCn0oyA", "url": "https://www.youtube.com/@panyachan87"},
    {"name": "玄ちゃんねる", "id": "UCUOn0qeJ3YABTRRqe_52MiA", "url": "https://www.youtube.com/@fukuda_gen1027"},
    {"name": "うすきチャンネル", "id": "UCp5ZGRS2WZujP3Oi2C3Kquw", "url": "https://www.youtube.com/@%E3%81%86%E3%81%99%E3%81%8D%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB"},
    {"name": "うさぎとしんじ", "id": "UC4yP_T0KyIc7OR7nWgPHtAw", "url": "https://www.youtube.com/@%E3%81%86%E3%81%95%E3%81%8E%E3%81%A8%E3%81%97%E3%82%93%E3%81%98"},
    {"name": "救急医政治家・福田とおる", "id": "UCn99ji8uiM1rMZTVrb2IaJw", "url": "https://www.youtube.com/@%E7%A6%8F%E7%94%B0%E3%81%A8%E3%81%8A%E3%82%8B"},
    {"name": "小林さやかチャンネル", "id": "UCz4EuwJ6UQvjHuGR5wpJL-w", "url": "https://www.youtube.com/@%E5%B0%8F%E6%9E%97%E3%81%95%E3%82%84%E3%81%8B%E5%BE%8C%E6%8F%B4%E4%BC%9A"},
    {"name": "【公式】江原くみ子チャンネル", "id": "UCJkN5exl5XrfRhBkx4A7XMg", "url": "https://www.youtube.com/@eharakumiko"},
    {"name": "国民民主党　富山県　庭田ゆきえ", "id": "UCAxj_RFxlsX4EnaXuKDnRFw", "url": "https://www.youtube.com/@%E5%BA%AD%E7%94%B0%E5%B9%B8%E6%81%B5"},
    {"name": "奥村よしひろ", "id": "UCENJ_oZXbaU0ovsl7uTd7Sw", "url": "https://www.youtube.com/@YOSHIHIRO_OKUMURA29"},
    {"name": "きくち大二郎チャンネル", "id": "UCUSicJmBl8KnSB2ezFQm1dQ", "url": "https://www.youtube.com/@kikuchi_daijiro"},
    # {"name": "堀江あきら'が'学び直し塾", "id": "UC3UH6ZzhdozTkRffmVDn9Qg", "url": "https://www.youtube.com/@akirahorie1987"},
    {"name": "かわもと健一チャンネル", "id": "UCoLNTUZ83NXAZ0b-FQXqzaw", "url": "https://www.youtube.com/@kawamoto1979"},
    # {"name": "きどかおり", "id": "UCnUltJHRdMm4_peIdRbRI_Q", "url": "https://www.youtube.com/channel/UCnUltJHRdMm4_peIdRbRI_Q"},
    {"name": "平戸航太チャンネル", "id": "UCzXn5-cH5e9CANNjFh6mojA", "url": "https://www.youtube.com/@KoutaHirado"},
    {"name": "熊本ちひろ　横浜市会議員(南区)", "id": "UCnJs-Oz53p98wId7sdS1Ikg", "url": "https://www.youtube.com/@kumamoto_chi"},
    {"name": "愛媛1区・いしいともえ YouTubeチャンネル", "id": "UC6UMAxgnOSbAsrH2KK2hmjw", "url": "https://www.youtube.com/@%E6%94%BF%E6%B2%BB%E5%AE%B6%E3%81%84%E3%81%97%E3%81%84%E3%81%A8%E3%82%82%E3%81%88%E5%A5%B3%E6%80%A7%E3%81%AE%E7%94%9F%E3%81%8D"},
    {"name": "山田吉彦(ヨシヒコ)公式チャンネル", "id": "UCtcleTqYfCEzp6rR002Qo4A", "url": "https://www.youtube.com/channel/UCtcleTqYfCEzp6rR002Qo4A"},
    {"name": "山中しゅんすけチャンネル", "id": "UC_Reig3SKVc8gFxQT_dYlbA", "url": "https://www.youtube.com/@ER_Internal_Ortho"},
    # {"name": "おくもとゆりちゃんねる", "id": "UCLHKuD0_A71lwVqU68coCNw", "url": "https://www.youtube.com/@OkumotoYuri"},
    {"name": "牛田まゆチャンネル", "id": "UCUZtNoALtR3OYqS0n3Iakxw", "url": "https://www.youtube.com/@ushida-channel"},
    {"name": "薬師寺みちよチャンネル【公式】", "id": "UCckIbzB-LzHQtytJE__pg4A", "url": "https://www.youtube.com/@michiyo_yakushiji"},
    # {"name": "水野こういちチャンネル", "id": "UCCSHRid3dsr41kPX_Uf_9vg", "url": "https://www.youtube.com/channel/UCCSHRid3dsr41kPX_Uf_9vg"},
    {"name": "鈴木まさきチャンネル@国民民主党", "id": "UC6DZano0LZUaPEOtN1tNu7g", "url": "https://www.youtube.com/channel/UC6DZano0LZUaPEOtN1tNu7g"},
    # {"name": "後藤ひとし事務所", "id": "UC3oa3fhphcDPF1zgbyQ90UQ", "url": "https://www.youtube.com/@go510"},
    # {"name": "せっきー教育ちゃんねる", "id": "UCNELIPmEUBr4LL6-RUQyjzg", "url": "https://www.youtube.com/channel/UCNELIPmEUBr4LL6-RUQyjzg"},
    # {"name": "伊藤たつおチャンネル", "id": "UCs7HgyO7o4-nX0BinHycNig", "url": "https://www.youtube.com/@tatsuo_i_39thankyou"},
    # {"name": "京都府議会議員　酒井つねおチャンネル", "id": "UC5UuiF-EdKu0ZC6UwcvGb4w", "url": "https://www.youtube.com/channel/UC5UuiF-EdKu0ZC6UwcvGb4w"},
    {"name": "川崎の翔平チャンネル【国民民主党 山口翔平】", "id": "UCaK1fEZln3n_isrWZxFQrEg", "url": "https://www.youtube.com/@kawasaki-shohei"},
    {"name": "木村さちこのさっチャンネル", "id": "UCIIpLTDxSDGnftUdPJtx1Dg", "url": "https://www.youtube.com/@kimurasachikolaw"},
    {"name": "梶原みずほ　国民民主党公認候補　衆議院 東京10区 豊島区 文京区", "id": "UC06A1kNyns6DN52qCOYEMRg", "url": "https://www.youtube.com/@mizuhokajiwara"},
    {"name": "くわずるゆき子(渋谷区議会議員⭐️国民民主党)", "id": "UCzEQqcCjvZjcmWuE09EI-DQ", "url": "https://www.youtube.com/@kwzr"},
    {"name": "さゆみチャンネル", "id": "UCeEJUVPrZ70sgkFq6rrO4gA", "url": "https://www.youtube.com/@sayumi-okayama"},
    {"name": "野村たいき #国民民主党 #新潟4区", "id": "UCVMSdrXnRxSy9_yyuQZOvdA", "url": "https://www.youtube.com/@yasu10ki"},
    {"name": "すわれいこ", "id": "UClnkZdyqQTHp5pD0BCVb6Ig", "url": "https://www.youtube.com/@suwa-reiko"},
    {"name": "入江のぶこチャンネル 国民民主党・東京7区 衆議院議員候補者", "id": "UCE4wl6JIFtBjESzCBa4SoZA", "url": "https://www.youtube.com/channel/UCE4wl6JIFtBjESzCBa4SoZA"},
    {"name": "中村太一チャンネル 国民民主党 衆議院神奈川17区", "id": "UC5HQt2fgOoYrwrADbMjRg3A", "url": "https://www.youtube.com/channel/UC5HQt2fgOoYrwrADbMjRg3A"},
    {"name": "鳩山紀一郎", "id": "UCGHNFMTYrhOj3CFu0MDc3UQ", "url": "https://www.youtube.com/channel/UCGHNFMTYrhOj3CFu0MDc3UQ"},
]

# ID が UC… でなければ URL から抜き出す
for ch in channels:
    if not re.match(r"^UC[A-Za-z0-9_-]{22}$", ch["id"]):
        m = re.search(r"/channel/([A-Za-z0-9_-]+)", ch["url"])
        if m:
            ch["id"] = m.group(1)


def fetch_channel_stats(ids):
    """channels.list(part=statistics,contentDetails) で subs/videos/uploads を取得"""
    stats = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        resp = YOUTUBE.channels().list(
            part="statistics,contentDetails", id=",".join(chunk)
        ).execute()
        for it in resp.get("items", []):
            cid = it["id"]
            stats[cid] = {
                "subs": int(it["statistics"].get("subscriberCount", 0)),
                "videos": int(it["statistics"].get("videoCount", 0)),
                "uploads": it["contentDetails"]["relatedPlaylists"]["uploads"]
            }
    return stats


def fetch_latest_videos_from_uploads(stats):
    """playlistItems.list + videos.list で最新動画情報をまとめて取得"""
    latest = {}
    all_vids = []
    # 1) playlistItems で最新動画ID と公開日時＋タイトルを取る
    for cid, info in stats.items():
        try:
            resp = YOUTUBE.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=info["uploads"],
                maxResults=1
            ).execute()
            items = resp.get("items", [])
            if items:
                it = items[0]
                vid = it["contentDetails"]["videoId"]
                pub = it["contentDetails"]["videoPublishedAt"]
                dt = (datetime.fromisoformat(pub.replace("Z", "+00:00"))
                           .astimezone(timezone(timedelta(hours=9))))
                latest[cid] = {
                    "title": it["snippet"]["title"],
                    "url": f"https://youtu.be/{vid}",
                    "published": dt.strftime("%Y/%m/%d %H:%M"),
                    "views": 0,
                    "videoId": vid
                }
                all_vids.append(vid)
            else:
                latest[cid] = {"title":"", "url":"", "published":"", "views":0, "videoId": None}
        except HttpError:
            latest[cid] = {"title":"", "url":"", "published":"", "views":0, "videoId": None}

    # 2) videos.list で再生数を一括取得
    for i in range(0, len(all_vids), 50):
        chunk = all_vids[i:i + 50]
        resp = YOUTUBE.videos().list(
            part="statistics", id=",".join(chunk)
        ).execute()
        for it in resp.get("items", []):
            vid = it["id"]
            views = int(it["statistics"].get("viewCount", 0))
            # videoId から channelId を逆引きして埋め込み
            for cid, info in latest.items():
                if info.get("videoId") == vid:
                    info["views"] = views
                    break

    return latest


def fetch_recent_post_count(cid, days=30):
    """過去 days 日の投稿本数を取得"""
    now = datetime.now(timezone(timedelta(hours=9)))
    after = (now - timedelta(days=days)).isoformat()
    try:
        resp = YOUTUBE.search().list(
            part="id", channelId=cid, publishedAfter=after,
            type="video", maxResults=50
        ).execute()
        return len(resp.get("items", []))
    except HttpError:
        return 0


def human_readable(n):
    return f"{n:,}人"


def load_previous_stats():
    """前回 stats を読み込み、旧フォーマットをマイグレート"""
    if not os.path.exists(PREV_FILE):
        return {}
    raw = json.load(open(PREV_FILE, encoding="utf-8"))
    migrated = {}
    for cid, v in raw.items():
        if isinstance(v, int):
            migrated[cid] = {"subs": v, "videos": 0}
        else:
            migrated[cid] = {"subs": v.get("subs", 0), "videos": v.get("videos", 0)}
    return migrated


def save_current_stats(stats):
    # subs, videos のみ保存
    slim = {cid: {"subs": s["subs"], "videos": s["videos"]} for cid, s in stats.items()}
    json.dump(slim, open(PREV_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    
def compute_next_quota_reset_jst() -> datetime:
    # 太平洋夏時間（PDT）
    pac = ZoneInfo("America/Los_Angeles")
    # 日本時間（JST）
    jst = ZoneInfo("Asia/Tokyo")

    now_pac = datetime.now(pac)
    # 今日の太平洋 0:00（＝深夜）を取得
    today_mid_pac = now_pac.replace(hour=0, minute=0, second=0, microsecond=0)

    # もしもう今日の 0:00 を過ぎていたら「翌日の 0:00」、まだなら「今日の 0:00」
    if now_pac >= today_mid_pac:
        reset_pac = today_mid_pac + timedelta(days=1)
    else:
        reset_pac = today_mid_pac

    # 日本時間に変換
    return reset_pac.astimezone(jst)


def print_growth_tips():
    tips = """
以下の施策を実践すると、チャンネル登録者数を増やしやすくなります。政治系チャンネルならではのポイントを交えつつご紹介します。

1. **定期的・計画的な投稿スケジュール**
   * 毎週〇曜日の〇時といった"いつ公開されるか分かる"規則性を持たせる  
   * 長期的に続けることで視聴者の定着率がアップ

2. **クリックを誘うサムネイル＆タイトル設計**
   * 顔のアップ＋感情のこもった表情を大きく配置  
   * "◯◯とは何か？"「知られざる□□」など問いかけ型にすると興味を引きやすい  
   * タイトルは30文字以内に要点を盛り込み、キーワードを前半に

3. **動画冒頭の "5秒ルール" を徹底**
   * 最初の5秒で「この動画で何が得られるのか」「どんな話題か」を明確に伝え、離脱を防止

4. **視聴維持率（Audience retention）の向上**
   * 章立て（チャプター）を活用して見やすくする  
   * 途中で"サプライズ情報"や"質問投げかけ"を挟み、最後まで見てもらえる工夫を

5. **エンゲージメントを促す仕掛け**
   * 本編中・最後に必ず「👍高評価／🔔通知オン」「コメント・質問」を呼びかける  
   * コメントに運営側から積極的に返信し、コミュニティ感を醸成

6. **SNS・メールマガジンでの横展開**
   * Twitter／Facebook／LINE公式アカウント等で新着公開を告知  
   * 静止画＋短い切り抜き動画をSNSに投下し、本編への導線を用意

7. **コラボ・ゲスト出演**
   * 同じく政治系YouTuberやインフルエンサー、地方議員などとコラボして相互露出を図る  
   * 異業種ゲスト（文化人・専門家・大学教授など）を呼ぶのも◎

8. **再生リスト（プレイリスト）で動画を束ねる**
   * "政策解説シリーズ"「議員インタビューシリーズ」などテーマ別にまとめると視聴が連続しやすい  
   * 視聴終了後の次動画自動再生が効果的に働く

9. **YouTube Analytics を活用した改善**
   * 視聴維持率やクリック率が低い動画はサムネ・タイトル・冒頭を見直す  
   * トラフィックソースを分析し、外部導線（SNS／検索など）強化を検討

10. **ユーザー参加型コンテンツ**
    * 視聴者からの質問を募集して答える「Q&A」「ライブ配信」を定期的に開催  
    * ポーリング機能（コミュニティタブ）で次回企画を決めてもらうなど双方向性を重視

---
これらを地道に積み重ねることで、チャンネルの「認知→興味→登録→視聴」の一連の流れがスムーズになり、登録者数の増加につながります。ぜひお試しください！
"""

    print(tips)


def main():
    prev_stats = load_previous_stats()
    ids = [c["id"] for c in channels]

    try:
        # 通常取得
        stats = fetch_channel_stats(ids)
        latest = fetch_latest_videos_from_uploads(stats)
        recent_counts = {cid: fetch_recent_post_count(cid) for cid in ids}
    except HttpError as e:
        # クォータ超過時のフォールバック
        if e.resp.status == 403 and "quotaExceeded" in e.content.decode():
            print("Warning: YouTube Data API のクォータを超過しました。前回の結果を表示します。\n")
            # 次回リセット時刻を表示
            next_reset = compute_next_quota_reset_jst()
            print(f"次回クォータリセット（日本時間）: {next_reset.strftime('%Y/%m/%d %H:%M:%S')} JST\n")
            # キャッシュのみで出力。recent_counts も 0 で埋めておく
            stats = {
                cid: {
                    "subs": prev_stats.get(cid, {}).get("subs", 0),
                    "videos": prev_stats.get(cid, {}).get("videos", 0),
                    "uploads": None
                }
                for cid in ids
            }
            latest = {
                cid: {"title":"", "url":"", "published":"", "views":0}
                for cid in ids
            }
            recent_counts = {cid: 0 for cid in ids}
        else:
            raise

    # 出力部（例、省略せず全文をここに…）
    now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y/%m/%d %H:%M:%S")
    print(f"国民民主党 Youtubeチャンネル {now} 現在\n")

    for ch in sorted(channels, key=lambda ch: stats[ch["id"]]["subs"], reverse=True):
        cid = ch["id"]
        sub = stats[cid]["subs"]
        vidc = stats[cid]["videos"]
        prev_sub = prev_stats.get(cid, {}).get("subs", 0)
        prev_vid = prev_stats.get(cid, {}).get("videos", 0)
        diff_sub = sub - prev_sub
        diff_vid = vidc - prev_vid
        ds = f" ({'+' if diff_sub>=0 else '-'}{abs(diff_sub):,}人)" if cid in prev_stats else ""
        dv = f" ({'+' if diff_vid>=0 else '-'}{abs(diff_vid):,}本)" if cid in prev_stats else ""

        print(f"{ch['name']}  登録者数 {human_readable(sub)}{ds}  動画本数 {vidc}本{dv}")

        # 直近30日
        rc = recent_counts.get(cid, 0)
        if rc:
            avg = 30 / rc
            print(f"  直近30日で{rc}本投稿（平均{avg:.1f}日／本）")

        # 最新動画
        lv = latest[cid]
        if lv.get("title"):
            views_str = f"{lv['views']:,}回"
            print(f"  最新：『{lv['title']}』／{lv['published']}／再生数：{views_str}")
            print(f"    {lv['url']}")
        else:
            print(f"  {ch['url']}")

        print()  # 空行

    save_current_stats(stats)
    print_growth_tips()


if __name__ == "__main__":
    main()
