function Div(elem)
	local openings = pandoc.List()
	local closings = pandoc.List()
	if elem.classes:find("outcomes") then
		openings:insert(
			pandoc.RawBlock("typst", '#rect(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.checkmark.box')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Learning outcomes")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("input") then
		openings:insert(pandoc.RawBlock("typst", "#emoji.keyboard"))
		openings:insert(pandoc.Strong(pandoc.Str("Input")))
	end

	if elem.classes:find("output") then
		openings:insert(pandoc.RawBlock("typst", "#emoji.printer"))
		openings:insert(pandoc.Strong(pandoc.Str("Output")))
	end

	if elem.classes:find("example") then
		openings:insert(
			pandoc.RawBlock("typst", '#block(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.rocket')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Example")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("tip") then
		openings:insert(
			pandoc.RawBlock("typst", '#rect(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.person.sassy')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Tip")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("important") then
		openings:insert(
			pandoc.RawBlock("typst", '#rect(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.excl.double')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Important!")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("warning") then
		openings:insert(
			pandoc.RawBlock("typst", '#rect(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.warning')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Warning")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("checklist") then
		openings:insert(
			pandoc.RawBlock("typst", '#rect(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.checkmark.box')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Checklist")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("aside") then
		openings:insert(
			pandoc.RawBlock("typst", '#block(width: 100%, inset: 12pt, stroke: (dash: "dashed"))[#emoji.star ')
		)
		openings:insert(pandoc.Strong(pandoc.Str("Aside")))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("columns") then
		openings:insert(pandoc.RawBlock("typst", "#columns(2)["))
		closings:insert(pandoc.RawBlock("typst", "]"))
	end

	if elem.classes:find("column") then
		-- blindly add a column break after every column.
		closings:insert(pandoc.RawBlock("typst", "#colbreak()"))
	end

	openings:insert(elem)
	openings:extend(closings)

	return openings
end
