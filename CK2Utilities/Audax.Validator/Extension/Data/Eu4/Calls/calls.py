

class Exports:
	pass

Exports.AllScopes = ['Country', 'Province', 'Global', 'Unit']
Exports.AllNonGlobalScopes = ['Country', 'Province', 'Unit']


def make_any_and_random_scopes(name, source, target, plural=False):
	return """
(ContextValidator {source}Trigger) = {{ Members = {{
	(N N) = {{ Left = any_{name}{ending} Right = {target}Trigger }}
	(N N) = {{ Left = all_{name}{ending} Right = {target}Trigger }}
}} }}
(ContextValidator {source}Command) = {{ Members = {{
	(N N) = {{ Left = every_{name} Right = {target}AllowLimitClause }}
	(N N) = {{ Left = random_{name} Right = {target}AllowLimitClause }}
}} }}""".format(
		name=name,
		source=source,
		target=target,
        ending='s' if plural else ''
	)

Exports.make_any_and_random_scopes = make_any_and_random_scopes


EXPORT = {
	'KEY': 'calls',
	'VALUE': Exports
}
