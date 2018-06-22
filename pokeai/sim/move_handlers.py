from typing import List

from pokeai.sim.game_rng import GameRNGReason
from pokeai.sim.move_handler_context import MoveHandlerContext
from pokeai.sim.poke_type import PokeType


def check_hit_attack_default(context: MoveHandlerContext) -> bool:
    """
    攻撃技のデフォルト命中判定
    :param context:
    :return:
    """
    # TODO: 発動条件(ランク変化が可能か、状態異常の相手に状態異常技を打っていないか、相手があなをほる状態でないか)
    # TODO: 相性（攻撃技）
    # TODO: 相性（補助技：毒タイプに対するどくどくや地面タイプに対するでんじは）

    # 命中率による判定
    # https://wiki.xn--rckteqa2e.com/wiki/%E5%91%BD%E4%B8%AD
    if context.flag.accuracy > 0:
        # 技の命中率×自分のランク補正(命中率)÷相手のランク補正(回避率)
        hit_ratio_table = {100: 255, 95: 242, 90: 229, 85: 216,
                           80: 204, 75: 191, 70: 178, 60: 152, 55: 140, 50: 127, 0: 0}
        hit_ratio = hit_ratio_table[context.flag.accuracy]
        hit_ratio = hit_ratio * 2 // (-context.attack_poke.rank_accuracy.value + 2)
        hit_ratio = hit_ratio * 2 // (context.defend_poke.rank_evasion.value + 2)
        # 1~255の乱数と比較
        hit_judge_rnd = context.field.rng.gen(context.attack_player, GameRNGReason.HIT, 254) + 1
        if hit_ratio <= hit_judge_rnd:
            context.field.put_record_other("命中率による判定で外れた")
            return False
    else:
        # 必中技
        pass

    return True


def calc_damage_core(power: int, attack_level: int, attack: int, defense: int,
                     critical: bool, same_type: bool, type_matches_x2: List[int],
                     rnd: int):
    """
    ダメージ計算のコア。
    :param power: 威力
    :param attack_level: 攻撃側レベル(急所考慮なし)
    :param attack: 攻撃側こうげき/とくしゅ(急所考慮あり)
    :param defense: 防御側ぼうぎょ/とくしゅ(急所考慮あり)
    :param critical: 急所
    :param same_type: タイプ一致
    :param type_matches_x2: 技と防御側相性(タイプごとに、相性補正の2倍の値を与える: 等倍なら2、半減なら1)
    :param rnd: 0~38の乱数
    :return:
    """
    assert 0 <= rnd <= 38
    if critical:
        attack_level *= 2
    damage = attack_level * 2 // 5 + 2
    damage = damage * power * attack // defense // 50 + 2
    if same_type:
        damage = damage * 3 // 2
    for tmx2 in type_matches_x2:
        damage = damage * tmx2 // 2
    damage = damage * (rnd + 217) // 255
    return damage


def calc_damage(context: MoveHandlerContext) -> int:
    """
    通常攻撃技のダメージ計算を行う。
    """
    power = context.flag.power  # 威力
    attack_level = context.attack_poke.lv  # 攻撃側レベル

    # 急所判定
    critical_ratio = context.attack_poke.base_s // 2
    # TODO: はっぱカッター急所率
    critical = context.field.rng.gen(context.attack_player, GameRNGReason.CRITICAL, 255) + 1 < critical_ratio
    if critical:
        context.field.put_record_other("きゅうしょにあたった")
    # タイプ処理
    move_type = context.flag.move_type
    same_type = move_type in context.attack_poke.poke_types
    type_matches_x2 = PokeType.get_match_list(move_type, context.defend_poke.poke_types)
    type_matches_prod = type_matches_x2[0] * (type_matches_x2[1] if len(type_matches_x2) == 2 else 2)
    if type_matches_prod > 4:
        context.field.put_record_other("こうかはばつぐんだ")
    elif type_matches_prod == 0:
        context.field.put_record_other("こうかはないようだ")
        # 命中判定時点で本来外れているので、ダメージ計算はしないはず
    elif type_matches_prod < 4:
        context.field.put_record_other("こうかはいまひとつのようだ")

    if PokeType.is_physical(move_type):
        attack = context.attack_poke.eff_a(critical)
        defense = context.defend_poke.eff_b(critical)
    else:
        attack = context.attack_poke.eff_c(critical)
        defense = context.defend_poke.eff_c(critical)
    damage_rnd = context.field.rng.gen(context.attack_player, GameRNGReason.DAMAGE, 38)
    damage = calc_damage_core(power=power,
                              attack_level=attack_level,
                              attack=attack, defense=defense,
                              critical=critical, same_type=same_type,
                              type_matches_x2=type_matches_x2, rnd=damage_rnd)
    if damage > context.defend_poke.hp:
        # ダメージは受け側のHP以下
        damage = context.defend_poke.hp
    return damage


def launch_move_attack_default(context: MoveHandlerContext):
    """
    攻撃技のデフォルト発動
    :param context:
    :return:
    """
    # 威力・相性に従ってダメージ計算し、受け手のHPから減算
    damage = calc_damage(context)
    context.field.put_record_other(f"ダメージ: {damage}")
    context.defend_poke.hp_incr(-damage)


def check_side_effect_none(context: MoveHandlerContext) -> bool:
    """
    追加効果なし
    :param context:
    :return:
    """
    return False


def launch_side_effect_none(context: MoveHandlerContext):
    """
    追加効果なし
    :param context:
    :return:
    """
    return