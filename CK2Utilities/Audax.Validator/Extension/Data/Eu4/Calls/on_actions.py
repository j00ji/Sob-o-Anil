

class Exports:
	pass

Exports.CountryFromCountry = [
	'on_federation_leader_change',
	'on_battle_won_country',
	'on_battle_lost_country',
	'on_diplomatic_annex',
	'on_war_lost',
	'on_war_won',
	'on_enforce_rebel_demands',
	'on_integrate',
	'on_annexed',
	'on_colonial_reintegration',
	'on_hre_member_true_religion',
	'on_hre_member_false_religion',
	'on_refuse_tribute',
	'on_accept_tribute',
	'on_mandate_of_heaven_gained',
	'on_mandate_of_heaven_lost',
	'on_dependency_gained',
	'on_dependency_lost',
	'on_chinese_empire_dismantled',
	'on_create_vassal',
	'on_country_released',
	'on_flagship_destroyed',
	'on_flagship_captured',
    'on_create_client_state',
    'on_emperor_elected',
    'on_replace_governor',
    'on_force_conversion',
    'on_royal_marriage',
    'on_alliance_created',
    'on_royal_marriage_broken',
    'on_alliance_broken',
    'on_war_ended',
    'on_colonial_nation_established',
    'on_separate_war_won',
    'on_overrun',
]

Exports.CountryFromProvince = [
	'on_siege_won_country',
	'on_siege_lost_country',
	'on_raid_coast',
	'on_scorch_earth',
	'on_naval_barrage',
	'on_barrage',
]

Exports.ProvinceFromProvince = [
	'on_minority_expelled',
]

Exports.ProvinceFromCountry = [
	'on_battle_won_province',
	'on_added_to_trade_company',
	'on_removed_from_company',
	'on_company_formed',
	'on_company_disolved',
	'on_battle_lost_province',
	'on_siege_won_province',
	'on_siege_lost_province',
	'on_abandon_colony',
	'on_explore_coast',
	'on_conquistador_empty',
	'on_conquistador_native',
	'on_regiment_recruited',
	'on_convert_by_trade_policy',
	'on_company_chartered',
	'on_province_owner_change',
    'on_colonist_boosting_colony',
    'on_conquest',
    'on_expanded_infrastructure',
    'on_core',
    'on_colony_established',
]

Exports.UnitFromCountry = [
	'on_mercenary_recruited',
]

EXPORT = {
	'KEY': 'on_actions',
	'VALUE': Exports,
}
