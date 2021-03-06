from pokeai.sim.move import Move
from pokeai.sim.poke_type import PokeType
from pokeai.sim.poke_db_move_flag import PokeDBMoveFlag

move_flag_db = {
    Move.ABSORB: PokeDBMoveFlag(PokeType.GRASS, 20, 100, 20, {"ja": "すいとる", "en": "Absorb"}),
    Move.ACID: PokeDBMoveFlag(PokeType.POISON, 40, 100, 30, {"ja": "ようかいえき", "en": "Acid"}),
    Move.ACIDARMOR: PokeDBMoveFlag(PokeType.POISON, 0, 100, 40, {"ja": "とける", "en": "Acid Armor"}),
    Move.AGILITY: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 30, {"ja": "こうそくいどう", "en": "Agility"}),
    Move.AMNESIA: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 20, {"ja": "ドわすれ", "en": "Amnesia"}),
    Move.AURORABEAM: PokeDBMoveFlag(PokeType.ICE, 65, 100, 20, {"ja": "オーロラビーム", "en": "Aurora Beam"}),
    Move.BARRAGE: PokeDBMoveFlag(PokeType.NORMAL, 15, 85, 20, {"ja": "たまなげ", "en": "Barrage"}),
    Move.BARRIER: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 30, {"ja": "バリアー", "en": "Barrier"}),
    Move.BIDE: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 10, {"ja": "がまん", "en": "Bide"}),
    Move.BIND: PokeDBMoveFlag(PokeType.NORMAL, 15, 75, 20, {"ja": "しめつける", "en": "Bind"}),
    Move.BITE: PokeDBMoveFlag(PokeType.NORMAL, 60, 100, 25, {"ja": "かみつく", "en": "Bite"}),
    Move.BLIZZARD: PokeDBMoveFlag(PokeType.ICE, 120, 90, 5, {"ja": "ふぶき", "en": "Blizzard"}),
    Move.BODYSLAM: PokeDBMoveFlag(PokeType.NORMAL, 85, 100, 15, {"ja": "のしかかり", "en": "Body Slam"}),
    Move.BONECLUB: PokeDBMoveFlag(PokeType.GROUND, 65, 85, 20, {"ja": "ホネこんぼう", "en": "Bone Club"}),
    Move.BONEMERANG: PokeDBMoveFlag(PokeType.GROUND, 50, 90, 10, {"ja": "ホネブーメラン", "en": "Bonemerang"}),
    Move.BUBBLE: PokeDBMoveFlag(PokeType.WATER, 20, 100, 30, {"ja": "あわ", "en": "Bubble"}),
    Move.BUBBLEBEAM: PokeDBMoveFlag(PokeType.WATER, 65, 100, 20, {"ja": "バブルこうせん", "en": "Bubble Beam"}),
    Move.CLAMP: PokeDBMoveFlag(PokeType.WATER, 35, 75, 10, {"ja": "からではさむ", "en": "Clamp"}),
    Move.COMETPUNCH: PokeDBMoveFlag(PokeType.NORMAL, 18, 85, 15, {"ja": "れんぞくパンチ", "en": "Comet Punch"}),
    Move.CONFUSERAY: PokeDBMoveFlag(PokeType.GHOST, 0, 100, 10, {"ja": "あやしいひかり", "en": "Confuse Ray"}),
    Move.CONFUSION: PokeDBMoveFlag(PokeType.PSYCHC, 50, 100, 25, {"ja": "ねんりき", "en": "Confusion"}),
    Move.CONSTRICT: PokeDBMoveFlag(PokeType.NORMAL, 10, 100, 35, {"ja": "からみつく", "en": "Constrict"}),
    Move.CONVERSION: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 30, {"ja": "テクスチャー", "en": "Conversion"}),
    Move.COUNTER: PokeDBMoveFlag(PokeType.FIGHT, 0, 100, 20, {"ja": "カウンター", "en": "Counter"}),
    Move.CRABHAMMER: PokeDBMoveFlag(PokeType.WATER, 90, 85, 10, {"ja": "クラブハンマー", "en": "Crabhammer"}),
    Move.CUT: PokeDBMoveFlag(PokeType.NORMAL, 50, 95, 30, {"ja": "いあいぎり", "en": "Cut"}),
    Move.DEFENSECURL: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 40, {"ja": "まるくなる", "en": "Defense Curl"}),
    Move.DIG: PokeDBMoveFlag(PokeType.GROUND, 100, 100, 10, {"ja": "あなをほる", "en": "Dig"}),
    Move.DISABLE: PokeDBMoveFlag(PokeType.NORMAL, 0, 55, 20, {"ja": "かなしばり", "en": "Disable"}),
    Move.DIZZYPUNCH: PokeDBMoveFlag(PokeType.NORMAL, 70, 100, 10, {"ja": "ピヨピヨパンチ", "en": "Dizzy Punch"}),
    Move.DOUBLEEDGE: PokeDBMoveFlag(PokeType.NORMAL, 100, 100, 15, {"ja": "すてみタックル", "en": "Double-Edge"}),
    Move.DOUBLEKICK: PokeDBMoveFlag(PokeType.FIGHT, 30, 100, 30, {"ja": "にどげり", "en": "Double Kick"}),
    Move.DOUBLESLAP: PokeDBMoveFlag(PokeType.NORMAL, 15, 85, 10, {"ja": "おうふくビンタ", "en": "Double Slap"}),
    Move.DOUBLETEAM: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 15, {"ja": "かげぶんしん", "en": "Double Team"}),
    Move.DRAGONRAGE: PokeDBMoveFlag(PokeType.DRAGON, 0, 100, 10, {"ja": "りゅうのいかり", "en": "Dragon Rage"}),
    Move.DREAMEATER: PokeDBMoveFlag(PokeType.PSYCHC, 100, 100, 15, {"ja": "ゆめくい", "en": "Dream Eater"}),
    Move.DRILLPECK: PokeDBMoveFlag(PokeType.FLYING, 80, 100, 20, {"ja": "ドリルくちばし", "en": "Drill Peck"}),
    Move.EARTHQUAKE: PokeDBMoveFlag(PokeType.GROUND, 100, 100, 10, {"ja": "じしん", "en": "Earthquake"}),
    Move.EGGBOMB: PokeDBMoveFlag(PokeType.NORMAL, 100, 75, 10, {"ja": "タマゴばくだん", "en": "Egg Bomb"}),
    Move.EMBER: PokeDBMoveFlag(PokeType.FIRE, 40, 100, 25, {"ja": "ひのこ", "en": "Ember"}),
    Move.EXPLOSION: PokeDBMoveFlag(PokeType.NORMAL, 170, 100, 5, {"ja": "だいばくはつ", "en": "Explosion"}),
    Move.FIREBLAST: PokeDBMoveFlag(PokeType.FIRE, 120, 85, 5, {"ja": "だいもんじ", "en": "Fire Blast"}),
    Move.FIREPUNCH: PokeDBMoveFlag(PokeType.FIRE, 75, 100, 15, {"ja": "ほのおのパンチ", "en": "Fire Punch"}),
    Move.FIRESPIN: PokeDBMoveFlag(PokeType.FIRE, 15, 70, 15, {"ja": "ほのおのうず", "en": "Fire Spin"}),
    Move.FISSURE: PokeDBMoveFlag(PokeType.GROUND, 0, 30, 5, {"ja": "じわれ", "en": "Fissure"}),
    Move.FLAMETHROWER: PokeDBMoveFlag(PokeType.FIRE, 95, 100, 15, {"ja": "かえんほうしゃ", "en": "Flamethrower"}),
    Move.FLASH: PokeDBMoveFlag(PokeType.NORMAL, 0, 70, 20, {"ja": "フラッシュ", "en": "Flash"}),
    Move.FLY: PokeDBMoveFlag(PokeType.FLYING, 70, 95, 15, {"ja": "そらをとぶ", "en": "Fly"}),
    Move.FOCUSENERGY: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 15, {"ja": "きあいだめ", "en": "Focus Energy"}),
    Move.FURYATTACK: PokeDBMoveFlag(PokeType.NORMAL, 15, 85, 20, {"ja": "みだれづき", "en": "Fury Attack"}),
    Move.FURYSWIPES: PokeDBMoveFlag(PokeType.NORMAL, 18, 80, 15, {"ja": "みだれひっかき", "en": "Fury Swipes"}),
    Move.GLARE: PokeDBMoveFlag(PokeType.NORMAL, 0, 75, 30, {"ja": "へびにらみ", "en": "Glare"}),
    Move.GROWL: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 40, {"ja": "なきごえ", "en": "Growl"}),
    Move.GROWTH: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 40, {"ja": "せいちょう", "en": "Growth"}),
    Move.GUILLOTINE: PokeDBMoveFlag(PokeType.NORMAL, 0, 30, 5, {"ja": "ハサミギロチン", "en": "Guillotine"}),
    Move.GUST: PokeDBMoveFlag(PokeType.NORMAL, 40, 100, 35, {"ja": "かぜおこし", "en": "Gust"}),
    Move.HARDEN: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 30, {"ja": "かたくなる", "en": "Harden"}),
    Move.HAZE: PokeDBMoveFlag(PokeType.ICE, 0, 100, 30, {"ja": "くろいきり", "en": "Haze"}),
    Move.HEADBUTT: PokeDBMoveFlag(PokeType.NORMAL, 70, 100, 15, {"ja": "ずつき", "en": "Headbutt"}),
    Move.HIGHJUMPKICK: PokeDBMoveFlag(PokeType.FIGHT, 85, 90, 20, {"ja": "とびひざげり", "en": "High Jump Kick"}),
    Move.HORNATTACK: PokeDBMoveFlag(PokeType.NORMAL, 65, 100, 25, {"ja": "つのでつく", "en": "Horn Attack"}),
    Move.HORNDRILL: PokeDBMoveFlag(PokeType.NORMAL, 0, 30, 5, {"ja": "つのドリル", "en": "Horn Drill"}),
    Move.HYDROPUMP: PokeDBMoveFlag(PokeType.WATER, 120, 80, 5, {"ja": "ハイドロポンプ", "en": "Hydro Pump"}),
    Move.HYPERBEAM: PokeDBMoveFlag(PokeType.NORMAL, 150, 90, 5, {"ja": "はかいこうせん", "en": "Hyper Beam"}),
    Move.HYPERFANG: PokeDBMoveFlag(PokeType.NORMAL, 80, 90, 15, {"ja": "ひっさつまえば", "en": "Hyper Fang"}),
    Move.HYPNOSIS: PokeDBMoveFlag(PokeType.PSYCHC, 0, 60, 20, {"ja": "さいみんじゅつ", "en": "Hypnosis"}),
    Move.ICEBEAM: PokeDBMoveFlag(PokeType.ICE, 95, 100, 10, {"ja": "れいとうビーム", "en": "Ice Beam"}),
    Move.ICEPUNCH: PokeDBMoveFlag(PokeType.ICE, 75, 100, 15, {"ja": "れいとうパンチ", "en": "Ice Punch"}),
    Move.JUMPKICK: PokeDBMoveFlag(PokeType.FIGHT, 70, 95, 25, {"ja": "とびげり", "en": "Jump Kick"}),
    Move.KARATECHOP: PokeDBMoveFlag(PokeType.NORMAL, 50, 100, 25, {"ja": "からてチョップ", "en": "Karate Chop"}),
    Move.KINESIS: PokeDBMoveFlag(PokeType.PSYCHC, 0, 80, 15, {"ja": "スプーンまげ", "en": "Kinesis"}),
    Move.LEECHLIFE: PokeDBMoveFlag(PokeType.BUG, 20, 100, 15, {"ja": "きゅうけつ", "en": "Leech Life"}),
    Move.LEECHSEED: PokeDBMoveFlag(PokeType.GRASS, 0, 90, 10, {"ja": "やどりぎのタネ", "en": "Leech Seed"}),
    Move.LEER: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 30, {"ja": "にらみつける", "en": "Leer"}),
    Move.LICK: PokeDBMoveFlag(PokeType.GHOST, 20, 100, 30, {"ja": "したでなめる", "en": "Lick"}),
    Move.LIGHTSCREEN: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 30, {"ja": "ひかりのかべ", "en": "Light Screen"}),
    Move.LOVELYKISS: PokeDBMoveFlag(PokeType.NORMAL, 0, 70, 10, {"ja": "あくまのキッス", "en": "Lovely Kiss"}),
    Move.LOWKICK: PokeDBMoveFlag(PokeType.FIGHT, 50, 90, 20, {"ja": "けたぐり", "en": "Low Kick"}),
    Move.MEDITATE: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 40, {"ja": "ヨガのポーズ", "en": "Meditate"}),
    Move.MEGADRAIN: PokeDBMoveFlag(PokeType.GRASS, 40, 100, 10, {"ja": "メガドレイン", "en": "Mega Drain"}),
    Move.MEGAKICK: PokeDBMoveFlag(PokeType.NORMAL, 120, 75, 5, {"ja": "メガトンキック", "en": "Mega Kick"}),
    Move.MEGAPUNCH: PokeDBMoveFlag(PokeType.NORMAL, 80, 85, 20, {"ja": "メガトンパンチ", "en": "Mega Punch"}),
    Move.METRONOME: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 10, {"ja": "ゆびをふる", "en": "Metronome"}),
    Move.MIMIC: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 10, {"ja": "ものまね", "en": "Mimic"}),
    Move.MINIMIZE: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 20, {"ja": "ちいさくなる", "en": "Minimize"}),
    Move.MIRRORMOVE: PokeDBMoveFlag(PokeType.FLYING, 0, 100, 20, {"ja": "オウムがえし", "en": "Mirror Move"}),
    Move.MIST: PokeDBMoveFlag(PokeType.ICE, 0, 100, 30, {"ja": "しろいきり", "en": "Mist"}),
    Move.NIGHTSHADE: PokeDBMoveFlag(PokeType.GHOST, 0, 100, 15, {"ja": "ナイトヘッド", "en": "Night Shade"}),
    Move.PAYDAY: PokeDBMoveFlag(PokeType.NORMAL, 40, 100, 20, {"ja": "ネコにこばん", "en": "Pay Day"}),
    Move.PECK: PokeDBMoveFlag(PokeType.FLYING, 35, 100, 35, {"ja": "つつく", "en": "Peck"}),
    Move.PETALDANCE: PokeDBMoveFlag(PokeType.GRASS, 70, 100, 20, {"ja": "はなびらのまい", "en": "Petal Dance"}),
    Move.PINMISSILE: PokeDBMoveFlag(PokeType.BUG, 14, 85, 20, {"ja": "ミサイルばり", "en": "Pin Missile"}),
    Move.POISONGAS: PokeDBMoveFlag(PokeType.POISON, 0, 55, 40, {"ja": "どくガス", "en": "Poison Gas"}),
    Move.POISONPOWDER: PokeDBMoveFlag(PokeType.POISON, 0, 75, 35, {"ja": "どくのこな", "en": "Poison Powder"}),
    Move.POISONSTING: PokeDBMoveFlag(PokeType.POISON, 15, 100, 35, {"ja": "どくばり", "en": "Poison Sting"}),
    Move.POUND: PokeDBMoveFlag(PokeType.NORMAL, 40, 100, 35, {"ja": "はたく", "en": "Pound"}),
    Move.PSYBEAM: PokeDBMoveFlag(PokeType.PSYCHC, 65, 100, 20, {"ja": "サイケこうせん", "en": "Psybeam"}),
    Move.PSYCHIC: PokeDBMoveFlag(PokeType.PSYCHC, 90, 100, 10, {"ja": "サイコキネシス", "en": "Psychic"}),
    Move.PSYWAVE: PokeDBMoveFlag(PokeType.PSYCHC, 0, 80, 15, {"ja": "サイコウェーブ", "en": "Psywave"}),
    Move.QUICKATTACK: PokeDBMoveFlag(PokeType.NORMAL, 40, 100, 30, {"ja": "でんこうせっか", "en": "Quick Attack"}),
    Move.RAGE: PokeDBMoveFlag(PokeType.NORMAL, 20, 100, 20, {"ja": "いかり", "en": "Rage"}),
    Move.RAZORLEAF: PokeDBMoveFlag(PokeType.GRASS, 55, 95, 25, {"ja": "はっぱカッター", "en": "Razor Leaf"}),
    Move.RAZORWIND: PokeDBMoveFlag(PokeType.NORMAL, 80, 75, 10, {"ja": "かまいたち", "en": "Razor Wind"}),
    Move.RECOVER: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 20, {"ja": "じこさいせい", "en": "Recover"}),
    Move.REFLECT: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 20, {"ja": "リフレクター", "en": "Reflect"}),
    Move.REST: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 10, {"ja": "ねむる", "en": "Rest"}),
    Move.ROAR: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 20, {"ja": "ほえる", "en": "Roar"}),
    Move.ROCKSLIDE: PokeDBMoveFlag(PokeType.ROCK, 75, 90, 10, {"ja": "いわなだれ", "en": "Rock Slide"}),
    Move.ROCKTHROW: PokeDBMoveFlag(PokeType.ROCK, 50, 65, 15, {"ja": "いわおとし", "en": "Rock Throw"}),
    Move.ROLLINGKICK: PokeDBMoveFlag(PokeType.FIGHT, 60, 85, 15, {"ja": "まわしげり", "en": "Rolling Kick"}),
    Move.SANDATTACK: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 15, {"ja": "すなかけ", "en": "Sand Attack"}),
    Move.SCRATCH: PokeDBMoveFlag(PokeType.NORMAL, 40, 100, 30, {"ja": "ひっかく", "en": "Scratch"}),
    Move.SCREECH: PokeDBMoveFlag(PokeType.NORMAL, 0, 85, 40, {"ja": "いやなおと", "en": "Screech"}),
    Move.SEISMICTOSS: PokeDBMoveFlag(PokeType.FIGHT, 0, 100, 20, {"ja": "ちきゅうなげ", "en": "Seismic Toss"}),
    Move.SELFDESTRUCT: PokeDBMoveFlag(PokeType.NORMAL, 130, 100, 5, {"ja": "じばく", "en": "Self-Destruct"}),
    Move.SHARPEN: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 30, {"ja": "かくばる", "en": "Sharpen"}),
    Move.SING: PokeDBMoveFlag(PokeType.NORMAL, 0, 55, 15, {"ja": "うたう", "en": "Sing"}),
    Move.SKULLBASH: PokeDBMoveFlag(PokeType.NORMAL, 100, 100, 15, {"ja": "ロケットずつき", "en": "Skull Bash"}),
    Move.SKYATTACK: PokeDBMoveFlag(PokeType.FLYING, 140, 90, 5, {"ja": "ゴッドバード", "en": "Sky Attack"}),
    Move.SLAM: PokeDBMoveFlag(PokeType.NORMAL, 80, 75, 20, {"ja": "たたきつける", "en": "Slam"}),
    Move.SLASH: PokeDBMoveFlag(PokeType.NORMAL, 70, 100, 20, {"ja": "きりさく", "en": "Slash"}),
    Move.SLEEPPOWDER: PokeDBMoveFlag(PokeType.GRASS, 0, 75, 15, {"ja": "ねむりごな", "en": "Sleep Powder"}),
    Move.SLUDGE: PokeDBMoveFlag(PokeType.POISON, 65, 100, 20, {"ja": "ヘドロこうげき", "en": "Sludge"}),
    Move.SMOG: PokeDBMoveFlag(PokeType.POISON, 20, 70, 20, {"ja": "スモッグ", "en": "Smog"}),
    Move.SMOKESCREEN: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 20, {"ja": "えんまく", "en": "Smokescreen"}),
    Move.SOFTBOILED: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 10, {"ja": "タマゴうみ", "en": "Soft-Boiled"}),
    Move.SOLARBEAM: PokeDBMoveFlag(PokeType.GRASS, 120, 100, 10, {"ja": "ソーラービーム", "en": "Solar Beam"}),
    Move.SONICBOOM: PokeDBMoveFlag(PokeType.NORMAL, 0, 90, 20, {"ja": "ソニックブーム", "en": "Sonic Boom"}),
    Move.SPIKECANNON: PokeDBMoveFlag(PokeType.NORMAL, 20, 100, 15, {"ja": "とげキャノン", "en": "Spike Cannon"}),
    Move.SPLASH: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 40, {"ja": "はねる", "en": "Splash"}),
    Move.SPORE: PokeDBMoveFlag(PokeType.GRASS, 0, 100, 15, {"ja": "キノコのほうし", "en": "Spore"}),
    Move.STOMP: PokeDBMoveFlag(PokeType.NORMAL, 65, 100, 20, {"ja": "ふみつけ", "en": "Stomp"}),
    Move.STRENGTH: PokeDBMoveFlag(PokeType.NORMAL, 80, 100, 15, {"ja": "かいりき", "en": "Strength"}),
    Move.STRINGSHOT: PokeDBMoveFlag(PokeType.BUG, 0, 95, 40, {"ja": "いとをはく", "en": "String Shot"}),
    Move.STRUGGLE: PokeDBMoveFlag(PokeType.NORMAL, 50, 100, 10, {"ja": "わるあがき", "en": "Struggle"}),
    Move.STUNSPORE: PokeDBMoveFlag(PokeType.GRASS, 0, 75, 30, {"ja": "しびれごな", "en": "Stun Spore"}),
    Move.SUBMISSION: PokeDBMoveFlag(PokeType.FIGHT, 80, 80, 25, {"ja": "じごくぐるま", "en": "Submission"}),
    Move.SUBSTITUTE: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 10, {"ja": "みがわり", "en": "Substitute"}),
    Move.SUPERFANG: PokeDBMoveFlag(PokeType.NORMAL, 0, 90, 10, {"ja": "いかりのまえば", "en": "Super Fang"}),
    Move.SUPERSONIC: PokeDBMoveFlag(PokeType.NORMAL, 0, 55, 20, {"ja": "ちょうおんぱ", "en": "Supersonic"}),
    Move.SURF: PokeDBMoveFlag(PokeType.WATER, 95, 100, 15, {"ja": "なみのり", "en": "Surf"}),
    Move.SWIFT: PokeDBMoveFlag(PokeType.NORMAL, 60, 100, 20, {"ja": "スピードスター", "en": "Swift"}),
    Move.SWORDSDANCE: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 30, {"ja": "つるぎのまい", "en": "Swords Dance"}),
    Move.TACKLE: PokeDBMoveFlag(PokeType.NORMAL, 35, 95, 35, {"ja": "たいあたり", "en": "Tackle"}),
    Move.TAILWHIP: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 30, {"ja": "しっぽをふる", "en": "Tail Whip"}),
    Move.TAKEDOWN: PokeDBMoveFlag(PokeType.NORMAL, 90, 85, 20, {"ja": "とっしん", "en": "Take Down"}),
    Move.TELEPORT: PokeDBMoveFlag(PokeType.PSYCHC, 0, 100, 20, {"ja": "テレポート", "en": "Teleport"}),
    Move.THRASH: PokeDBMoveFlag(PokeType.NORMAL, 90, 100, 20, {"ja": "あばれる", "en": "Thrash"}),
    Move.THUNDER: PokeDBMoveFlag(PokeType.ELECTR, 120, 70, 10, {"ja": "かみなり", "en": "Thunder"}),
    Move.THUNDERBOLT: PokeDBMoveFlag(PokeType.ELECTR, 95, 100, 15, {"ja": "10まんボルト", "en": "Thunderbolt"}),
    Move.THUNDERPUNCH: PokeDBMoveFlag(PokeType.ELECTR, 75, 100, 15, {"ja": "かみなりパンチ", "en": "Thunder Punch"}),
    Move.THUNDERSHOCK: PokeDBMoveFlag(PokeType.ELECTR, 40, 100, 30, {"ja": "でんきショック", "en": "Thunder Shock"}),
    Move.THUNDERWAVE: PokeDBMoveFlag(PokeType.ELECTR, 0, 100, 20, {"ja": "でんじは", "en": "Thunder Wave"}),
    Move.TOXIC: PokeDBMoveFlag(PokeType.POISON, 0, 85, 10, {"ja": "どくどく", "en": "Toxic"}),
    Move.TRANSFORM: PokeDBMoveFlag(PokeType.NORMAL, 0, 100, 10, {"ja": "へんしん", "en": "Transform"}),
    Move.TRIATTACK: PokeDBMoveFlag(PokeType.NORMAL, 80, 100, 10, {"ja": "トライアタック", "en": "Tri Attack"}),
    Move.TWINEEDLE: PokeDBMoveFlag(PokeType.BUG, 25, 100, 20, {"ja": "ダブルニードル", "en": "Twineedle"}),
    Move.VICEGRIP: PokeDBMoveFlag(PokeType.NORMAL, 55, 100, 30, {"ja": "はさむ", "en": "Vice Grip"}),
    Move.VINEWHIP: PokeDBMoveFlag(PokeType.GRASS, 35, 100, 10, {"ja": "つるのムチ", "en": "Vine Whip"}),
    Move.WATERFALL: PokeDBMoveFlag(PokeType.WATER, 80, 100, 15, {"ja": "たきのぼり", "en": "Waterfall"}),
    Move.WATERGUN: PokeDBMoveFlag(PokeType.WATER, 40, 100, 25, {"ja": "みずでっぽう", "en": "Water Gun"}),
    Move.WHIRLWIND: PokeDBMoveFlag(PokeType.NORMAL, 0, 85, 20, {"ja": "ふきとばし", "en": "Whirlwind"}),
    Move.WINGATTACK: PokeDBMoveFlag(PokeType.FLYING, 35, 100, 35, {"ja": "つばさでうつ", "en": "Wing Attack"}),
    Move.WITHDRAW: PokeDBMoveFlag(PokeType.WATER, 0, 100, 40, {"ja": "からにこもる", "en": "Withdraw"}),
    Move.WRAP: PokeDBMoveFlag(PokeType.NORMAL, 15, 85, 20, {"ja": "まきつく", "en": "Wrap"}),
}
