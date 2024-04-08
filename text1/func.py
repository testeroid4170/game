import random

import os

#喘ぎ声、セリフのリスト

sl1 = ['あんっ！','あんっ…','あぁんっ！','あぁんっ…','ああぁんっ！','ああぁん…','ひゃあんっ！','ひゃあん…','ひゃあぁんっ！','ひゃあぁん...'\
       ,'んっ...んっ...','んっ...んっ...んっ...','んああぁんっ！','んああぁん...','うっ...うっ...うっ...','ああああぁんっ！','ああああぁん...']

sl2 = ['…入って…きたぁ……あぁんっ！…','…すごい…ちんぽ…きたぁ…','…きた…ちんぽ……あんっ！…おまんこに入ってきたぁ…',\
       '…おちんぽっ！…あぁんっ！…このおちんぽ…凄すぎ…','…入って…きたぁ………あんっ！','…あんっ！あんっ！…入って…きた...'\
       ,'…はいっちゃった…おまんこに大きなポコちん…入ってきたぁ…','…この…ちんぽ…オタくんの…エロちんぽ入ってきた…'\
       ,'…入って…きたぁ………あんっ！','ひゃあんっ！…あんっ！…あの！…あんっ！…きたぁ…おちんぽ…きたぁ…']

al2 = ['あんっ！','あんっ…','あぁんっ！','あぁんっ…','ああぁんっ！','ああぁん…','ひゃあんっ！','ひゃあん…','ひゃあぁんっ！',\
       'ひゃあぁん...','んっ...んっ...','んっ...んっ...んっ...','んああぁんっ！','んああぁん...','うっ...うっ...うっ...','ああああぁんっ！',\
       'ああああぁん!','あんっ♡','ひゃあんっ♡','いやぁんっ♡','ひゃんっ♡','んっ♡んっ♡','らめぇ♡','あぁん♡','もっとぉ♡','感じるぅ♡','あっ♡','ああぁんっ♡']

al3 = ['ひゃああぁんっ！…','あああぁんっ！…','あぁんっ！','あんっ！あんっ！','んああぁんっ！…','んっ…んっ…','ひゃあぁんっ！',\
       'んあっ！…','あっ…あっ…あっ…','んおおおんっ！','ひゃんっ！','いやぁんっ！…','いやああぁんっ！','んっ…あぁんっ！','うっ…うっ…うっ…']

dl1 = ['…奥まで入ってる……','…ヤバい…ちんぽ…すごい…','このおちんぽ…やばすぎ…気持ちいい…','…奥の方グリグリされるの好き…',\
       'ちんぽ…もっと欲しいの…','そこ……そこが気持ちいいの！','このおちんぽ…あんっ！…どんどん良くなってく…','…もっと欲しいの！'\
       ,'ちんぽ…あんっ！…大好き…','このちんぽ…あんっ！大きくて気持ちいい……','…この体位…あんっ！…大好き…','奥まで…あんっ！…ちんぽ届いてるよ',\
       'そこ…すごくいい…','突いて…あんっ！…もっと突いてー！…','…クリトリスも…あんっ！…触って…',\
       'そんなにされたらっ…あぁんっ！…おかしくなっちゃう','セックス…気持ちよすぎ…あぁんっ！…もっとしてぇ！']

dl2 = ['…もっと無理矢理犯してー！','もっと…激しくしてぇ…','そこ…気持ちよすぎ…','おまんこおかしくなっちゃうくらいはげしく犯してぇー！',\
       '気持ちいい…あんっ…これ…最高…','もっとして！…それ好きなのぉ！','あぁんっ！…激しいの…好き…',\
       'もぉう...セックスの…途中なのにおっぱいばっかり見てぇ…','感じるっ…そこ感じるっ！','そんなにされたらっ…あんっ！…おまんこおかしくなっちゃう！'\
       ,'おまんこ…もっとついてー！','ちんぽで…奥の方…あんっ…掻き回されるの好き…','激しいっ…あんっ！…気持ちよすぎて…おかしくなっちゃう！',\
       'んっ…感じすぎて…おまんこおかしくなっちゃう！','そこ好き！…もっとついてぇ！','ガンガン突かれるの好き…',\
       'おまんこだけじゃなくて…あんっ！…体全体が気持ちよくなっちゃう！','もっとしてぇ！理性なくなるまで犯しまくってぇ！',\
       '…そんなに…されたら…あん']

zl1 = ['…ヤバい……イッちゃう…あんっ！あんっ！','イッちゃう…あぁんっ!','あんっ！…もうイッちゃう…','イクっ！私イッちゃう！'\
       ,'イき…そう…ひゃああぁんっ！','イクッ！イクッ！イっちゃう！','もうだめ……イっちゃいそう…','いっ…イッちゃう…らめぇ…']

zl2 = ['…イクっ！イクっ！イクっ！…ああああぁんっ！','…イクっ！イクっ！イクっ！…ひゃああぁんっ！','…イクっ！イクっ！…ああぁんっ！'\
       ,'…イクっ！イクっ！…ひゃあぁんっ！','…イクっ！イクっ！イクっ！あんっ！あんっ！…いくぅっ！…ああああああぁんっ！',\
       '…イクっ！イクっ！…いくぅっ！…ひゃああぁんっ！','…イクっ！イクっ！…いくぅっ！…あぁんっ！','…イクっ！イクっ！イクっーー！ああああぁんっ！'\
       ,'…イクっ！イクっ！イクっ！ああああぁんっ！','…イクっ！イクっ！イくぅっ！…あああぁんっ！','…イクっ！イクっ！イくぅっ！…ひゃあぁんっ！',\
       '…イクっ！イクっ！精液…あんっ！…中に出して…','イっちゃう！イっちゃう！精液中に出してぇー！ああぁんっー',\
       'イっちゃう！種付けしてぇー！ああぁんっ！','イっちゃう！イっちゃう！種付けしてぇー！ひゃああぁんっ！','…イクっ！イクっ！種付けしてぇー！ひゃああぁんっ！']

ol1 = ['はぁ…はぁ…はぁ…','んっ…はぁ…はぁ…','はぁ…はぁ…はぁ…','はぁ…はぁ…','うっ…うっ…うっ…','おっ…おっ…','んんんっ…ん…']

ol2 = ['すごい精液の量…いっぱい中出しされちゃった…','まだ快感が残ってる…はぁ…気持ちよすぎて…体動かない…','ヤバい…気持ちよすぎて動けない…'\
       ,'すごい勢いで種付けされちゃった…','おまんこから精液溢れ出てる…','イきすぎて…体痺れちゃった…はぁ…はぁ…セックス…気持ちよすぎる…',\
       'おまんこの中…精液でいっぱい…','すごい…アツアツの精液たっぷり中出しされちゃった…','まだイった快感が残ってる…はぁ…すごい気持ちよかったなぁ…'\
       ,'ヤバい…体動かせないくらい気持ちいいよ…','いっぱいマーキングされちゃった…','おまんこから白濁液溢れ出てる…',\
       '気持ちよすぎて…動けなくなっちゃった…はぁ…はぁ…セックス…凄すぎる…','おまんこの中…白濁液でいっぱい…',\
       '…アツアツの精液いっぱい注ぎこまれちゃった…']

hrm1a = ['…勇者様はおっぱいが大好きなんですね♡','…おっぱいばっかり…そんな…','…気持ちいい…それ…すごくいいです…',\
         '…そんなに強く…揉まれたら… ','…それ…ものすごく…感じちゃう…','…勇者様…もっとして欲しいです…',\
         '…勇者様ぁ…もっと強く揉んでください…','…勇者さま…もっと揉んでくださぁい♡','…興奮してきた…はぁはぁ…',\
         '…おっぱい揉まれてるだけで、イッちゃいそう…','乳首...すごくかんじちゃうのぉ♡','もっと乳首つねってほしいです♡']

op1a = ['あんっ！','ひゃんっ！','いやぁんっ！','んっ...','あんっ♡','ひゃあぁんっ♡','いやあぁんっ♡','ああぁんっ♡','あっ...']


ral1 = ['ああぁんっ！','んんっ…','あっ…あぁんっ！','あんっ！','んっ…','ひゃあぁんっ！','うっ…うっ…うっ…','んああぁんっ！',\
        'ぐっ…ぐっ…','ひゃんっ！','いやぁんっ！','んんっ…','ああぁんっ…','あぁんっ…','あんっ…','ひゃあんっ…','ひゃんっ…','いやっ…']

ral2 = ['んっ…んっ…','んっ…','ひゃあああぁんっ！','ああぁんっ！','あぁんっ！','あんっ！','うおおっ！','ひゃあっ！','あんっ！','あんっ！あんっ！'\
     ,'うああぁんっ！','んああぁんっ！','ひゃんっ！','ひゃあああぁんっ…','ああぁんっ…','あぁんっ…','あんっ…','うおおっ…','ひゃあっ…','あんっ…',\
       'あんっ！あんっ…','うああぁんっ…','んああぁんっ…','ひゃんっ…']

ral3 = ['ぐぅおっ！','うおぉあっ！','うぐおぉっ！','ぐっ！','ぐおぉあっ！','おっ！おぉっ！','んんっ！','ああぁっ！','ぐうぅっ！']

rsl1 = ["…やめろっ！","…それ以上は！","…くっ…くそ…","…はぁ…はぁ…はぁ…","…うおおっ！？","…きっ…貴様…","…はっ…早くその肉棒を抜け…",\
        "…ぐっ…ぐうぅっ…","…こ…こんなもの…で…","…ぐあぁっ…","…ぐうっ…","…うぐっ…","…ゆ…許さんぞ…"]

rsl2 = ['…ぐはっ…ぐおおぉ！…','…くっ…この私が…','…ぐあぁっ！…','…ぐうっ！…','…うぐあっ！…','…うああああぁ！','…うごごごご！','…はああああぁっ！？',\
        'んおっ！んおっ！','そっ…そこは…ダメだ！','それ…以上は…','やっ…やめてくれ…','それは…効きすぎる…','…はぁ…はぁ…']

rol1 = ['やっ…やめてくれっ！','そんなもの中に出されたら…','たのむ…やめてくれ！','…ぐっ…中だけは…','…それだけはっ！']

rol2 = ["ぐおおおおお！…はぁ…はぁ…はぁ…","んあんっ！んあああああああんっ！","あひゃあああああぁ！あひゃああぁんっ！",\
        "おっ…おおおおおおぉんっ！…はぁ…はぁ…はぁ…","んおっ！…んおおおお…ああああぁんっ！…はぁ…はぁ…はぁ…"]

rb1 = ['中に出すぞ！','よし！このまま中に出すぞ！','中出しするぞ！','このまま中出しするぞ！','出るっ！中に出すぞ！']

rb2 = ['うおおぉ！出るっ！','うっ！うおおおおぉ！出すぞ！','出るっ！出るっ！イクぞ！','うおおぉっ！出すぞ！うおおぉ！']

psl1 = ['勇者様のおちんぽ包ませて頂きますね。','では勇者様のおちんぽをおっぱいでズリズリさせて頂きますね。','勇者様♡このおっぱい使って気持ちよくなっていいんですよ？',\
        'この爆乳を使って気持ちよくなりましょうね♡','たくさん気持ちいいことしましょうね♡','このデカ乳で勇者様のおちんちん包ませて頂きますね。',\
        '勇者様のおちんぽ…はやく私の爆乳で挟ませてください♡',\
        '勇者様のおちんちん…早く私のデカ乳で挟ませてください♡','では勇者様のちんちんを私の爆乳でパフパフさせて頂きますね♡',\
        '勇者様♡このデカ乳使って気持ちよくなりましょうね♡','このデカ乳を使っていっぱい良いことしましょうね♡',\
        'この淫乱デカ乳で勇者様のおちんぽ包ませて頂きますね♡']

pdl1 = ['どうですか～私のおっぱいは？','勇者様気持ちいいですかぁ？','もぉう…勇者様はおっぱいが大好きなんですね…','勇者様のためにいっぱいサービスしちゃいますね…',\
        '勇者様ったら、すごく幸せそうですね…','いっぱい気持ちよくなってくださいね…','そんなにおっぱいが好きなんですかぁ？','いっぱいおっぱいに埋もれてくださいね…',\
       'おっぱいとちんちんがこすれて気持ちいいですね！','勇者様のおちんぽ…すごく熱いです…','勇者様のおちんぽ…大きくてこすりがいがあります…',\
       'いっぱい疲れを癒していってくださいね♡','勇者様はパイズリが大好きなんですね！素敵です！','勇者様に気持ちよくなって頂けるよう、精一杯頑張りますね！'\
       ,'おちんぽがおっぱいに囲まれて気持ちいいですか？','勇者様のおちんぽ、幸せそうでよかったです。','すごいおちんぽですね。こすりがいがあって嬉しいです！',\
       'もっともっと気持ちよくなってくださいね']

pl1 = ['…ずりずり…','…ごしごし…','…むにゅむにゅ…','…むにゅう…','…にゅぽにゅぽ…','…にちゃにちゃ…',\
       '…ぐり！ぐり！ぐり！','…ずりずり！ずりずり！','…ごしごし！','…むにゅむにゅ！','…むにゅう！','…にゅぽにゅぽ！',\
       '…にちゃにちゃ！','…ぐり♡ぐり♡','…ずりずり♡','…ごしごし♡ごしごし♡','…むにゅむにゅ♡','…むにゅう♡むにゅう♡',\
       '…にゅぽにゅぽ♡','…にちゃにちゃ♡']

pl2 = ['…ずりずり…ずりずり…','…ごしごし…ごしごし…','…むにゅむにゅ…むにゅむにゅ…','…むにゅう…むにゅう…','…にゅぽにゅぽ…にゅぽにゅぽ…','…にちゃにちゃ…にちゃにちゃ…',\
       '…ぐり！ぐり！ぐり！','…ずりずり！ずりずり！','…ごしごし！ごしごし！','…むにゅむにゅ！むにゅむにゅ！','…むにゅう！むにゅう！','…にゅぽにゅぽ！にゅぽにゅぽ！',\
       '…にちゃにちゃ！にちゃにちゃ！','…ぐり♡ぐり♡ぐり♡','…ずりずり♡ずりずり♡','…ごしごし♡ごしごし♡','…むにゅむにゅ♡むにゅむにゅ♡','…むにゅう♡むにゅう♡',\
       '…にゅぽにゅぽ♡にゅぽにゅぽ♡','…にちゃにちゃ♡にちゃにちゃ♡']

pl2 = ['あんっ！あんっ！','んっ…んっ…','ひゃああぁんっ！','ひゃあぁんっ！','んんっ！','いやぁんっ！','あんっ...あんっ...','んっ！んっ！','ひゃあんっ...',\
       'ひゃあぁんっ...','んんっ...','いやぁんっ...','あんっ♡あんっ♡','んっ♡んっ♡','ひゃあんっ♡','ひゃあぁんっ♡','んんっ♡','いやぁんっ♡']

pdl2 = ['これからこのおっぱいで、もっとパフパフイチャイチャしましょうね♡','私たちのおっぱいで今日は存分に楽しんでいってくださいね♡',\
       'もぉう♡勇者様ったらおっぱいばっかり見て♡','勇者様は本当におっぱいが大好きなんですね♡','私のおっぱいデカ乳で、た～くさん楽しんでくださいね♡',\
       'これからこの爆乳おっぱいで、楽しいことしましょうね♡','勇者様は大きいおっぱいが大好きなんですね♡','今日は私の爆乳で楽しんでいって下さいね♡',\
       'ぶるんぶるんの爆乳おっぱいで、勇者様気持ちよくしますね♡','もぉう♡さっきからおっぱい見過ぎですよ♡','勇者様はおっぱいが本当に大好きなんですね♡']


sya_1a = ['うおおぉっ！出るっ！','出るっ！出るっ！','イクッ！イクッ！']

hrm_s = ['もっと...して欲しいです...','そこ...すごく気持ちいいです...','おまんこぉ...おかしくなっちゃう...\
      気持ちよすぎて...おかしくなっちゃう...','もっと...おまんこいじめてほしいです...','そこぉ...気持ちよすぎです...',\
      'こんなの...頭おかしくなっちゃう...','す...ごい...気持ちいい','おっぱいも...触ってほしいです...','勇者様のおちんぽ...すごぉい...'\
      ,'はぁ...はぁ...もっとしてほしいです...','す...ごく気持ちいいです...','性感帯がこすられて...ああぁんっ♡','気持ちよすぎて...おまんこおかしくなっちゃう♡'\
      ,'そこぉ...すごく感じるのぉ...','Gスポットが刺激されて...ああぁんっ♡',]

pf_1a = ['沢山出ましたね♡勇者様♡','いっぱい出ましたね♡勇者様♡','気持ちよかったですか？勇者様♡'\
         ,'勇者様の精液...すごくエッチですね♡','勇者様のエッチなお汁たくさん出ましたね','すごくいっぱい射精しましたね♡勇者様♡']

ops_1a = ['おっぱい気持ちいい？もっと揉んでもいいよ？','もっと強く揉んでも大丈夫だよ？','もっと乳首つねってぇ♡','おっぱいワシ掴みしてぇ♡',\
          '乳首にデコピンしてぇ♡','おっぱいもっとモミモミしてぇ♡','好きなだけおっぱい揉んでいいんだよ？','おっぱい揉まれるの気持ちいい♡',\
          'おっぱい思いっきりモミモミしてね♡']

#SEのリスト

sv1 = ['sv_1a', 'sv_1b', 'sv_1c']
sv1_z = ['sv_1z']
sv2 = ['sv_2a', 'sv_2b', 'sv_2c']
sv_2z = ['sv_2z']

sub1 = ['sub1_hard1', 'sub1_hard2', 'sub1_hard3', 'sub1_norm1', 'sub1_norm2', 'sub1_norm3',\
        'sub1_soft1', 'sub1_soft2', 'sub1_soft3','sub1_z1', 'sub1_z2', 'sub1_z3']


sub2 = ['sub2_hard1', 'sub2_hard2', 'sub2_hard3', 'sub2_norm1', 'sub2_norm2', 'sub2_norm3', 'sub2_soft1', \
        'sub2_soft2', 'sub2_soft3','sub2_z1', 'sub2_z2', 'sub2_z3']

sexy1 = ['sexy1', 'sexy2', 'sexy3']

aoi = ['aoi_hard1', 'aoi_hard2', 'aoi_hard3', 'aoi_norm1', 'aoi_norm2', 'aoi_norm3', 'aoi_soft1', 'aoi_soft2', \
       'aoi_soft3','aoi_z1', 'aoi_z2', 'aoi_z3']

momo = ['momo_hard1', 'momo_hard2', 'momo_hard3', 'momo_norm1', 'momo_norm2', 'momo_norm3', 'momo_soft1', \
        'momo_soft2', 'momo_soft3','momo_soft2', 'momo_soft3', 'momo_z1', 'momo_z2']

ririka = ['ririka_hard1', 'ririka_hard2', 'ririka_hard3', 'ririka_norm1', 'ririka_norm2', 'ririka_norm3', \
          'ririka_soft1', 'ririka_soft2', 'ririka_soft3','ririka_z1', 'ririka_z2'] 

piston1 = ['piston1']
piston2 = ['piston2']

syasei = ['syasei']

pyzuri = ['py_slow','py_norm','py_fast1', 'py_fast2']


#SEの関数を定義

def se_stop():
    print('<StopSE>')
    print('')

def se_hard(se_list):
    se_stop()
    new_list = [i for i in se_list if 'hard' in i]
    se1 = ''.join(random.sample(new_list,1))
    print(f"<PlaySE: {se1}, 90, 100, 0>")
    print('')

def se_norm(se_list):
    se_stop()
    new_list = [i for i in se_list if 'norm' in i]
    se1 = ''.join(random.sample(new_list,1))
    print(f"<PlaySE: {se1}, 90, 100, 0>")
    print('')

def se_soft(se_list):
    se_stop()
    new_list = [i for i in se_list if 'soft' in i]
    se1 = ''.join(random.sample(new_list,1))
    print(f"<PlaySE: {se1}, 90, 100, 0>")
    print('')

def se_z(se_list):
    se_stop()
    new_list = [i for i in se_list if '_z' in i]
    se1 = ''.join(random.sample(new_list,1))
    print(f"<PlaySE: {se1}, 90, 100, 0>")
    print('')

#パイズリのse,音声直接入力の汎用関数
def py_se(se):
    print("<PlaySE: "+se+", 90, 100, 0>")
    print('')

def sv_se(se_list):
    se1 = ''.join(random.sample(se_list,1))
    print(f"<PlaySE: {se1}, 90, 100, 0>")
    print('')

#喘ぎ声、セリフの関数を定義

#window関数
def window(name):
    print(f'<WindowPosition: Bottom><Background: Transparent><Name: {name}>')

#喘ぎ声の関数
def text1(name,list1,list2):
    window(name)
    message1 = ''.join(random.sample(list1,3))
    print(message1)
    message2 = ''.join(random.sample(list2,3))
    print(message2)
    print('')

#セリフの関数
def serif1(name,d_list):
    window(name)
    dia1= ''.join(random.sample(d_list,1))
    print(dia1)
    dia2= ''.join(random.sample(d_list,1))
    print(dia2)
    print('')

#セリフ１フレーズ
def serif2(name,d_list):
    window(name)
    dia2= ''.join(random.sample(d_list,1))
    print(dia2)
    print('')


#サキュバス喘ぎ声
def sv_text(list1,list2):
    window('サキュバス')
    message1 = ''.join(random.sample(list1,3))
    print(message1)
    message2 = ''.join(random.sample(list2,3))
    print(message2)
    print('')

#サキュバスセリフ
def sv_serif(d_list):
    window('サキュバス')
    dia2= ''.join(random.sample(d_list,1))
    print(dia2)
    dia3= ''.join(random.sample(d_list,1))
    print(dia3)
    print('')

#僕セリフ
def my_serif(list):
    window('僕')
    message = ''.join(random.sample(list,1))
    print(message)
    print('')


#エッチ後の関数
def jigo1(name):
    window(name)
    dia2= ''.join(random.sample(ol2,1))
    print(dia2)
    print('')

    #text1(name,list1 = sl1,list2 = al2)
    


#コモンイベント
def common():
    print('<CE: 2>')
    print('')

#画像変更
def image_change(image):
    print(f'<ShowPicture: 1, {image}, Scale[100][100]>')
    print('')

#普通の喘ぎ声1
def template1(name,se_list,image):
    image_change(image)
    se_soft(se_list)
    text1(name,list1 = sl1,list2 = al2)
    serif1(name,sl2)
    se_soft(se_list)
    text1(name,al2,al3)
    text1(name,al3,sl1)
    se_soft(se_list)
    text1(name,op1a,al3)
    serif1(name,dl2)
    se_norm(se_list)
    serif1(name,dl1)
    text1(name,op1a,al3)
    se_norm(se_list)
    text1(name,al3,sl1)
    serif1(name,dl2)
    se_norm(se_list)
    text1(name,al2,al3)
    serif1(name,dl1)
    se_norm(se_list)
    text1(name,al2,sl1)
    serif1(name,dl2)
    se_soft(se_list)
    text1(name,al3,al2)
    text1(name,op1a,sl1)
    se_hard(se_list)
    text1(name,op1a,al3)
    text1(name,sl1,al2)
    se_hard(se_list)
    serif1(name,dl2)
    text1(name,al3,sl1)
    se_hard(se_list)
    text1(name,al2,al3)
    se_hard(se_list)
    text1(name,al2,op1a)
    text1(name,al3,al2)
    se_hard(se_list)
    text1(name,al2,sl1)
    serif1(name,dl2)
    se_z(se_list)
    serif1(name,zl1)
    se_hard(se_list)
    text1(name,op1a,al3)
    se_z(se_list)
    serif1(name,zl2)
    common()
    se_stop()
    serif1(name,ol1)
    jigo1(name)
    serif1(name,ol1)

#普通の喘ぎ声2
def template2(name,se_list,image):
    image_change(image)
    se_soft(se_list)
    text1(name,list1 = sl1,list2 = al2)
    serif1(name,sl2)
    se_soft(se_list)
    text1(name,sl1,op1a)
    text1(name,al3,sl1)
    se_soft(se_list)
    text1(name,al2,al3)
    serif1(name,dl1)
    se_norm(se_list)
    serif1(name,dl2)
    text1(name,sl1,al3)
    se_norm(se_list)
    text1(name,op1a,al2)
    serif1(name,dl1)
    se_norm(se_list)
    text1(name,al3,sl1)
    serif1(name,dl2)
    se_norm(se_list)
    text1(name,al3,op1a)
    serif1(name,dl1)
    se_soft(se_list)
    text1(name,al3,al2)
    text1(name,op1a,al2)
    se_hard(se_list)
    text1(name,al2,op1a)
    text1(name,sl1,al2)
    se_hard(se_list)
    serif1(name,dl1)
    text1(name,al3,sl1)
    se_hard(se_list)
    text1(name,op1a,al2)
    se_hard(se_list)
    text1(name,al2,op1a)
    text1(name,al3,al2)
    se_hard(se_list)
    text1(name,op1a,sl1)
    serif1(name,dl2)
    se_z(se_list)
    serif1(name,zl1)
    se_hard(se_list)
    text1(name,sl1,al2)
    se_z(se_list)
    serif1(name,zl2)
    se_stop()
    common()
    serif1(name,ol1)
    jigo1(name)
    serif1(name,ol1)

#ギャルイベント＿始め
def gyal_opa(name,se_list,image):
    image_change(image)
    se_norm(se_list)
    text1(name,al3,sl1)
    serif1(name,ops_1a)
    se_norm(se_list)
    serif1(name,ops_1a)
    text1(name,op1a,al3)
    se_norm(se_list)
    text1(name,al2,op1a)
    text1(name,al3,al2)
    se_hard(se_list)
    serif1(name,ops_1a)
    text1(name,op1a,al2)
    se_hard(se_list)
    serif1(name,ops_1a)
    text1(name,al3,sl1)
    se_hard(se_list)
    text1(name,op1a,al3)
    serif1(name,ops_1a)
    se_norm(se_list)
    text1(name,al3,op1a)
    text1(name,sl1,al2)

#ハーレム始め　hrm1a,　pdl2
def hrm_begin(name,se_list,image):
    image_change(image)
    se_norm(se_list)
    text1(name,al2,sl1)
    serif1(name,hrm1a)
    se_norm(se_list)
    serif1(name,pdl2)
    text1(name,op1a,al3)
    se_norm(se_list)
    text1(name,al2,op1a)
    text1(name,al3,al2)
    se_hard(se_list)
    serif1(name,hrm1a)
    text1(name,op1a,al2)
    se_hard(se_list)
    serif1(name,pdl2)
    text1(name,al3,sl1)
    se_hard(se_list)
    text1(name,op1a,al3)
    serif1(name,pdl2)
    se_hard(se_list)
    text1(name,al3,op1a)
    text1(name,sl1,al2)
    se_hard(se_list)
    serif1(name,hrm1a)
    text1(name,op1a,al2)

def hrm_begin2(name,se_list,image):
    text = hrm_begin('女性',sub1,'hl_mc3.1')
    return

#ハーレムエッチ hrm_s, pf_1a
def hrm_sex1(name,se_list,image):
    image_change(image)
    se_soft(se_list)
    text1(name,list1 = sl1,list2 = al2)
    serif2(name,sl2)
    se_soft(se_list)
    text1(name,al2,al3)
    text1(name,al3,sl1)
    se_soft(se_list)
    text1(name,op1a,al3)
    serif2(name,hrm_s)
    se_norm(se_list)
    serif2(name,hrm_s)
    text1(name,op1a,al3)
    se_norm(se_list)
    text1(name,al3,sl1)
    serif2(name,hrm_s)
    se_norm(se_list)
    text1(name,al2,al3)
    serif2(name,hrm_s)
    se_norm(se_list)
    text1(name,al2,sl1)
    serif1(name,dl2)
    se_hard(se_list)
    serif2(name,hrm_s)
    text1(name,al3,sl1)
    se_hard(se_list)
    text1(name,op1a,al3)
    serif2(name,hrm_s)
    se_hard(se_list)
    serif2(name,hrm_s)
    text1(name,al2,sl1)
    se_z(se_list)
    serif1(name,zl1)
    se_hard(se_list)
    text1(name,op1a,al3)
    se_z(se_list)
    serif1(name,zl2)
    common()
    se_stop()
    serif1(name,ol1)
    serif2(name,pf_1a)
    serif1(name,ol1)

#パイズリ＿短い,psl1始まり　pdl1セリフ　pl1ずり音　pl2喘ぎ声,pyzuri = ['py_slow','py_norm','py_fast1', 'py_fast2'] #sya_1a  pf_1a
def py_short(name,image):
    image_change(image)
    serif2(name,psl1)
    py_se('py_slow')
    text1(name,pl1,pl2)
    text1(name,pl2,pl1)
    py_se('py_slow')
    text1(name,pl1,pl2)
    serif2(name,pdl1)
    py_se('py_norm')
    text1(name,pl2,pl1)
    serif2(name,pdl1)
    py_se('py_norm')
    text1(name,pl1,pl2)
    serif2(name,pdl1)
    py_se('py_fast1')
    text1(name,pl2,pl1)
    serif2(name,pdl1)
    py_se('py_fast2')
    text1(name,pl1,pl2)
    serif2(name,pdl1)
    py_se('py_fast1')
    text1(name,pl2,pl1)
    text1(name,pl1,pl2)
    py_se('py_fast2')
    text1(name,pl1,pl2)
    text1(name,pl2,pl1)
    py_se('py_fast1')
    serif2(name,pdl1)
    text1(name,pl1,pl2)

#パイズリ＿長い
def py_long(name,image):
    image_change(image)
    serif2(name,psl1)
    py_se('py_slow')
    text1(name,pl1,pl2)
    text1(name,pl2,pl1)
    py_se('py_slow')
    text1(name,pl1,pl2)
    serif2(name,pdl1)
    py_se('py_norm')
    text1(name,pl2,pl1)
    serif2(name,pdl1)
    py_se('py_norm')
    text1(name,pl1,pl2)
    serif2(name,pdl1)
    py_se('py_fast1')
    text1(name,pl2,pl1)
    serif2(name,pdl1)
    py_se('py_fast2')
    text1(name,pl1,pl2)
    serif2(name,pdl1)
    py_se('py_fast1')
    text1(name,pl2,pl1)
    text1(name,pl1,pl2)
    py_se('py_fast2')
    text1(name,pl1,pl2)
    text1(name,pl2,pl1)
    py_se('py_fast1')
    serif2(name,pdl1)
    text1(name,pl1,pl2)
    py_se('py_fast2')
    text1(name,pl1,pl2)
    text1(name,pl2,pl1)
    py_se('py_fast1')
    common()
    se_stop()
    serif2(name,sya_1a)
    serif2(name,pf_1a)

#喘ぎral1,あえぎral2,ぐおぉっ！ral3,セリフrsl1,セリフrsl2,中出しやめろrol1,中出し喘ぎrol2, 竿役中出しrb1,竿役中出し２rb2, sv_text(list1,list2),serif2(name,d_list)
#サキュバス
def scv(se_list,se_list2,image):
    image_change(image)
    sv_se(se_list)
    sv_text(ral1,ral2)
    sv_serif(rsl1)
    sv_se(se_list)
    sv_text(ral3,ral2)
    sv_serif(rsl2)
    sv_se(se_list)
    sv_text(ral2,ral1)
    sv_serif(rsl1)
    sv_se(se_list)
    sv_text(ral1,ral3)
    sv_text(ral2,ral1)
    sv_se(se_list)
    sv_text(ral1,ral3)
    sv_serif(rsl2)
    sv_se(se_list)
    sv_text(ral1,ral2)
    sv_serif(rsl1)
    sv_se(se_list)
    sv_text(ral2,ral3)
    sv_serif(rsl2)
    sv_se(se_list)
    sv_text(ral1,ral2)
    sv_serif(rsl1)
    sv_se(se_list)
    sv_text(ral2,ral3)
    sv_text(ral1,ral3)
    sv_se(se_list)
    sv_text(ral3,ral2)
    sv_serif(rsl2)
    sv_se(se_list)
    sv_text(ral2,ral1)
    sv_serif(rsl1)
    my_serif(rb1)
    sv_se(se_list2)
    sv_serif(rol1)
    my_serif(rb2)
    common()
    sv_serif(rol2)
    se_stop()
    sv_text(ol1,ol1)


#喘ぎ声テンプレ1
template1('りりか',ririka,'gl_l3.1')

#喘ぎ声テンプレ2
template2('もも',momo,'gl_l2.1')

#ギャルハーレム始め　りりか
gyal_opa('りりか',ririka,'gl_o1.3')

#ギャルハーレム始め もも
gyal_opa('もも',momo,'gl_l1.3')

#ギャルハーレム始め あおい
gyal_opa('あおい',aoi,'gl_l1.4')

#ハーレム始め
hrm_begin('女性',sub1,'hi_mc3.1')

def message(name,se_list,image):
    text = template1(name,se_list,image)
    return text

def hrm1(name,se_list,img):
    hrm_txt = hrm_begin(name,se_list,img)
    return hrm_txt



with open('hlmi2_wed.txt','a') as f:
    print(hrm1('女性',sub1,'hl_wd3.1'),file = f)

#ハーレムエッチ
hrm_sex1('ナース',sub1'img')

py_short('バニーガール',sub,'img')

py_long('バニーガール')

scv(sv1,sv1_z)